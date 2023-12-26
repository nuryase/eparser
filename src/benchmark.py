import timeit
from auxiliary import create_ebook_from_path


def benchmark_full_process():
    """
    Benchmarks the entire unzipping, extraction, and parsing process.
    """
    full_process = create_ebook_from_path("tests/test.epub", "test")
    return full_process


if __name__ == "__main__":
    start_time = timeit.default_timer()
    full_procces = benchmark_full_process()
    print("Full Process: ", timeit.default_timer() - start_time)
