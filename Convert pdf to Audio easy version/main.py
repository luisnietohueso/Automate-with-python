'''
Project Description: In this project, we will create an audio file based on a PDF using the following Python libraries: pyttsx3 and PyPDF2. To install a library, you should use the command "pip install library_name".

Author of this code: Luis Nieto Hueso

References used: geeksforgeeks
'''
# Importing the modules
import PyPDF2
import pyttsx3

# Path to the PDF file
path = open('example.pdf', 'rb')

# Creating a PdfReader object
pdfReader = PyPDF2.PdfReader(path)

# The page from which you want to start
# This will read page 1 of the PDF.
page = pdfReader.pages[0]

# Extracting the text from the PDF
text = page.extract_text()

# Reading the text
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()