from eparser import Parser
from handler import EPUBHandler


def create_ebook_from_path(epub_path: str, folder_name: str):
    """
    Parses the EPUB file into an eBook stored in a dictionary given the EPUB path.

    Parameters:
        epub_path - Path leading to the EPUB file.
        folder_name - Name for the folder containing the extracted contents.

    Returns:
        contents - Dictionary containing the eBook. Denoted (chapter_number : chapter_contents)
    """
    extract = EPUBHandler(epub_path, folder_name)
    extract.extract_contents()

    parser = Parser(extract.get_filenames(), extract.set_current_path())
    contents = parser.parse_contents()

    return contents


def create_ebook_from_extracted(oebps_path, folder_name):
    """
    Parses a pre-extracted EPUB file into an eBook stored in a dictionary given the OEBPS path.

    Parameters:
        oebps_path - Path leading to the extracted folder.
        folder_name - Folder to be parsed.

    Returns:
        contents - Dictionary containing the eBook. Denoted (chapter_number : chapter_contents)
    """
    extract = EPUBHandler(oebps_path, folder_name)

    parser = Parser(extract.get_filenames(), extract.set_current_path())
    contents = parser.parse_contents()

    return contents
