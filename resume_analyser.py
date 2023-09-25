import streamlit as st

!pip install PYMuPDF

import fitz  # PyMuPDF

st.title("Smart Resume Analyser")
st.sidebar.markdown("# Choose User")
activities = ["Normal User", "Admin"]
choice = st.sidebar.selectbox("Choose among the given options:", activities)

# Upload a PDF file
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    # Display the uploaded PDF file name
    st.write("Uploaded PDF file:", uploaded_file.name)

    # Save the uploaded file to your PC
    file_name = f"uploaded_resume.pdf"  # Choose a suitable name
    with open(file_name, "wb") as f:
        f.write(uploaded_file.read())

    st.success(f"File '{file_name}' saved successfully!")

    # Use PyMuPDF to convert PDF pages to images
    pdf_document = fitz.open(file_name)
    pdf_images = []
    for page_number in range(pdf_document.page_count):
        page = pdf_document.load_page(page_number)
        pdf_image = page.get_pixmap()
        pdf_images.append(pdf_image)

    # Display PDF pages as images
    for page_number, pdf_image in enumerate(pdf_images):
        st.image(pdf_image, caption=f"Page {page_number + 1}", use_column_width=True)
