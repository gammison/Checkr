import docx

doc = docx.Document('path here')
paragraph_length = len(doc.paragraphs)
text_file = open('test.txt', 'w')
for para in doc.paragraphs:
    text_file.write(para.text)

