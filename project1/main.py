from wsgiref import types
import streamlit as st
from dotenv import load_dotenv
import PyPDF2
import os
import io
from google import generativeai as genai

load_dotenv()



st.title("AI Resume Roaster")
st.divider()
st.badge("By Parikshit")
st.markdown("Upload your resume and get AI-powered roasting!")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

uploaded_file = st.file_uploader("Upload your resume", type=["pdf", "txt"])

job_role = st.text_input("Enter the job role you are applying for", placeholder="e.g., Software Engineer")

analyze_button = st.button("Analyze Resume")

def extract_text_from_pdf(file_bytes):
    reader = PyPDF2.PdfReader(io.BytesIO(file_bytes))
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_text_from_txt(file_bytes):
    return file_bytes.decode("utf-8")

def extract_text(file):
    file_type = file.type
    if file_type == "application/pdf":
        return extract_text_from_pdf(file.read())
    elif file_type == "text/plain":
        return extract_text_from_txt(file.read())
    else:
        text = ""
    return text
    
if analyze_button and uploaded_file:
    try:
        resume_text = extract_text(uploaded_file)
        if not resume_text:
            st.error("Could not extract text from the uploaded file.")
        else:
            st.subheader("Resume Text")
            st.text_area("Extracted Text", value=resume_text, height=300)

            if job_role:
                st.subheader("AI Roast")
                
                with st.spinner("AI is analyzing your resume... Please wait!"):
                    model = genai.GenerativeModel("gemini-1.5-flash")
                    response = model.generate_content(
                        f"Roast this resume for the job role of {job_role}:\n\n{resume_text}"
                    )
                
                st.write("AI Response:")
                if response.text:
                    st.write(response.text)
                else:
                    st.write("No response generated.")
            else:
                st.warning("Please enter a job role to get the AI roast.")
    except Exception as e:
        st.error(f"An error occurred while processing the file: {e}")
