import sys
import os
import re
from pathlib import Path

def main():

    path = sys.argv[1]
    filename = sys.argv[2]
    path = Path(path)
    markdown_file = [x for x in path.iterdir() if x.is_dir() == False and str(x)[-3:] == ".md" and str(x).find("▫️") != -1]
    assert os.path.exists(path) and len(markdown_file) == 1, "enter a valid path with a single markdown file in it"

    filepath = Path(os.path.join(path, filename))
    open(filepath, "x")
    F = open(filepath, "a")

    markdown_indexfile_path = markdown_file[0]

    with open(markdown_indexfile_path, "r") as guide:
        guide_string = guide.read()

        matches = re.findall(r"\[\[([A-Za-z0-9_ ]+)\]\]", guide_string)

    for m in matches:
        print(m)

    guide.close()



if __name__ == "__main__":
    main()