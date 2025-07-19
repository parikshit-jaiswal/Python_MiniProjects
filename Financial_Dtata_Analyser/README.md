# AI Financial Data Analyser 📊💰

A powerful Streamlit web application that leverages Google's Gemini AI to analyze financial CSV data and provide intelligent insights, trends, and recommendations.

## Features

- 📈 **CSV Data Processing**: Upload and process financial CSV files with automatic data extraction
- 🤖 **AI-Powered Analysis**: Uses Google Gemini 1.5 Flash for intelligent financial analysis
- 📊 **Data Visualization**: Interactive table view with pandas DataFrame display
- 🎯 **Multiple Analysis Types**: 
  - Financial Summary
  - Expense Analysis
  - Revenue Analysis
  - Budget Analysis
  - Trend Analysis
  - Custom Analysis
- 📝 **Formatted Output**: Clean, structured data preview with column information
- ⏳ **Real-time Processing**: Loading indicators and progress feedback
- 🎨 **User-friendly Interface**: Clean Streamlit interface with intuitive navigation

## Prerequisites

- Python 3.7+
- Google Gemini API Key

## Installation

1. **Clone or download the project**:
   ```bash
   cd Financial_Data_Analyser
   ```

2. **Install required dependencies**:
   ```bash
   pip install streamlit python-dotenv google-generativeai pandas
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

## Getting Your Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the key and add it to your `.env` file

## Usage

1. **Start the application**:
   ```bash
   streamlit run main.py
   ```

2. **Upload your CSV file**:
   - Click "Browse files" and select your financial CSV file
   - The app will automatically process and display the data

3. **Choose analysis type**:
   - Select from predefined analysis types or choose "Custom Analysis"
   - For custom analysis, enter your specific question

4. **Get AI insights**:
   - Click "Analyze CSV Data" to get intelligent financial insights
   - View comprehensive analysis results

## Supported Data Formats

- **CSV Files**: Financial data in comma-separated values format
- **Data Structure**: Any CSV with financial data (expenses, revenue, budgets, etc.)

## Analysis Types

### Financial Summary
Comprehensive overview of your financial data with key insights and patterns.

### Expense Analysis
Detailed breakdown of spending patterns, categories, and recommendations for cost optimization.

### Revenue Analysis
Analysis of income streams, revenue trends, and growth opportunities.

### Budget Analysis
Budget performance review with variance analysis and planning recommendations.

### Trend Analysis
Identification of financial trends, seasonal patterns, and forecasting insights.

### Custom Analysis
Ask specific questions about your financial data for tailored insights.

## File Structure

```
Financial_Data_Analyser/
├── main.py          # Main Streamlit application
├── README.md        # This documentation
└── .env            # Environment variables (create this)
```

## Code Overview

- **CSV Processing**: Handles CSV file upload and text extraction
- **Data Display**: Shows both raw text format and pandas DataFrame
- **AI Integration**: Uses Google Generative AI for financial analysis
- **Error Handling**: Comprehensive error handling for file processing
- **User Experience**: Loading spinners and clear feedback messages

## Sample CSV Structure

Your CSV files can contain any financial data, such as:

```csv
Date,Category,Description,Amount,Type
2024-01-01,Food,Grocery Shopping,150.00,Expense
2024-01-02,Salary,Monthly Salary,5000.00,Income
2024-01-03,Transportation,Gas,60.00,Expense
```

## Dependencies

- `streamlit` - Web application framework
- `python-dotenv` - Environment variable management
- `google-generativeai` - Google Gemini AI integration
- `pandas` - Data manipulation and analysis
- `csv` - CSV file processing
- `io` - Input/output operations

## Contributing

Feel free to fork this project and submit pull requests for improvements!

## License

This project is open source and available under the MIT License.

## Author

**Parikshit** - AI Financial Data Analyser

---

*Transform your financial data into actionable insights with the power of AI! 🚀*
