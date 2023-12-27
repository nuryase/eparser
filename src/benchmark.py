import timeit
from utils import get_ebook


def benchmark_small_process(epub_path: str, ebook_name: str):
    """
    Benchmarks process for a small EPUB.
    """

    # Test with small EPUB (no metrics as of yet)
    small_epub_process = get_ebook(epub_path, ebook_name)
    return small_epub_process


def benchmark_medium_process(epub_path: str, ebook_name: str):
    """
    Benchmarks process for a medium EPUB.
    """

    # Test with Large EPUB (550~ chapters)
    large_epub_process = get_ebook(epub_path, ebook_name)
    return large_epub_process


def benchmark_large_process(epub_path: str, ebook_name: str):
    """
    Benchmarks process for a large EPUB.
    """

    # Test with Large EPUB (550~ chapters)
    large_epub_process = get_ebook(epub_path, ebook_name)
    return large_epub_process


if __name__ == "__main__":
    start_time = timeit.default_timer()
    benchmark_large_process("tests/test-epubs/medium.epub", "medium")
    # full_process = get_ebook("tests/test.epub", "test")
    print("Medium EPUB Process: ", timeit.default_timer() - start_time)
