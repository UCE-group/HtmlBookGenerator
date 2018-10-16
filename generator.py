import os

import pdfkit
import requests
from PyPDF2 import PdfFileWriter, PdfFileReader

from URLProvider import URLProvider

TMP_DIR = 'tmp'
OUTPUT_FILE = 'deeplearning.pdf'


def get_html(url):
    return requests.get(url).text


# fix bug of wkhtmltopdf
def html_transform(text):
    text = text.replace('right:0;', '')
    text = text.replace('right: 0;', '')
    text = text.replace('right:0', '')
    text = text.replace('right: 0', '')

    text = text.replace('bottom:0;', '')
    text = text.replace('bottom: 0;', '')
    text = text.replace('bottom:0', '')
    text = text.replace('bottom: 0', '')
    return text


def main():
    provider = URLProvider()
    pdf_write = PdfFileWriter()
    for url in provider.next():
        html = get_html(url)
        html = html_transform(html)
        print('generate html {}'.format(url))
        pdf_name = os.path.join(TMP_DIR, url.split('/')[-1] + '.pdf')
        pdfkit.from_string(html, pdf_name)
        pdf_reader = PdfFileReader(open(pdf_name, 'rb'))
        page_counts = pdf_reader.getNumPages()
        for i in range(page_counts):
            page = pdf_reader.getPage(i)
            pdf_write.addPage(page)
    pdf_write.write(open(OUTPUT_FILE, 'wb'))
    print('Done!')


if __name__ == '__main__':
    main()
