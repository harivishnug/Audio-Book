#Made by Hari Vishnu
#Only for Educational purpose

import pyttsx3
import PyPDF2
speaker = pyttsx3.init()
book = open('oops.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
for num in range(7, pages):
    page = pdfReader.getPage(7)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
