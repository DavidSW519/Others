import PyPDF2
pag = 0 #La pagina donde inicia
# Abrir el archivo PDF en modo de lectura binaria
with open('ruta_archivo', 'rb') as file:
    pdf_reader = PyPDF2.PdfReader(file)
    num_pages = len(pdf_reader.pages)
    paginas = 50 #Las paignas que desplegaras
    to_pag = pag+paginas
    for page_num in range(pag,to_pag):
        page = pdf_reader.pages[page_num]
        page_content = page.extract_text().split(str(page_num+1))[0]
        print(page_content)
