# coding=utf-8
"""Generate a keyword index of a pdf file.

"""
from __future__ import print_function, unicode_literals
import pdfquery
import StringIO
from lxml import etree
import textract

s = u"Königsegg"
print(s)

word_list = [u"Königsegg", u"Koppel", u"Kornek", u"Kratz", u"Krebs", u"Kristaller",]
print(word_list, )


fp = "Obenaus_Umbruch_S1-462_low_MO_2.pdf"
text = textract.process(fp, encoding='latin-1')
parser = textract.parsers.pdf_parser.Parser()
text = parser.extract(fp, method='tesseract')

pdf = pdfquery.PDFQuery(fp, )
pdf.load()
# pdf.file.write("test")
pdf.load(0)
s = StringIO.StringIO()
pdf.tree.write(s, pretty_print=True, encoding="utf-8")
etree.tostring(pdf.tree, pretty_print=True)
print('Andr' in s.getvalue())

# pdf.extract([('with_parent','LTPage[pageid=1]'), ('with_formatter', 'text'),])

# word_list = ['collective', 'chlamy', 'molecular motors', 'energy']
pages = {key: set() for key in word_list}
# label = pdf.pq('LTTextLineHorizontal')

# for key in word_list:
#     if key in s.getvalue():
#         print key
#     else:
#         print 'nothing'

page = 0
while True:
    print(page)
    if page > 50:
        break
    try:
        pdf = pdfquery.PDFQuery(fp)
        pdf.load(page)
        # pdf.load(1)
        # s = StringIO.StringIO()
        # pdf.tree.write(s, pretty_print=True, encoding="latin-1")
        content = etree.tostring(pdf.tree, pretty_print=True)
        for key in word_list:
            if key in content:
                pages[key].add(page)
            if key.title() in content:
                pages[key].add(page)
        page += 1
        # s.close()
    except StopIteration:
        break

print({key: sorted(list(pages[key])) for key in pages.keys()})



# pdf.load(51)
# d = pdf.extract([('with_formatter', lambda match: match.text()),
#                  ('test', 'LTTextLineHorizontal:contains("Ideas")')])
# print d
# from pdfminer.pdfdevice import PDFDevice
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.pdfpage import PDFPage
# from pdfminer.pdfparser import PDFParser
# from pdfminer.pdfdocument import PDFDocument, PDFTextExtractionNotAllowed
# pdf.pq('LTTextLineHorizontal:contains("retiring")')
# pdf.extract([
#     # ('with_parent','LTPage[page_index="1"]'),
#     ('last_name', ':in_bbox("315,680,395,700")')  # only matches elements on page 1
# ])
# f = open(fp, 'rb')
# # Create a PDF parser object associated with the file object.
# parser = PDFParser(f)
# # Create a PDF document object that stores the document structure.
# # Supply the password for initialization.
# document = PDFDocument(parser)
# # Check if the document allows text extraction. If not, abort.
# if not document.is_extractable:
#     raise PDFTextExtractionNotAllowed
# # Create a PDF resource manager object that stores shared resources.
# rsrcmgr = PDFResourceManager()
# # Create a PDF device object.
# device = PDFDevice(rsrcmgr)
# # Create a PDF interpreter object.
# interpreter = PDFPageInterpreter(rsrcmgr, device)
# # Process each page contained in the document.
# for page in PDFPage.create_pages(document):
#     interpreter.process_page(page)

# # Get the outlines of the document.
# outlines = document.get_outlines()
# for (level,title,dest,a,se) in outlines:
#     print (level, title)
# d = pdf.extract([('with_formatter', lambda match: match.text()), ] +
#                 [('{}'.format(key), 'LTTextLineHorizontal:contains("{}")'.format(key)) for key in word_list] +
#                 [('{}'.format(key), 'LTTextLineHorizontal:contains("{}")'.format(key.title())) for key in word_list])
