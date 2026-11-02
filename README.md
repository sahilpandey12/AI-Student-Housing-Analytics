# 🏠 AI-Powered Student Housing Booking Analytics

An interactive business intelligence dashboard that analyses student accommodation booking data using Python, SQL, Streamlit and Google Gemini AI.

## 📌 Project Overview

This project demonstrates how data analytics and generative AI can help a student housing platform understand booking patterns, marketing performance, customer preferences and business opportunities.

The project uses a synthetic dataset of 1,000 booking records.

## 🎯 Business Objectives

* Analyse booking performance across different cities.
* Identify effective marketing channels.
* Understand accommodation preferences.
* Track monthly booking trends.
* Generate actionable business recommendations using Gemini AI.

## 🛠️ Technologies Used

| Technology        | Purpose                           |
| ----------------- | --------------------------------- |
| Python            | Data processing and analysis      |
| Pandas            | Data manipulation                 |
| SQL               | Business queries and aggregations |
| SQLite            | Database management               |
| Streamlit         | Interactive dashboard             |
| Plotly            | Data visualisation                |
| Google Gemini API | AI-generated business insights    |

## 📊 Dashboard Features

* Business KPI cards
* City-wise booking analysis
* Marketing channel performance
* Property type analysis
* Monthly booking trends
* Interactive city filters
* AI-powered business analysis

## 🤖 AI Integration

Google Gemini AI analyses verified business metrics and generates:

* Business performance summaries
* Important business insights
* Marketing channel comparisons
* Business opportunities
* Actionable recommendations

AI-generated findings are checked against the underlying dataset to avoid unsupported conclusions.

## 📁 Project Structure

```text
AI-Student-Housing-Analytics/
│
├── app.py
├── analysis.py
├── ai_insights.py
├── generate_data.py
├── test_ai.py
├── bookings.csv
├── sql/
│   └── queries.sql
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/sahilpandey12/AI-Student-Housing-Analytics.git
```

### 2. Open the project folder

```bash
cd AI-Student-Housing-Analytics
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment (Windows)

```powershell
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install pandas streamlit plotly google-genai python-dotenv
```

### 6. Configure Gemini API

Create a `.env` file in the project directory:

```text
GEMINI_API_KEY=your_api_key_here
```

Never upload your API key to GitHub.

### 7. Launch the dashboard

```bash
streamlit run app.py
```

## 📈 Data Analysis

The project explores:

* City-wise confirmed bookings
* Marketing channel booking rates
* Average monthly rent
* Accommodation type preferences
* Monthly booking patterns

Marketing booking rates are calculated using booking records as the denominator and should be interpreted as a record-to-booking rate proxy, not a verified unique-lead conversion rate.

## ⚠️ Data Disclaimer

This project uses synthetic data generated for educational and portfolio purposes.

It does not contain actual Amber customer, booking or financial data. Business insights are illustrative and should not be interpreted as actual company performance.

## 👨‍💻 Author

Developed as a data analytics portfolio project to demonstrate practical skills in Python, SQL, data visualisation and AI-assisted business analysis.
