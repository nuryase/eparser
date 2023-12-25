from lxml import etree
from handler import EPUBHandler
import os


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
        epub_directory = self.path

        for filename in contents:
            file_path = os.path.join(epub_directory, "OEBPS", filename)
            tree = etree.parse(file_path)

            paragraphs = tree.xpath(
                "//xhtml:p", namespaces={"xhtml": "http://www.w3.org/1999/xhtml"}
            )
            chapter_text = ""

            for paragraph in paragraphs:
                chapter_text += (
                    etree.tostring(paragraph, method="text", encoding="utf-8").decode(
                        "utf-8"
                    )
                    + "\n"
                )

            ebook[chapter_number] = chapter_text
            chapter_number += 1

        return ebook
