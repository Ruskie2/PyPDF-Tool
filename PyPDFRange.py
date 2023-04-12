import PyPDF2

def remove_range_of_pages_from_pdf(input_file, output_file, start_page, end_page):
    with open(input_file, 'rb') as infile:
        reader = PyPDF2.PdfReader(infile)
        writer = PyPDF2.PdfWriter()
        for pagenum in range(len(reader.pages)):
            if pagenum < start_page or pagenum > end_page:
                page = reader.pages[pagenum]
                writer.add_page(page)
        with open(output_file, 'wb') as outfile:
            writer.write(outfile)
inputpdf = ''
outputpdf = ''
# Example usage: remove pages 2-4 from input.pdf and save the result to output.pdf
remove_range_of_pages_from_pdf(inputpdf, outputpdf, 1, 3)
