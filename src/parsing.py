from lxml import etree
import os


def parse_contents(directory_path: str, filenames: list[str]):
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
        file_path = os.path.join(directory_path, filename)

        try:
            tree = etree.parse(file_path)
            paragraphs = tree.xpath(
                "//xhtml:p", namespaces={"xhtml": "http://www.w3.org/1999/xhtml"}
            )
            chapter_contents = "\n".join(
                [
                    etree.tostring(paragraph, method="text", encoding="utf-8").decode(
                        "utf-8"
                    )
                    for paragraph in paragraphs
                ]
            )

            ebook[chapter_number] = chapter_contents
            chapter_number += 1

        except Exception as error:
            print("ERROR CHECK:", error)

    return ebook
