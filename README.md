# Index pdf document

In general, PDF is a bad format to use extract an index of page numbers for specific keywords.
There are, however, some situations in which the text source or other means are not available.
So here is one work-around on how to generate an index on a Windows computer.

# Using xpdf

Good results can be achieved using the open source software [xpdf](http://www.foolabs.com/xpdf/download.html) and a python script.
In the first step the pdf is converted to individual html pages using

    pdftohtml.exe pdf_file.pdf html
    
where `pdf_file.pdf` is the pdf to be analysed and `html` is the output directory.
From the html output we generate the index by running the python script `extract_from_html` which assumes the `html` folder to be present and generates and html index.

