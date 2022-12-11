import zipfile
import sys
import time


def main():
    start_time = time.time()
    if len(sys.argv) < 2:
        print("Usage: python main.py <zipfile>")
        return

    file = sys.argv[1]
    unzip = sys.argv[2] == '-u' if len(sys.argv) > 2 else None

    if unzip:
        try:
            extract_zip(file)
        except zipfile.BadZipFile:
            print("Not a valid zip file")
    else:
        try:
            zip_file(file)
        except FileNotFoundError:
            print("File not found")

    print(f"--- {time.time() - start_time} seconds ---")


def extract_zip(zip_file):
    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall("./temp")


def zip_file(file):
    with zipfile.ZipFile(f"{file}.zip", "w", compresslevel=9) as zip_ref:
        zip_ref.write(file)


if __name__ == "__main__":
    main()
