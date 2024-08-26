```
python pymerge-md "source/file/path" "new_file_name.md"
```

returns a *new_file_name.md* file with the content of all the files listed as links in *"▫️ some_index_name.md"*. This is specifically designed for my vault structure, of which i leave an example here.

```
╰─$ tree                                                                                        127 ↵
.
├── ▫️  elettrostatica.md
└── ▫️  nts
    ├── campo elettrico.md
    ├── capacita' di un conduttore.md
    ├── circuitazione.md
    ├── circuiti rc.md
    ├── condensatori.md
    ...
```

order in which content of files is appended into the main one is dictated by the order in the index file.