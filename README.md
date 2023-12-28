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


