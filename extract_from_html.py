"""Converted pdf with the help of xpdf into html files.

"""
import codecs
# import csv
# wb = xlrd.open_workbook("Besitzer.xlsx", encoding_override='latin-1')
# sheet = wb.sheet_by_name('Besitzer')
# besitzer = [c.value for c in sheet.col_slice(0)]
# besitzer[6]


f = codecs.open('html/page{}.html'.format(22), encoding='utf-8')
text = f.read()

f = codecs.open("Besitzer.txt", encoding='cp1252')
lines = f.readlines()
besitzer = sorted(list(set([line.split('\t')[1] for line in lines if len(line.split('\t')[1]) > 0])))

word_list = besitzer
pages = {key: [] for key in word_list}
for page_number in range(1, 463):
    f = codecs.open('html/page{}.html'.format(page_number), encoding='utf-8')
    text = f.read()
    for word in word_list:
        if word in text:
            pages[word].append(page_number)
print([u'{}: {}'.format(key, pages[key]) for key in besitzer])

f = codecs.open('text.html', 'w', encoding='utf-8')
s = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN"
    "http://www.w3.org/TR/html4/strict.dtd">
<html lang="en">
  <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    <title>title</title>
    <link rel="stylesheet" type="text/css" href="style.css">
    <script type="text/javascript" src="script.js"></script>
  </head>
  <body>'''
s += '<br>'.join([u'{}: {}'.format(key, pages[key]) for key in besitzer])
s+= '''
  </body>
</html>
'''
f.write(s)