## html book 下载器

本程序采用 python3.6 编写，依赖 pdfkit, requests, PyPDF2 库。代码结构如下：

- URLProvider.py url 管理器，内部维护一个 url 序列。
- generator.py pdf 生成部分。通过 url 管理器 爬取 html 信息，生成 pdf 文件。