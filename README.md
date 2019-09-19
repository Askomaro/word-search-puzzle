# word-search-puzzle
Implementation word search puzzle

Main idea is to use compact prefix tree as data structure to store all possible words and then find needed words.
Implementation has been taken from another my repository -> https://github.com/Askomaro/python_trie 

Performance: this realization for board 15x15 takes ~ 200 ms 

##How to use it:
1. Clone repository
2. Install dependencies into virtual environment:
```pip install -r requirements.txt```
3. In order to get knoweledge about existed CLI parameters, use next:
```
python3 main.py --help
Usage: main.py [OPTIONS]

Options:
  --i INTEGER       Number of rows.
  --j INTEGER       Number of elements in a row.
  --file_name TEXT  Name of file with words.
  --help            Show this message and exit.

```

to run unit tests, use next command:
```
pytest tests/
```