import sys
import os
from pathlib import Path

def main():

    path = sys.argv[1]
    path = Path(path)
    assert os.path.exists(path) and len([x for x in path.iterdir() if x.is_dir() == False and str(x)[-3:] == ".md"]) != 0, "enter a valid path with a markdown file in it"

    

if __name__ == "__main__":
    main()