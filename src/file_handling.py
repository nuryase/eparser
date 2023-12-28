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


def get_html_files(ebook_name: str, standard: bool = False, directory_path: str = None):
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

    if standard:
        file_path = os.path.join(
            directory_path, "epub", "text"
        )  # Adjust the path accordingly
    else:
        file_path = os.path.join(directory_path, "OEBPS")

    # Obtain the list of all files in the directory
    all_files = sorted(os.listdir(file_path))

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
