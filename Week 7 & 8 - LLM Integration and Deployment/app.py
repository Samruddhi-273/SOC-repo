import streamlit as st
from PIL import Image
import pandas as pd
import os

from utils.llm import generate_report
from utils.detector import detect_defects

st.set_page_config(
    page_title="Industrial QA",
    page_icon="🔍",
    layout="wide"
)

# ---------------- Sidebar ---------------- #

with st.sidebar:

    st.title("🏭 Industrial QA")

    st.markdown("---")

    st.subheader("Project Overview")

    st.write(
        "An AI-powered system for automated steel surface defect detection "
        "and inspection report generation."
    )

    st.markdown("---")

    st.subheader("Technology Stack")

    st.markdown("""
- YOLOv8 (Defect Detection)
- Ollama
- Llama 3.2 (Inspection Report)
- Streamlit (Web Application)
""")

    st.markdown("---")

    st.subheader("Workflow")

    st.markdown("""
1. Upload Image
2. Detect Defects
3. Generate AI Report
4. Download Report
""")

    st.markdown("---")

    st.subheader("Developer")

    st.write("Samruddhi Magadum")

# ---------------- Main Page ---------------- #

st.title("🔍 Multimodal AI System for Industrial Quality Assurance")


st.write("---")

inspection_date = st.date_input("📅 Inspection Date")

uploaded_file = st.file_uploader(
    "Upload Steel Surface Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    # Save uploaded image
    image_path = os.path.join("uploads", uploaded_file.name)

    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    col1, col2 = st.columns(2)

    # ---------------- Original Image ---------------- #

    with col1:
        st.subheader("Original Image")
        st.image(image_path, use_container_width=True)

    # ---------------- Run Inspection ---------------- #

    if st.button("Run Inspection"):

        with st.spinner("Running YOLOv8 Detection..."):

            annotated_image, detections = detect_defects(image_path)

        # ---------------- Calculate Metrics ---------------- #

        total_defects = len(detections)

        if total_defects > 0:
            confidences = [d["confidence"] for d in detections]
            highest_confidence = max(confidences)
            average_confidence = sum(confidences) / total_defects
        else:
            highest_confidence = 0
            average_confidence = 0

        # ---------------- Detected Image ---------------- #

        with col2:
            st.subheader("Detected Image")
            st.image(annotated_image, use_container_width=True)

        # ---------------- Summary Dashboard ---------------- #

        st.write("---")

        st.subheader("📊 Inspection Summary")

        c1, c2, c3 = st.columns(3)

        c1.metric("Total Defects", total_defects)
        c2.metric("Highest Confidence", f"{highest_confidence:.2f}%")
        c3.metric("Average Confidence", f"{average_confidence:.2f}%")

        # ---------------- Overall Status ---------------- #

        if highest_confidence >= 80:
            st.error("🔴 Overall Status: Rework Required")

        elif highest_confidence >= 50:
            st.warning("🟡 Overall Status: Inspection Required")

        else:
            st.success("🟢 Overall Status: Accepted")

        # ---------------- Defect Table ---------------- #

        st.write("---")

        st.subheader("Detected Defects")

        if len(detections) == 0:

            st.success("✅ No defects detected.")

        else:

            table = []

            for d in detections:

                if d["confidence"] >= 80:
                    severity = "High"

                elif d["confidence"] >= 50:
                    severity = "Medium"

                else:
                    severity = "Low"

                table.append({

                    "Defect": d["defect"],

                    "Confidence (%)": f'{d["confidence"]:.2f}',

                    "Severity": severity

                })

            df = pd.DataFrame(table)

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )

        # ---------------- AI Inspection Report ---------------- #

        st.write("---")

        st.subheader("📋 Inspection Report")

        with st.spinner("Generating AI Inspection Report..."):

            report = generate_report(detections, inspection_date)

        

        st.markdown(report)

        # ---------------- Download Button ---------------- #

        st.download_button(
            label="📄 Download Inspection Report",
            data=report,
            file_name="Inspection_Report.txt",
            mime="text/plain"
        )