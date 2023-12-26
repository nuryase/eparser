# eParser

eParser is a library for handling and parsing EPUB files.


# Usage
eParser unzips, extracts, and parses the contents of the EPUB file, focusing on the text contained within.

The main usage of eParser is to obtain the eBook contents contained within an EPUB file without the need for third-party software.

Below is an example of how eParser can be used:

```py
from eparser import get_ebook

# extracts and parses the contents of the epub file given its path
ebook = get_ebook('path-to-epub-file')

# ebook chapter contents can be accessed using the chapter number
print(ebook[1])
```


# Misc
eParser will be used in the [**brew**](https://github.com/nuryase/brew) application: An e-book reader app.

Refactor handler.py and eparser.py and test using multiple epubs.
