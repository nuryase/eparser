import argparse
from utils import process_epub


def parse_args():
    parser = argparse.ArgumentParser(description="Process EPUB Files")

    # Required arguments
    parser.add_argument("epub_file_path", help="Path to the EPUB file")
    parser.add_argument("ebook_name", help="Name of the eBook")

    # Optional argument
    parser.add_argument(
        "--out_directory", "-o", help="Output directory for processed content"
    )

    return parser.parse_args()


def main():
    args = parse_args()

    # Call your function with the provided arguments
    files = process_epub(
        args.epub_file_path, args.ebook_name, out_directory=args.out_directory
    )

    # Optionally, you can print or use the returned files


if __name__ == "__main__":
    main()
