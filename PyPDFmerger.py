import PyPDF2

def merge_pdfs(output_file, input_files):
    pdf_writer = PyPDF2.PdfWriter()
    for input_file in input_files:
        pdf_reader = PyPDF2.PdfReader(input_file)
        for page in range(pdf_reader.numPages):
            pdf_writer.add_page(pdf_reader.get_page(page))
    with open(output_file, 'wb') as out:
        pdf_writer.write(out)
outputpdf = ''
inputone = ''
inputtwo = ''
# Example usage: merge input1.pdf and input2.pdf and save the result to output.pdf
merge_pdfs(outputpdf, [inputone, inputtwo])