import streamlit as st

# Create a Streamlit app
st.title("PDF Uploader and Saver")

# Upload a PDF file
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    # Display the uploaded file
    st.write("Uploaded PDF file:", uploaded_file.name)

    # Save the uploaded file to your PC
    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.read())
    
    st.success(f"File '{uploaded_file.name}' saved successfully by prakash!")
    
st.title("Smart Resume Analyser")
st.sidebar.markdown("# Choose User")
activities = ["Normal User", "Admin"]
choice = st.sidebar.selectbox("Choose among the given options:", activities)
