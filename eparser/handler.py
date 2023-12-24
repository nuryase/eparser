import zipfile
import os


class EPUBHandler:
    """
    Unzips and extracts EPUB contents contained in the OEBPS folder.

    OEBPS folder contains the .xhtml/.html container chapters.
    """

    def __init__(self, path: str, outdir_name: str):
        """
        path - Path to EPUB file.
        outdir_name - Name for the directory containing the extracted EPUB contents.
        """
        self.path = path
        self.outdir_name = outdir_name

    def set_current_path(self):
        """
        Sets path to the directory for extracted EPUB contents.
        """
        current_path = os.getcwd()
        return current_path + "/extracted-epubs/" + self.outdir_name + "/"

    def extract_contents(self):
        """
        Unzips given EPUB file and extracts content into directory in set_current_path().
        """
        epub_directory = self.set_current_path()

        try:
            os.mkdir(epub_directory)
            print("Successful creation of EPUB directory.")

        except OSError as error:
            print("ERROR:", error)

        try:
            with zipfile.ZipFile(self.path, "r") as zip_ref:
                zip_ref.extractall(epub_directory)

        except FileNotFoundError:
            print("ERROR: EPUB file could not be found" + "\n" + self.path)

    def get_filenames(self):
        """
        Obtains chapter filenames from the OEBPS folder and stores them in a list.

        Returns:
            contents - A list containing filenames ending with .xhtml/.html
        """
        contents = []
        epub_directory = self.set_current_path()

        for filename in sorted(os.listdir(epub_directory + "OEBPS/")):
            if filename.endswith("html"):
                contents.append(filename)

        return contents
