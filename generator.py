import os

import pdfkit
import requests
from PyPDF2 import PdfFileWriter, PdfFileReader
import threading
import time

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


class URL_resolver(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
    def run(self):
        html = get_html(self.url)
        html = html_transform(html)
        print('generate html {}'.format(self.url))
        self.pdf_name = os.path.join(TMP_DIR, self.url.split('/')[-1] + '.pdf')
        pdfkit.from_string(html, self.pdf_name)
        
        

def main():
    provider = URLProvider()
    threads = []
    for url in provider.next():
        thread = URL_resolver(url)
        thread.start()
        threads.append(thread)

    pdf_write = PdfFileWriter()
    for t in threads:
        t.join()
        pdf_reader = PdfFileReader(open(t.pdf_name, 'rb'))
        page_counts = pdf_reader.getNumPages()
        for i in range(page_counts):
            page = pdf_reader.getPage(i)
            pdf_write.addPage(page)

    pdf_write.write(open(OUTPUT_FILE, 'wb'))
    print('Done!')


if __name__ == '__main__':
    s = time.time()
    main()
    e = time.time()
    print('耗时 {}s'.format(e - s))
