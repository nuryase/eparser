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

# Extract and parse the contents of the EPUB file
ebook = get_ebook(epub_file_path)

# Accessing eBook Chapters
# Each chapter can be accessed using its corresponding chapter number
chapter_number = 1
print(f"Content of Chapter {chapter_number}:\n{ebook[chapter_number]}")
```


## Misc
eParser will be used in the [**brew**](https://github.com/nuryase/brew) application: An eBook reader app.

Refactor handler.py and eparser.py and test using multiple epubs.
