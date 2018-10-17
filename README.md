## html book 下载器

envirement: python3.6

depends:    
- pdfkit
- requests
- PyPDF2
- wkhtmltopdf

程序逻辑并不复杂，甚至极为简单。单页面 html 生成 pdf 采用 wkhtmltopdf 工具(需要单独安装)。pdfkit 是对该工具的python 封装。requests 用来请求 html 页面。PyPDF2 用来将各单独html生成的pdf 合并为一个文件。整个程序划分为两个文件。使用者对 URLProvider.py 进行扩充就可以处理自己的业务。
- URLProvider.py url 管理器，内部维护一个 url 序列。
- generator.py pdf 生成部分。通过 url 管理器 爬取 html 信息，生成 pdf 文件。