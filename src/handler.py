import zipfile
import os


class EPUBHandler:
    """
    Unzips and extracts EPUB contents contained in the OEBPS folder.

    OEBPS folder contains the .xhtml/.html container chapters.
    """

    def __init__(self, path: str, outdir_name: str):
        """
        Parameters
        ----------

        path: str
            Path to EPUB file.

        outdir_name: str
            Name for the directory containing the extracted EPUB contents.
        """
        self.path = path
        self.outdir_name = outdir_name

    def set_current_path(self):
        """
        Sets path to the directory for extracted EPUB contents.
        """
        current_path = os.getcwd()
        epub_directory = os.path.join(current_path, "extracted-epubs", self.outdir_name)

        try:
            # Check if the directory already exists
            if not os.path.exists(epub_directory):
                os.makedirs(epub_directory)
            else:
                pass

        except OSError as error:
            print("ERROR CHECK:", error)

        return epub_directory

    def extract_contents(self):
        """
        Unzips given EPUB file and extracts content into directory in set_current_path().
        """
        epub_directory = self.set_current_path()

        try:
            with zipfile.ZipFile(self.path, "r") as zip_ref:
                zip_ref.extractall(epub_directory)

            print("Successful extraction of EPUB contents.")

        except FileNotFoundError:
            print("ERROR: EPUB file could not be found" + "\n" + self.path)
        except Exception as error:
            print("ERROR CHECK:", error)

    def get_filenames(self):
        """
        Obtains chapter filenames from the OEBPS folder and stores them in a list.

        Returns
        -------

            contents: List[str]
                A list containing filenames ending with .xhtml/.html
        """
        contents = []
        epub_directory = self.set_current_path()
        oebps_path = os.path.join(epub_directory, "OEBPS")

        for filename in sorted(os.listdir(oebps_path)):
            if filename.endswith("html"):
                contents.append(filename)

        return contents
