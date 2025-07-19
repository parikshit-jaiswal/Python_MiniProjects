# AI Resume Roaster 🔥

A fun and insightful Streamlit web application that uses Google's Gemini AI to analyze and "roast" your resume for specific job roles. Get honest feedback about your resume's strengths and weaknesses!

## Features

- 📄 **Multi-format Support**: Upload resumes in PDF or TXT format
- 🤖 **AI-Powered Analysis**: Uses Google Gemini 1.5 Flash for intelligent resume evaluation
- 🎯 **Job-Specific Feedback**: Tailored roasting based on the job role you're applying for
- 📝 **Text Extraction**: Automatically extracts and displays text from uploaded files
- ⏳ **Loading Indicators**: Real-time feedback while AI processes your resume
- 🎨 **Clean Interface**: User-friendly Streamlit interface

## Prerequisites

- Python 3.7+
- Google Gemini API Key

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd project1
   ```

2. **Install dependencies**:
   ```bash
   pip install streamlit python-dotenv PyPDF2 google-generativeai
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root and add your Gemini API key:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

## Getting Your Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the key and add it to your `.env` file

## Usage

1. **Run the application**:
   ```bash
   streamlit run main.py
   ```

2. **Upload your resume**:
   - Click "Browse files" and select your resume (PDF or TXT format)
   - The app will automatically extract and display the text

3. **Enter job role**:
   - Type the job role you're applying for (e.g., "Software Engineer", "Data Scientist")

4. **Get your roast**:
   - Click "Analyze Resume" and wait for the AI to process
   - Read the honest feedback about your resume!

## File Structure

```
project1/
├── main.py           # Main Streamlit application
├── README.md         # This file
├── pyproject.toml    # Project configuration
├── uv.lock          # Dependency lock file
└── .env             # Environment variables (create this)
```

## Code Overview

- **Text Extraction**: Handles both PDF and TXT file formats using PyPDF2
- **AI Integration**: Uses Google Generative AI (Gemini) for resume analysis
- **Error Handling**: Comprehensive error handling for file processing and API calls
- **User Experience**: Loading spinners and clear feedback messages

## Supported File Formats

- **PDF**: Automatically extracts text using PyPDF2
- **TXT**: Direct text file reading

## Contributing

Feel free to fork this project and submit pull requests for improvements!

## License

This project is open source and available under the MIT License.

## Author

**Parikshit** - AI Resume Roaster

---

*Disclaimer: This is a fun project for educational purposes. The AI responses are generated automatically and should be taken with humor and constructive criticism in mind.*
