from file_handling import extract_contents, get_html_files
from parsing import parse_contents


def get_ebook(
    epub_file_path: str,
    epub_name: str,
    standard: bool = False,
    out_directory: str = None,
):
    """
    Creates eBook from EPUB.

    Parameters
    ----------

        epub_file_path: str
            Path leading to EPUB file.

        epub_name: str
            Name of the eBook.
    """
    filenames, file_path = process_epub(
        epub_file_path, epub_name, standard, out_directory
    )
    ebook = parse_contents(file_path, filenames)
    return ebook


def process_epub(
    epub_file_path: str,
    ebook_name: str,
    standard: bool = False,
    out_directory: str = None,
):
    """
    Auxiliary function.
    """
    extract_contents(epub_file_path, ebook_name, out_directory)
    filenames, file_path = get_html_files(ebook_name, standard, out_directory)

    return filenames, file_path
