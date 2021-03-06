import PyPDF2

with open('dummy.pdf', 'rb') as file:
 reader = PyPDF2.PdfFileReader(file) #PyPDF have method .pdfreader to read pdf but it can only read binary
 page = reader.getPage(0)  #Pypdf needs to know which pdf page to rotate
 page.rotateCounterClockwise(180)
 writer = PyPDF2.PdfFileWriter()
 writer.addPage(page)
 with open('changed.pdf', 'wb') as newfile:
     writer.write(newfile)
     
