# Python AI Projects Collection 🐍🤖

A comprehensive collection of AI-powered Python applications built with modern frameworks and Google's Gemini AI. This repository showcases various practical applications of artificial intelligence in different domains.

## 🚀 Projects Overview

### 1. [AI Resume Roaster](./project1/) 🔥
**Fun and insightful resume analysis tool**
- **Description**: An AI-powered application that provides honest, humorous feedback on resumes for specific job roles
- **Tech Stack**: Streamlit, Google Gemini AI, PyPDF2, python-dotenv
- **Features**:
  - PDF and TXT resume processing
  - Job-specific feedback
  - AI-powered roasting and constructive criticism
  - Clean web interface

### 2. [AI Financial Data Analyser](./Financial_Dtata_Analyser/) 📊
**Intelligent financial data insights**
- **Description**: A powerful tool for analyzing financial CSV data with AI-generated insights and recommendations
- **Tech Stack**: Streamlit, Google Gemini AI, Pandas, python-dotenv
- **Features**:
  - CSV data processing and visualization
  - Multiple analysis types (Expense, Revenue, Budget, Trends)
  - Interactive data tables
  - Custom analysis queries

## 🛠️ Tech Stack

### Core Technologies
- **Python 3.7+** - Main programming language
- **Streamlit** - Web application framework
- **Google Gemini AI** - Advanced AI analysis
- **Pandas** - Data manipulation and analysis
- **PyPDF2** - PDF text extraction
- **python-dotenv** - Environment variable management

### AI Integration
- **Google Generative AI (Gemini 1.5 Flash)** - Natural language processing and analysis
- **Custom prompting** - Tailored AI responses for specific use cases

## 🔧 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- Google Gemini API Key

### Global Setup
1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Python
   ```

2. **Install common dependencies**:
   ```bash
   pip install streamlit python-dotenv google-generativeai pandas PyPDF2 python-docx
   ```

3. **Set up environment variables**:
   Create a `.env` file in each project directory:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

### Getting Your Gemini API Key
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the key to your `.env` files

## 🏃‍♂️ Quick Start

### Running Any Project
```bash
# Navigate to the project directory
cd project_name

# Run the Streamlit application
streamlit run main.py
```

### Development Mode (Auto-reload)
```bash
# For live development with auto-refresh
streamlit run main.py --server.runOnSave true
```

## 📁 Repository Structure

```
Python/
├── project1/                 # AI Resume Roaster
│   ├── main.py              # Main application
│   ├── README.md            # Project-specific docs
│   ├── pyproject.toml       # Project configuration
│   └── uv.lock             # Dependencies
├── Financial_Dtata_Analyser/ # AI Financial Analyser
│   ├── main.py              # Main application
│   └── README.md            # Project-specific docs
├── README.md                # This universal README
└── .env                     # Global environment variables
```

## 🎯 Features Across Projects

### Common Features
- **AI-Powered Analysis** - Intelligent insights using Google Gemini
- **File Processing** - Support for multiple file formats
- **Interactive UI** - Clean, user-friendly interfaces
- **Real-time Processing** - Loading indicators and progress feedback
- **Error Handling** - Comprehensive error management
- **Responsive Design** - Works on desktop and mobile

### Unique Capabilities
- **Resume Analysis** - Job-specific feedback and roasting
- **Financial Insights** - Multi-dimensional financial data analysis
- **Data Visualization** - Interactive tables and previews
- **Custom Queries** - User-defined analysis prompts

## 🧪 Development

### Code Standards
- Clean, readable Python code
- Modular function design
- Comprehensive error handling
- User-friendly interfaces

### Testing Projects
Each project can be tested individually by:
1. Navigating to the project directory
2. Running `streamlit run main.py`
3. Uploading sample files
4. Testing different analysis options

## 📚 Documentation

Each project contains its own detailed README with:
- Project-specific installation instructions
- Usage examples
- Feature descriptions
- Code explanations

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Parikshit**
- AI Resume Roaster
- AI Financial Data Analyser

## 🔮 Future Projects

This repository will continue to grow with more AI-powered Python applications:
- Document Summarizer
- Image Analysis Tools
- Chatbot Applications
- Data Visualization Dashboards

## 🆘 Support

If you encounter any issues:
1. Check the project-specific README files
2. Ensure your Gemini API key is properly configured
3. Verify all dependencies are installed
4. Create an issue in the repository

---

**Transform your data into intelligent insights with the power of AI! 🚀**
