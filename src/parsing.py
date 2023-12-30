import os
from lxml import etree
from typing import List
import logging


def parse_contents(filenames: List[str], directory_path: str):
    """
    Parses .xhtml/.html files in the extracted folder and stores text in an eBook dictionary.

    Parameters
    ----------
    filenames : List[str]
        List of filenames corresponding to the .xhtml/.html files to be parsed.

    directory_path : str
        Path to the directory containing the .xhtml/.html files.

    Returns
    -------
    dict
        A dictionary with key-value pairs representing chapter numbers and their contents.
        To access chapter contents, use `chapter_contents = ebook[chapter_number]`.
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
            logging.error(error)
            print("ERROR CHECK:", error)

    return ebook
