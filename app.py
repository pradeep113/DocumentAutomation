import streamlit as st
from backend import generate_document, extract_preview

st.set_page_config(page_title="Document Automation", layout="wide")

# Sidebar navigation
st.sidebar.title("📁 Document Modules")
module = st.sidebar.radio("Select Module", ["UDD", "ISF", "IP", "IQ", "OQ", "Upload to Veeva"])

st.title("📄 Document Automation Tool")

if module == "UDD":
    st.subheader("📌 UDD – User Design Document")

    uploaded_template = st.file_uploader("Upload Word Template (.docx)", type=["docx"])

    # UDD-specific inputs
    interface_id = st.text_input("Interface ID")
    source_4c = st.text_input("Source 4C Code")
    target_4c = st.text_input("Target 4C Code")
    flow_details = st.text_area("Flow Details")
    source_server = st.text_input("Source Server")
    source_port = st.text_input("Source Port")
    source_userid = st.text_input("Source User ID")
    source_path = st.text_input("Source Path")
    target_server = st.text_input("Target Server")
    target_port = st.text_input("Target Port")
    target_userid = st.text_input("Target User ID")
    target_path = st.text_input("Target Path")
    frequency = st.text_input("File Frequency")
    file_size = st.text_input("File Size")
    mode = st.selectbox("Transfer Mode", ["SFTP", "FTP", "API", "Other"])

    data = {
        "InterfaceID": interface_id,
        "Source4C": source_4c,
        "Target4C": target_4c,
        "FlowDetails": flow_details,
        "SourceServer": source_server,
        "SourcePort": source_port,
        "SourceUserID": source_userid,
        "SourcePath": source_path,
        "TargetServer": target_server,
        "TargetPort": target_port,
        "TargetUserID": target_userid,
        "TargetPath": target_path,
        "Frequency": frequency,
        "FileSize": file_size,
        "Mode": mode
    }

    if uploaded_template:
        col1, col2 = st.columns(2)

        with col1:
            if st.button("🔍 Preview Document Content"):
                preview_text = extract_preview(data, uploaded_template)
                st.subheader("📑 Document Preview")
                st.text_area("Preview", preview_text, height=400)

        with col2:
            if st.button("📥 Export Final Document"):
                docx_file = generate_document(data, uploaded_template)
                st.download_button("Download Word Document", docx_file, file_name="UDD_InterfaceDetails.docx")

else:
    st.info(f"🚧 The '{module}' module is under construction. Stay tuned!")

