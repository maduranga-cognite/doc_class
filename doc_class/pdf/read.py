

def read_pdf(file_name):
	import PyPDF2
	import textract
	import tabula
	from nltk.tokenize import word_tokenize
	from nltk.corpus import stopwords
	pdfFileObj = open('PDF_in\\'+ file_name +'.pdf','rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	#print('pages:'+str(pdfReader.numPages))
	pageObj = pdfReader.getPage(0)
	return pageObj.extractText()

	#text = textract.process('PDF_in/'+ file_name +'.pdf')


