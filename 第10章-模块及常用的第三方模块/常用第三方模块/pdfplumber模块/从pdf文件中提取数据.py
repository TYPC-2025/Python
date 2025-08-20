import pdfplumber
#打开PDF文件
with pdfplumber.open('Philomath第二届非数学类参考解析.pdf') as pdf:
    for i in pdf.pages: #遍历页
        print(i.extract_text()) # extract_text()提取内容
        print(f'----------第{i.page_number}页结束')
