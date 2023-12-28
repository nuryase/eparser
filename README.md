# eParser

eParser is a Python library designed for handling and parsing EPUB files. EPUB is a popular digital eBook format, and eParser simplifies the extraction and parsing of text content from these files.

### Getting Started

To begin using eParser, install it using pip: (Note: installation currently does not work)

```bash
pip install eparser
```

## Usage
eParser simplifies the process of working with EPUB files in Python, offering a convenient way to extract and parse textual content. 

The primary goal is to streamline the creation of eBooks from EPUB files without the need for external tools.

The following example demonstrates how to use eParser to process an EPUB file:

```py
from eparser import get_ebook

# Specify the path to the EPUB file
epub_file_path = 'path-to-epub-file'

# Specify the name of the eBook
ebook_name = 'Lord of the Mysteries'

# Extract and parse the contents of the EPUB file
ebook = get_ebook(epub_file_path, ebook_name)

# Accessing eBook Chapters
# Each chapter can be accessed using its corresponding chapter number
chapter_number = 1
print(f"Content of Chapter {chapter_number}:\n{ebook[chapter_number]}")
```

## Misc
eParser is an integral part of the [**brew**](https://github.com/nuryase/brew) application: An eBook reader app.


## Notes
Benchmark criteria are established based on both the quantity of .xhtml/.html files and the size of each file.

The library exclusively supports [**StandardEBooks**](https://standardebooks.org/ebooks) or OEBPS-formatted files. It does not provide compatibility with [**Gutenberg**](https://www.gutenberg.org/) EPUBS.

* Update DocStrings.

## EPUB Validity

The following illustrates the acceptable formats for EPUBs extracted in eParser. Only EPUBs formatted similarly to these examples are considered valid. Note that all examples, except for ```Viewpoint```, adhere to the StandardEBooks format. ```Viewpoint``` utilizes the [**OEBPS**](https://en.wikipedia.org/wiki/EPUB#Open_Container_Format_2.0.1) formatting.

```bash
├── Poetry
│   ├── META-INF
│   │   └── container.xml
│   ├── epub
│   │   ├── content.opf
│   │   ├── css
│   │   │   ├── core.css
│   │   │   ├── local.css
│   │   │   └── se.css
│   │   ├── images
│   │   │   ├── cover.jpg
│   │   │   ├── logo.png
│   │   │   └── titlepage.png
│   │   ├── onix.xml
│   │   ├── text
│   │   │   ├── colophon.xhtml
│   │   │   ├── imprint.xhtml
│   │   │   ├── poetry.xhtml
│   │   │   ├── titlepage.xhtml
│   │   │   └── uncopyright.xhtml
│   │   ├── toc.ncx
│   │   └── toc.xhtml
│   └── mimetype
├── The-Diary
│   ├── META-INF
│   │   └── container.xml
│   ├── epub
│   │   ├── content.opf
│   │   ├── css
│   │   │   ├── core.css
│   │   │   ├── local.css
│   │   │   └── se.css
│   │   ├── images
│   │   │   ├── cover.jpg
│   │   │   ├── illustration-1.png
│   │   │   ├── logo.png
│   │   │   └── titlepage.png
│   │   ├── onix.xml
│   │   ├── text
│   │   │   ├── afterword.xhtml
│   │   │   ├── chapter-1.xhtml
│   │   │   ├── colophon.xhtml
│   │   │   ├── endnotes-1.xhtml
│   │   │   ├── endnotes-10.xhtml
│   │   │   ├── endnotes-2.xhtml
│   │   │   ├── endnotes-3.xhtml
│   │   │   ├── endnotes-4.xhtml
│   │   │   ├── endnotes-5.xhtml
│   │   │   ├── endnotes-6.xhtml
│   │   │   ├── endnotes-7.xhtml
│   │   │   ├── endnotes-8.xhtml
│   │   │   ├── endnotes-9.xhtml
│   │   │   ├── foreword.xhtml
│   │   │   ├── halftitlepage.xhtml
│   │   │   ├── imprint.xhtml
│   │   │   ├── introduction.xhtml
│   │   │   ├── loi.xhtml
│   │   │   ├── titlepage.xhtml
│   │   │   └── uncopyright.xhtml
│   │   ├── toc.ncx
│   │   └── toc.xhtml
│   └── mimetype
├── The-Jew-Of-Malta
│   ├── META-INF
│   │   └── container.xml
│   ├── epub
│   │   ├── content.opf
│   │   ├── css
│   │   │   ├── core.css
│   │   │   ├── local.css
│   │   │   └── se.css
│   │   ├── images
│   │   │   ├── cover.jpg
│   │   │   ├── logo.png
│   │   │   └── titlepage.png
│   │   ├── onix.xml
│   │   ├── text
│   │   │   ├── act-1.xhtml
│   │   │   ├── act-2.xhtml
│   │   │   ├── act-3.xhtml
│   │   │   ├── act-4.xhtml
│   │   │   ├── act-5.xhtml
│   │   │   ├── colophon.xhtml
│   │   │   ├── dramatis-personae.xhtml
│   │   │   ├── endnotes.xhtml
│   │   │   ├── halftitlepage.xhtml
│   │   │   ├── imprint.xhtml
│   │   │   ├── prologue.xhtml
│   │   │   ├── titlepage.xhtml
│   │   │   └── uncopyright.xhtml
│   │   ├── toc.ncx
│   │   └── toc.xhtml
│   └── mimetype
├── The-Mystery-of-the-Yellow-Room
│   ├── META-INF
│   │   └── container.xml
│   ├── epub
│   │   ├── content.opf
│   │   ├── css
│   │   │   ├── core.css
│   │   │   ├── local.css
│   │   │   └── se.css
│   │   ├── images
│   │   │   ├── cover.jpg
│   │   │   ├── illustration-1.jpg
│   │   │   ├── illustration-2.png
│   │   │   ├── illustration-3.png
│   │   │   ├── logo.png
│   │   │   └── titlepage.png
│   │   ├── onix.xml
│   │   ├── text
│   │   │   ├── chapter-1.xhtml
│   │   │   ├── colophon.xhtml
│   │   │   ├── endnotes.xhtml
│   │   │   ├── frontispiece.xhtml
│   │   │   ├── halftitlepage.xhtml
│   │   │   ├── imprint.xhtml
│   │   │   ├── loi.xhtml
│   │   │   ├── titlepage.xhtml
│   │   │   └── uncopyright.xhtml
│   │   ├── toc.ncx
│   │   └── toc.xhtml
│   └── mimetype
└── Viewpoint (NON-STANDARD)
    ├── META-INF
    │   └── container.xml
    ├── OEBPS
    │   ├── README.MD
    │   ├── chap_00001.xhtml
    │   ├── chap_00002.xhtml
    │   ├── content.opf
    │   ├── cover.xhtml
    │   ├── footn-injection.json
    │   ├── image.jpg
    │   ├── images
    │   │   └── titlepage800.png
    │   ├── intro.xhtml
    │   ├── nav.xhtml
    │   ├── pack-all.sh
    │   ├── prepare.sh
    │   ├── toc.ncx
    │   ├── word-replace.json
    │   ├── word-replace.txt
    │   └── wordReplace2.js
    └── mimetype

```