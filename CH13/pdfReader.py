import PyPDF2

pdfFile1 = open('meetingminutes.pdf', 'rb')
pdfFile2 = open('meetingminutes2.pdf', 'rb')
pdfReader1 = PyPDF2.PdfFileReader(pdfFile1)
pdfReader2 = PyPDF2.PdfFileReader(pdfFile2)
pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdfReader1.numPages):
    pageObj = pdfReader1.getPage(pageNum)
    pageObj.mergePage(pdfWatermarkReader.getPage(0))        #add watermark for every page
    pdfWriter.addPage(pageObj)

for pageNum in range(pdfReader2.numPages):
    pageObj = pdfReader2.getPage(pageNum)
    pdfWriter.addPage(pageObj)

pdfOutputFile = open('Automate.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdfFile1.close()
pdfFile2.close()
