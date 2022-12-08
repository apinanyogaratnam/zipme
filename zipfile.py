import zipfile
import sys


def main():
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


def extract_zip(zip_file):
    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall("./temp")


def zip_file(file):
    with zipfile.ZipFile(f"{file}.zip", "w") as zip_ref:
        zip_ref.write(file)


if __name__ == "__main__":
    main()
