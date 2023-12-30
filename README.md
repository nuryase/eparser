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
from eparser import get_ebook, process_epub

# Example 1: Using get_ebook to directly obtain the eBook dictionary
epub_file_path = 'path-to-epub-file.epub'
ebook_name = 'MyEBook'
ebook = get_ebook(epub_file_path, ebook_name)

# Accessing eBook Chapters
chapter_number = 1
print(f"Content of Chapter {chapter_number}:\n{ebook[chapter_number]}")

# Example 2: Using process_epub to get filenames and file_path, then parsing contents separately
epub_file_path = 'another-path-to-epub-file.epub'
ebook_name = 'AnotherEBook'
out_directory = '/custom/output/directory'
standard_format = True

## Note that standard_format and out_directory are optional

# Get filenames and file_path using process_epub
filenames, file_path = process_epub(epub_file_path, ebook_name, standard_format, out_directory)

# Parse contents using the obtained filenames and file_path
ebook = parse_contents(filenames, file_path)

# Accessing eBook Chapters
chapter_number = 3
print(f"Content of Chapter {chapter_number}:\n{ebook[chapter_number]}")
```

## Misc
eParser is an integral part of the [**brew**](https://github.com/nuryase/brew) application: An eBook reader app.


## Notes
Benchmark criteria are established based on both the quantity of .xhtml/.html files and the size of each file.

The library exclusively supports [**StandardEBooks**](https://standardebooks.org/ebooks) or OEBPS-formatted files. It does not provide compatibility with [**Gutenberg**](https://www.gutenberg.org/) EPUBS.

## EPUB Validity

Refer to ```validity.md``` to view examples that illustrate the acceptable formats for EPUBs extracted in eParser. Only EPUBs formatted similarly to these examples are considered valid. It is important to note that all examples, with the exception of ```Viewpoint```, adhere to the StandardEBooks format. ```Viewpoint``` utilizes the [**OEBPS**](https://en.wikipedia.org/wiki/EPUB#Open_Container_Format_2.0.1) formatting.
