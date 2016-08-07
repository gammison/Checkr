import docx
import PyPDF2
import os


class ToTex():

    def __init__(self, path):
        self.path = path

    def doc_to_text(self):
        doc = docx.Document(self.path)
        tbc = self.path
        tbc = tbc[self.path.rfind('/'):self.path.rfind('.')]
        text_file = open('text/'+tbc+'txt', 'w')
        for para in doc.paragraphs:
            text_file.write(para.text + '\n')

    def file_read(self):
        tbc = self.path
        tbc = tbc[self.path.rfind('/'):self.path.rfind('.')]

        # rb for read binary mode
        pdf_obj = open(self.path, 'rb')
        reader = PyPDF2.PdfFileReader(pdf_obj)
        os.getcwd()
        text_file = ""

        for i in range(reader.numPages):
            text_file = text_file + " " + reader.getPage(i).extractText()
        target = open('text/'+tbc+'.txt', 'w')
        target.truncate()
        target.write(text_file)
