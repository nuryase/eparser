from handler import EPUBHandler
from eparser import Parser

# Handle and Parse

extract = EPUBHandler("/Users/yacquub/Downloads/copy.epub", "Book")

extract.extract_contents()

parser = Parser(extract.get_filenames(), extract.set_current_path())
content = parser.parse_contents()

print("Contents: ", content[1])
