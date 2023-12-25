from eparser.handler import EPUBHandler
from eparser.eparser import Parser

# Handle and Parse

extract = EPUBHandler("~/Downloads/copy.epub", "New-Book")

extract.extract_contents()

parser = Parser(extract.get_chapters(), extract.current_path())
content = parser.parser.contents()

print(content[1])
