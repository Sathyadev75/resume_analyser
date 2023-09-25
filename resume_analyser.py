import streamlit as st

import subprocess

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

import spacy
import re

# Load a spaCy model for English
nlp = spacy.load("en_core_web_sm")

# Replace 'resume.pdf' with the path to your PDF file
file_name = 'resume.pdf'
import pdfplumber

def extract_text_from_pdf(pdf_file_path):
    try:
        with pdfplumber.open(pdf_file_path) as pdf:
             text = ""
             for page in pdf.pages:
                   text += page.extract_text()
    except Exception as e:
        print(f"Error extracting text from PDF: {str(e)}")
    
    return text

# Extract text from the PDF
resume_text = extract_text_from_pdf(file_name)

# Process the extracted text with spaCy
doc = nlp(resume_text)

# Extract various details from the resume
email_addresses = [token.text for token in doc if token.like_email]
phone_numbers = [re.sub(r'\D', '', token.text) for token in doc if token.like_phone]
names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
addresses = [ent.text for ent in doc.ents if ent.label_ == "GPE" or ent.label_ == "LOC"]
education = [chunk.text for chunk in doc.noun_chunks if "education" in chunk.text.lower()]
experience = [chunk.text for chunk in doc.noun_chunks if "experience" in chunk.text.lower()]
skills = []

# Extracting skills (example: searching for specific keywords)
skill_keywords = ["python", "java", "machine learning", "data analysis"]
for token in doc:
    for keyword in skill_keywords:
        if keyword in token.text.lower() and token.is_alpha:
            skills.append(token.text)

# Print the extracted details
print("Extracted Email Addresses:")
print(email_addresses)

print("\nExtracted Phone Numbers:")
print(phone_numbers)

print("\nExtracted Names:")
print(names)

print("\nExtracted Addresses:")
print(addresses)

print("\nEducation:")
print(education)

print("\nExperience:")
print(experience)

print("\nSkills:")
print(skills)
