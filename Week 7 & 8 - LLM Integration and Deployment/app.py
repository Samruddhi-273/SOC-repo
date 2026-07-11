import streamlit as st
from PIL import Image

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Industrial Quality Assurance",
    page_icon="🔍",
    layout="wide"
)

# --------------------------------------------------
# Title
# --------------------------------------------------
st.title("🔍 Multimodal AI System for Industrial Quality Assurance")
st.markdown("### YOLOv8 + Llama 3.2 + Streamlit")

st.write("---")

# --------------------------------------------------
# File Upload
# --------------------------------------------------
uploaded_file = st.file_uploader(
    "📤 Upload a Steel Surface Image",
    type=["jpg", "jpeg", "png"]
)

st.write("---")

# --------------------------------------------------
# Display Uploaded Image
# --------------------------------------------------
if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.subheader("🖼️ Uploaded Image")
    st.image(image, caption="Uploaded Steel Surface Image", use_container_width=True)

else:
    st.info("Please upload a steel surface image to begin inspection.")

st.write("---")

# --------------------------------------------------
# Detection Results Section
# --------------------------------------------------
st.subheader("📌 Detection Results")

st.info("No inspection performed yet. YOLOv8 results will appear here.")

st.write("---")

# --------------------------------------------------
# Inspection Report Section
# --------------------------------------------------
st.subheader("📄 AI Inspection Report")

st.info("The AI-generated inspection report will appear here after running the inspection.")