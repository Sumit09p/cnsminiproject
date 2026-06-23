# 📧 EmConfig

A Flask-based web application that analyzes email content and extracts useful insights such as sender information, IP details, and email metadata.

## 🚀 Features

- Parse raw email headers
- Extract sender information
- IP address extraction
- IP enrichment and analysis
- Clean and user-friendly web interface
- Real-time email inspection
- HTML report generation

## 🛠️ Tech Stack

- Python
- Flask
- HTML5
- CSS3
- Jinja2 Templates

## 📂 Project Structure

```
emailproject/
│
├── app.py
├── parser.py
├── analyzer.py
├── ip_enrich.py
│
├── static/
│   └── style.css
│
├── templates/
│   ├── base.html
│   ├── index.html
│   └── result.html
│
└── requirements.txt
```

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Sumit09p/cnsminiproject.git
cd cnsminiproject
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Application will start at:

```text
http://localhost:5000
```

## 📖 How It Works

1. User enters email data or headers.
2. Application parses email metadata.
3. Sender and routing information are extracted.
4. IP addresses are identified.
5. IP enrichment module analyzes extracted IPs.
6. Results are displayed through a clean dashboard.

## 🎯 Use Cases

- Email Forensics
- Cyber Security Analysis
- Phishing Investigation
- Header Inspection
- Network Security Learning

## 🔒 Educational Purpose

This project was developed as part of a Computer Networks and Security (CNS) mini project to understand email analysis and network tracing techniques.

## 👨‍💻 Author

**Sumit Pandey**

GitHub: https://github.com/Sumit09p

---
⭐ If you found this project useful, consider giving it a star.
