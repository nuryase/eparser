from file_handling import extract_contents, get_html_files
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


def process_epub(epub_file_path: str, ebook_name: str, out_directory: str = None):
    """
    Auxiliary function.
    """
    extract_contents(epub_file_path, ebook_name, out_directory)
    files = get_html_files(ebook_name, out_directory)

    return files
