import csv
import streamlit as st
from dotenv import load_dotenv
import os
import io
from google import generativeai as genai
import pandas as pd

load_dotenv()

st.title("AI Financial Analyser")
st.divider()
st.badge("By Parikshit")
st.markdown("Upload your financial documents and get AI-powered insights!")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

def extract_text_from_csv(file_bytes):
    try:
        csv_string = file_bytes.decode("utf-8")
        csv_reader = csv.reader(io.StringIO(csv_string))
        text = ""
        rows = list(csv_reader)
        
        if rows:
            text += "CSV Data:\n"
            text += "=" * 50 + "\n\n"
            
            headers = rows[0]
            text += "Columns: " + ", ".join(headers) + "\n\n"
            text += f"Total rows: {len(rows) - 1}\n\n"
            text += "Sample Data:\n"
            text += "-" * 30 + "\n"
            
            for i, row in enumerate(rows[:11]):
                if i == 0:
                    text += " | ".join(f"{cell:>12}" for cell in row) + "\n"
                    text += "-" * (len(" | ".join(f"{cell:>12}" for cell in row))) + "\n"
                else:
                    text += " | ".join(f"{cell:>12}" for cell in row) + "\n"
            
            if len(rows) > 11:
                text += f"\n... and {len(rows) - 11} more rows\n"
                
        return text
    except Exception as e:
        return f"Could not extract text from CSV: {str(e)}"

def extract_text(file):
    file_type = file.type
    file_content = file.read()
    
    if file_type == "text/csv" or file.name.endswith('.csv'):
        return extract_text_from_csv(file_content)
    else:
        return "Only CSV files are supported"

uploaded_file = st.file_uploader("Upload your financial CSV document", type=["csv"])

if uploaded_file is not None:
    st.success(f"CSV file uploaded successfully: {uploaded_file.name}")
    
    with st.spinner("Processing CSV data..."):
        document_text = extract_text(uploaded_file)
    
    if document_text and "Could not extract" not in document_text and "Only CSV files" not in document_text:
        st.subheader("CSV Data Preview")
        st.text_area("Extracted Data", value=document_text[:1500] + "..." if len(document_text) > 1500 else document_text, height=300)
        
        try:
            uploaded_file.seek(0)
            df = pd.read_csv(uploaded_file)
            st.subheader("Data Table View")
            st.dataframe(df.head(10))
            
            if len(df) > 10:
                st.info(f"Showing first 10 rows. Total rows: {len(df)}")
                
        except Exception as e:
            st.warning(f"Could not display table view: {e}")
        
        analysis_type = st.selectbox(
            "Choose analysis type:",
            ["Financial Summary", "Expense Analysis", "Revenue Analysis", "Budget Analysis", "Trend Analysis", "Custom Analysis"]
        )
        
        if analysis_type == "Custom Analysis":
            custom_prompt = st.text_input("Enter your specific question about the CSV data:")
            prompt = custom_prompt if custom_prompt else "Analyze this financial CSV data"
        else:
            prompts = {
                "Financial Summary": "Provide a comprehensive financial summary and insights from this CSV data",
                "Expense Analysis": "Analyze the expenses and spending patterns in this CSV data", 
                "Revenue Analysis": "Analyze the revenue and income patterns in this CSV data",
                "Budget Analysis": "Analyze the budget information and financial planning from this CSV data",
                "Trend Analysis": "Identify trends and patterns in this financial CSV data"
            }
            prompt = prompts[analysis_type]
        
        if st.button("Analyze CSV Data"):
            with st.spinner("AI is analyzing your financial CSV data..."):
                try:
                    model = genai.GenerativeModel("gemini-1.5-flash")
                    response = model.generate_content(
                        f"{prompt}:\n\n{document_text}"
                    )
                    
                    st.subheader(f"AI {analysis_type}")
                    if response.text:
                        st.write(response.text)
                    else:
                        st.error("No response generated from AI")
                        
                except Exception as e:
                    st.error(f"Error during AI analysis: {e}")
    else:
        st.error(f"Error processing CSV file: {document_text}")