import PyPDF2
import os
filenam=os.getcwd()+"\\cv_2.pdf"
print(filenam)
tobecalle="test.txt"
def fileread(filename,tobecalled): #the path?

    pdfobj = open(filename,'rb') #rb for read binary mode
    reader = PyPDF2.PdfFileReader(pdfobj)
    os.getcwd()
    textfile = "";

    for i in range(reader.numPages):
        textfile= textfile+ " "+ reader.getPage(i).extractText()
    target = open(tobecalled,'w')
    target.truncate()
    target.write(textfile)

fileread(filenam,tobecalle)
