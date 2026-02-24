import pypdf as pdf

mergr = pdf.PdfMerger()
list_pdfs = ['k_adhar.pdf','pan_card.pdf']

for file in list_pdfs:
	mergr.append(file)

mergr.print("pdf merged")