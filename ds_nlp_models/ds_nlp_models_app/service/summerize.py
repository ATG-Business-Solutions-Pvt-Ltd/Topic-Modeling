pip install PyPDF2
pip install fpdf
pip install mglearn
pip install pyLDAvis
pip install fastapi kaleido
pip install python-multipart
pip install uvicorn
pip install panda
pip install numpy
pip install streamlit

from google.colab import drive
drive.mount('/content/drive')
import os
import PyPDF2
import fpdf
import streamlit as st
import re

# Directory for storing PDF files
pdf_directory = '/content/pdf_files'

# Directory for storing extracted text from PDFs
text_directory = '/content/extracted_text'

# Create directories if they don't exist
os.makedirs(text_directory, exist_ok=True)

pdf = fpdf.FPDF(format='letter')
pdf.add_font('Arial', '', '/content/arial.ttf', uni=True) #path of the font file is set to avoid the error generated by U+2019=','
pdf.set_font("Arial", size=12)
pdf.add_page()

def save_uploadedfile(uploadedfile):
    with open(os.path.join(pdf_directory, uploadedfile.name),'wb') as f:
        f.write(uploadedfile.getbuffer())
        return st.success("Saved File: to pdf_directory".format(uploadedfile.name))

st.title("PDF File upload")
st.text("A simple way to upload files directly into a directory")
uploadedfiles = st.file_uploader("Upload PDF", type=['pdf'], accept_multiple_files=True)
for file in uploadedfiles:
    if uploadedfiles is not None:
        save_uploadedfile(file)
    for file_name in os.listdir(pdf_directory):
        if file_name.endswith('.pdf'):
            # Open the PDF file
            with open(os.path.join(pdf_directory, file_name), 'rb') as file:
                # Create a PDF reader object
                reader = PyPDF2.PdfReader(file)

                # Extract text from each page
                text = ''
                for page in reader.pages:
                    text += page.extract_text()

                # Save the extracted text as a text file
                text_file_name = file_name.replace('.pdf', '.txt')
                text_file_path = os.path.join(text_directory, text_file_name)
                with open(text_file_path, 'w') as text_file:
                    text_file.write(text)
    with open('/content/extracted_text/sample-statement-of-work.txt') as f:
    clean_cont = f.read().splitlines()