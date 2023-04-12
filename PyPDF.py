import PyPDF2

def remove_pages_from_pdf(input_file, output_file, pages_to_remove):
    with open(input_file, 'rb') as infile:
        reader = PyPDF2.PdfReader(infile)
        writer = PyPDF2.PdfWriter()
        for pagenum in range(len(reader.pages)):
            if pagenum not in pages_to_remove:
                page = reader.pages[pagenum]
                writer.add_page(page)
        with open(output_file, 'wb') as outfile:
            writer.write(outfile)
inputpdf = 'E:/NAME.pdf'
outputpdf = 'C:/OTHERNAME.pdf'
# Example usage: remove the first and third pages from input.pdf and save the result to output.pdf
#remove_pages_from_pdf('input.pdf', 'output.pdf', [0, 1])
remove_pages_from_pdf(inputpdf, outputpdf, [0, 1])

