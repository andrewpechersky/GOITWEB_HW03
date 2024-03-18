import argparse
import sys
import shutil
import logging
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(threadName)s %(message)s")


def reader_folder(source: Path, output: Path) -> None:
    logging.info(f"Start process {threading.current_thread()} in {source}")
    for item in source.iterdir():
        if item.is_dir():
            with ThreadPoolExecutor() as executor:
                executor.submit(reader_folder, item, output)
        else:
            copy_file(item, output)


def copy_file(file_path: Path, output: Path) -> None:
    ext = file_path.suffix[1:]
    ext_folder = output / ext
    try:
        ext_folder.mkdir(exist_ok=True, parents=True)
        shutil.copy(file_path, ext_folder / file_path.name)
    except OSError as err:
        logging.error(err)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Sorting folder")
    parser.add_argument("--source", "-s", help="Source folder", required=True)
    parser.add_argument("--output", "-o", help="Output folder", default="dist")

    args = parser.parse_args()
    source = Path(args.source)
    output = Path(args.output)

    with ThreadPoolExecutor() as executor:
        executor.submit(reader_folder, source, output)   # 1 thread?


if __name__ == "__main__":
    main()
