from file_handling import extract_contents, get_html_files
from parsing import parse_contents
from typing import List


def get_ebook(
    epub_file_path: str,
    ebook_name: str,
    standard: bool = False,
    out_directory: str = None,
):
    """
    Creates an eBook dictionary from EPUB.

    Parameters
    ----------
    epub_file_path: str
        Path leading to the EPUB file.

    ebook_name: str
        Name of the eBook.

    standard: bool, optional
        Indicates whether it is a StandardEBook format (True) or OEBPS format (False, default).

    out_directory: str, optional
        Location where the EPUB will be extracted. Defaults to the default path if None.

    Returns
    -------
    dict
        eBook dictionary with chapter number as the key and chapter contents as the value.
    """
    filenames, file_path = process_epub(
        epub_file_path, ebook_name, standard, out_directory
    )
    ebook = parse_contents(filenames, file_path)
    return ebook


def process_epub(
    epub_file_path: str,
    ebook_name: str,
    standard: bool = False,
    out_directory: str = None,
):
    """
    Handles the extraction process for EPUB.

    Parameters
    ----------
    epub_file_path: str
        Path leading to EPUB file.

    ebook_name: str
        Name of the eBook.

    standard: bool, optional
        Indicates whether it is a StandardEBook format (True) or OEBPS format (False, default).

    out_directory: str, optional
        Location where the EPUB will be extracted. Defaults to the default path if None.

    Returns
    -------
    List[str], str
        A list of filenames referring to the chapters and the file path leading to the extracted contents.
    """
    extract_contents(epub_file_path, ebook_name, out_directory)
    filenames, file_path = get_html_files(ebook_name, standard, out_directory)

    return filenames, file_path
