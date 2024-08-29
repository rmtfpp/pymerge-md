import sys
import os
import re
from pathlib import Path

def append_after_third_delimiter(source_file, destination_file):
    with open(source_file, 'r', encoding='utf-8') as src:
        source_content = src.read()
    
    parts = source_content.split('---')
    
    if len(parts) > 3:
        content_to_append = parts[3].strip()
        
        with open(destination_file, 'a', encoding='utf-8') as dest:
            dest.write(f"### {str(source_file)[str(source_file).rfind('/') + 1:-3]}\n\n{content_to_append}\n\n---\n\n")
    else:
        print("source file hasnt enough delimiters.")


def append_after_third_delimiter_fake(source_file, destination_file):

    with open(source_file, 'r', encoding='utf-8') as src:
        source_content = src.read()
    
    with open(destination_file, 'r', encoding='utf-8') as dest:
        destination_content = dest.read()

    delimiter = '---'
    delimiter_count = 0
    insert_position = 0
    for i, line in enumerate(destination_content.splitlines(True)):
        if delimiter in line:
            delimiter_count += 1
        if delimiter_count == 3:
            insert_position = sum(len(l) for l in destination_content.splitlines(True)[:i+1])
            break
    
    if delimiter_count < 3:
        insert_position = len(destination_content)

    new_content = destination_content[:insert_position] + source_content + destination_content[insert_position:]

    with open(destination_file, 'w', encoding='utf-8') as dest:
        dest.write(new_content)


def main():

    path = sys.argv[1]
    filename = sys.argv[2]
    path = Path(path)
    markdown_file = [x for x in path.iterdir() if x.is_dir() == False and str(x)[-3:] == ".md" and str(x).find("▫️") != -1]
    assert os.path.exists(path) and len(markdown_file) == 1, "enter a valid path with a single markdown file in it"


    markdown_indexfile_path = markdown_file[0]

    with open(markdown_indexfile_path, "r") as guide:
        guide_string = guide.read()

        matches = re.findall(r"\[\[([\w\sÀ-ÖØ-öø-ÿ']+)\]\]", guide_string)

    guide.close()

    filepath = Path(os.path.join(path, filename))
    filepath.touch()

    for m in matches:
        m = m + ".md"
        print(m)
        m_path = Path(os.path.join(path, "▫️ nts", m))
        if m_path.is_file():
            append_after_third_delimiter(m_path, filepath)
        else:
            print(f"file {m} not found, skipped")


if __name__ == "__main__":
    main()