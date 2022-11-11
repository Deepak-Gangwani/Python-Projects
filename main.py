import pyttsx3
import PyPDF2

file = input("Enter the pdf file name-->")
start_page = int(input("Enter the start page of pdf file--> "))
end_page = int(input("Enter the end page of pdf file-->"))
book = open(f"{file}.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(f"The number of file pages-->{pages}")
speaker = pyttsx3.init()

for num in range(start_page,end_page):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    num = num+1
    speaker.runAndWait()