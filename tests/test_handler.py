import eparser.auxiliary

contents = eparser.auxiliary.create_ebook_from_path(
    "Users/yacquub/Downloads/copy.epub", "ORV"
)

print(contents[1])
