from lxml import etree
import os


def parse_contents(epub_directory: str, filenames: list[str]):
    """
    Parses .xhtml/.html in OEBPS folder and stores text in a dictionary.

    Returns
    -------
        ebook: dict
            A dictionary with key : value pairs in the form chapter_number : chapter_contents.

        **Use chapter_contents = ebook[chapter_number]**
    """
    ebook = dict()
    chapter_number = 1

    for filename in filenames:
        file_path = os.path.join(epub_directory, "OEBPS", filename)

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                chapter_text = file.read()

            ebook[chapter_number] = chapter_text
            chapter_number += 1

        except Exception as error:
            print("ERROR CHECK:", error)

    return ebook
