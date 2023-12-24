from lxml import etree
from handler import EPUBHandler


class Parser:
    """
    Parses .xhtml/.html files into plain text.
    """

    def __init__(self, contents: list, path: str):
        """
        contents - A list containing filenames ending with .xhtml/.html
        path - Path leading to the extracted EPUB directory.
        """
        self.contents = contents
        self.path = path

    def parse_contents(self):
        """
        Parses .xhtml/.html in OEBPS folder and stores text in a dictionary.

        Return:
            ebook - A dictionary with key : value pairs in the form chapter_number : chapter_contents.

            **Use chapter_contents = ebook[chapter_number]**
        """
        contents = self.contents
        ebook = dict()
        chapter_number = 1

        for filename in contents:
            tree = etree.parse(filename)

            paragraphs = tree.xpath("//p")
            chapter_text = ""

            for paragraph in paragraphs:
                chapter_text += str(paragraph.text) + "\n" + "\n"

            ebook[chapter_number] = paragraph.text
            chapter_number += 1

        return ebook
