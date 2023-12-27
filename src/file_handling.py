import patoolib
import os


def extract_contents(epub_file_path: str, ebook_name: str, out_directory: str = None):
    """
    Unzips EPUB and extracts contents.

    Parameters
    ----------

        epub_file_path: str
            Path leading to EPUB file.

        ebook_name: str
            Name of the eBook.

        out_directory: str
            Directory to extract the contents into (default: None)
    """
    if out_directory is None:
        out_directory = default_path(ebook_name)

    try:
        patoolib.extract_archive(epub_file_path, outdir=out_directory)

    except FileNotFoundError:
        print("ERROR: EPUB file could not be found" + "\n" + epub_file_path)
    except Exception as error:
        print("ERROR CHECK:", error)


def default_path(ebook_name: str):
    """
    Sets default path.

    Parameters
    ----------

        ebook_name: str
            Name of the eBook.

    Returns
    -------

        epub_directory: str
            Path to the extracted EPUBS.
    """
    current_path = os.getcwd()
    epub_directory = os.path.join(current_path, "extracted-epubs", ebook_name)

    if not os.path.exists(epub_directory):
        try:
            os.makedirs(epub_directory)
        except OSError as error:
            print("ERROR CHECK:", error)

    return epub_directory


def get_html_files(ebook_name: str, directory_path: str = None):
    """
    Obtains chapter filenames from the OEBPS folder and stores them in a list.

    Parameters
    ----------

        ebook_name: str
            Name of the eBook.

        directory_path: str
            Directory to extract the contents into (default: None)

    Returns
    -------

        filenames: List[str]
            A list containing chapter filenames.
    """
    if directory_path is None:
        directory_path = default_path(ebook_name)

    oebps_path = os.path.join(directory_path, "OEBPS")

    html_files = [
        filename
        for filename in sorted(os.listdir(oebps_path))
        if filename.endswith("html") and filename.startswith("chap")
    ]

    return html_files


def process_epub(epub_file_path: str, ebook_name: str, out_directory: str = None):
    """
    Auxiliary function. Move to utils.py
    """
    extract_contents(epub_file_path, ebook_name, out_directory)
    files = get_html_files(ebook_name, out_directory)

    return files
