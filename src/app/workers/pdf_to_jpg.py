from pdf2image import convert_from_path

def convert_pdf_to_jpg(path_to_pdf: str, filename: str) -> str:
    pages = convert_from_path(f'{path_to_pdf}', 500)
    for count, page in enumerate(pages):
        page.save(f'{filename}.jpg', 'JPEG')