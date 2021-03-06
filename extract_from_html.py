"""Converted pdf with the help of xpdf into html files.

"""
import codecs
from bs4 import BeautifulSoup

f = codecs.open('html/page{}.html'.format(22), encoding='utf-8')
text = f.read()

soup = BeautifulSoup(text, 'html.parser')
snippets = [s for s in soup.findAll(recursive=True, text=True) if s not in ['\n', ]]
snippets_without_end_dashes = [s if s[-1] not in ['-'] else s[:-1] for s in snippets]
text_without_end_dashes = u"".join(snippets_without_end_dashes)

f = codecs.open("keywords.txt", encoding='cp1252')
lines = f.readlines()
# take the second column of a csv file, adapt this to the provided keyword list.
word_list = sorted(list(set([line.split('\t')[1] for line in lines if len(line.split('\t')[1]) > 0])))

pages = {key: [] for key in word_list}
for page_number in range(1, 463):
    f = codecs.open('html/page{}.html'.format(page_number), encoding='utf-8')
    text = f.read()
    soup = BeautifulSoup(text, 'html.parser')
    snippets = [s for s in soup.findAll(recursive=True, text=True) if s not in ['\n', ]]
    snippets_without_end_dashes = [s if s[-1] not in ['-'] else s[:-1] for s in snippets]
    text_without_end_dashes = u"".join(snippets_without_end_dashes)
    for word in word_list:
        if word in text_without_end_dashes:
            pages[word].append(page_number)
print([u'{}: {}'.format(key, pages[key]) for key in word_list])

f = codecs.open('index.html', 'w', encoding='utf-8')
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
s += '<br>'.join([u'{}: {}'.format(key, pages[key]) for key in word_list])
s+= '''
  </body>
</html>
'''
f.write(s)