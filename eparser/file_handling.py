import logging
import os
import patoolib
from natsort import os_sorted


def extract_contents(
    epub_file_path: str, ebook_name: str, out_directory: str | None = None
):
    """
    Unzips an EPUB file and extracts its contents.

    Parameters
    ----------
    epub_file_path : str
        Path leading to the EPUB file.

    ebook_name : str
        Name of the eBook.

    out_directory : str, optional
        Directory to extract the contents into (default: None).
    """
    if out_directory is None:
        out_directory = default_path(ebook_name)

    try:
        # Verbosity set to -1 ignores patoolib prints
        patoolib.extract_archive(epub_file_path, outdir=out_directory, verbosity=-1)
    except FileNotFoundError:
        logging.error(f"ERROR: EPUB file not found:\n{epub_file_path}")
    except Exception as error:
        logging.error(error)


def default_path(ebook_name: str):
    """
    Sets the default extraction path.

    Parameters
    ----------
    ebook_name : str
        Name of the eBook.

    Returns
    -------
    str
        Path to the extracted EPUBs.
    """
    current_path = os.getcwd()
    epub_directory = os.path.join(current_path, "extracted-epubs", ebook_name)

    if not os.path.exists(epub_directory):
        try:
            os.makedirs(epub_directory)
        except OSError as error:
            logging.error(error)

    return epub_directory


def get_html_files(
    ebook_name: str, standard: bool = False, directory_path: str | None = None
):
    """
    Obtains chapter filenames from the OEBPS folder and stores them in a list.

    Parameters
    ----------
    ebook_name : str
        Name of the eBook.

    standard : bool, optional
        Indicates whether it is a StandardEBook format (True) or OEBPS format (False, default).

    directory_path : str, optional
        Directory to extract the contents into (default: None).

    Returns
    -------
    list[str]
        A list containing chapter filenames.
    """
    if directory_path is None:
        directory_path = default_path(ebook_name)

    if standard:
        file_path = os.path.join(directory_path, "epub", "text")
    else:
        file_path = os.path.join(directory_path, "OEBPS")

    # Obtain the list of all files in the directory
    all_files = os_sorted(os.listdir(file_path))

    if standard:
        html_files = [
            filename
            for filename in all_files
            if filename.startswith(ebook_name.lower()) and filename.endswith("html")
        ]
        html_files += [
            filename
            for filename in all_files
            if filename.startswith("chap") and filename.endswith("html")
        ]
        html_files += [
            filename
            for filename in all_files
            if filename.startswith("act") and filename.endswith("html")
        ]

    else:
        html_files = [
            filename
            for filename in all_files
            if filename.startswith("chap") and filename.endswith("html")
        ]

    return html_files, file_path
