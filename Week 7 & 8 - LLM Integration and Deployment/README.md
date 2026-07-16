#  AI-Powered Industrial Quality Assurance System
### Week 7 & 8 – LLM Integration and Deployment

##  Project Overview

This project integrates Computer Vision and Large Language Models (LLMs) to build an AI-powered Industrial Quality Assurance System. The application detects defects on steel surface images using a trained YOLOv8 model and generates professional inspection reports using the Llama 3.2 model running locally through Ollama.

The entire system is deployed as an interactive Streamlit web application, providing an end-to-end quality inspection workflow.

---

##  Objectives

- Build an interactive Streamlit web application.
- Integrate a custom-trained YOLOv8 model for steel surface defect detection.
- Use Ollama to run the Llama 3.2 Large Language Model locally.
- Automatically generate professional AI inspection reports.
- Deploy a complete Multimodal AI application.

---

##  Features

-  Upload steel surface images.
-  Detect defects using the trained YOLOv8 model.
-  Display detected defects with bounding boxes.
-  Show inspection summary including:
  - Total Defects
  - Highest Confidence
  - Average Confidence
  - Overall Inspection Status
-  Display detected defects in a structured table.
-  Generate AI-powered inspection reports using Llama 3.2.
-  Download the inspection report.

---

##  Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | Web Application |
| YOLOv8 | Steel Surface Defect Detection |
| Ollama | Local LLM Runtime |
| Llama 3.2 | AI Inspection Report Generation |
| Pandas | Data Processing |
| Pillow | Image Handling |

---

## Project Structure

```
Week 7 & 8 - LLM Integration and Deployment/
│
├── app.py
├── requirements.txt
├── README.md
│
├── model/
│   └── best.pt
│
├── uploads/
│
├── outputs/
│
└── utils/
    ├── detector.py
    └── llm.py
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/Samruddhi-273/SOC-repo/tree/master
cd "Week 7 & 8 - LLM Integration and Deployment"
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download and install Ollama from:

https://ollama.com/

Pull the Llama 3.2 model:

```bash
ollama pull llama3.2
```

Verify installation:

```bash
ollama list
```

---

## Running the Application

Navigate to the project folder.

Run:

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

##  Workflow

1. Upload a steel surface image.
2. YOLOv8 detects surface defects.
3. Detected image with bounding boxes is displayed.
4. Inspection summary is generated.
5. Detected defects are shown in a table.
6. Llama 3.2 generates a professional inspection report.
7. Download the inspection report.

---

##  Sample Inspection Report

```
Inspection Report

Inspection Date: 09 July 2026

Detected Defects:
• Scratch (96%)
• Pitted Surface (91%)

Summary:
Two surface defects were detected on the steel sheet. The defects may affect the surface quality and should be inspected before further processing.

Severity:
Medium

Recommended Action:
• Inspect the affected region manually.
• Remove or repair the damaged section if required.
• Monitor the production line for recurring defects.
• Perform quality verification before shipment.
```

---

##  Sample Output

Add screenshots here after running the application.

Suggested screenshots:

- Home Screen
- Uploaded Image
- Detected Image
- Inspection Summary
- AI Inspection Report

---

##  Learning Outcomes

Through this project, I learned:

- Integrating a trained YOLOv8 model into a Streamlit application.
- Running Large Language Models locally using Ollama.
- Generating AI-powered inspection reports with Llama 3.2.
- Deploying an end-to-end Multimodal AI application.
- Building user-friendly interfaces for AI solutions.

---

##  Future Improvements

- PDF report generation.
- Support for multiple image uploads.
- Confidence visualization charts.
- Cloud deployment.
- Inspection history tracking.

---
