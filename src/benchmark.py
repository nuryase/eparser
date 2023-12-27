import timeit
from utils import get_ebook


def benchmark_process(epub_path: str, ebook_name: str):
    """
    Benchmarks process for a different EPUB sizes.

    Process time is determined by the number and size of .xhtml/html files.

    e.g. The 16.9mb x-large.epub takes ~40ms whereas the 3.9mb large.epub takes ~100ms.
    """

    # Test with small EPUB (no metrics as of yet)
    epub_process = get_ebook(epub_path, ebook_name)
    return epub_process


if __name__ == "__main__":
    start_time = timeit.default_timer()
    benchmark_process("tests/test-epubs/large.epub", "large")
    print("X-Large2 EPUB Process: ", timeit.default_timer() - start_time)
