from file_handling import process_epub
from parsing import parse_contents


def get_ebook(epub_file_path: str, epub_name: str):
    """
    Creates eBook from EPUB.

    Parameters
    ----------

        epub_file_path: str
            Path leading to EPUB file.

        epub_name: str
            Name of the eBook.
    """
    filenames = process_epub(epub_file_path, epub_name)
    ebook = parse_contents("extracted-epubs/" + epub_name, filenames)
    return ebook
