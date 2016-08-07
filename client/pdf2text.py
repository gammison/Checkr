import PyPDF2
import os

to_be_called = "name here.txt"
# the path?


def file_read(filename, tbc):
    # rb for read binary mode
    pdf_obj = open(filename, 'rb')
    reader = PyPDF2.PdfFileReader(pdf_obj)
    os.getcwd()
    text_file = ""

    for i in range(reader.numPages):
        text_file = text_file + " " + reader.getPage(i).extractText()
    target = open(tbc, 'w')
    target.truncate()
    target.write(text_file)

file_read('G:\\Books\\AlbertCamusThePlague.pdf','test.txt')