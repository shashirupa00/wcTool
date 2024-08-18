# ccwc (Custom Character Word Count)

`ccwc` is a custom command-line tool that provides word, line, character, and byte counts for text files. It's inspired by the Unix `wc` command but with some additional features.

## Installation

1. Ensure you have Python 3 installed on your system.
2. Install the required `chardet` library:
   ```
   pip install chardet
   ```
3. Download the `ccwc` script and make it executable:
   ```
   chmod +x ccwc
   ```
4. Optionally, move it to a directory in your PATH for system-wide access:
   ```
   sudo mv ccwc /usr/local/bin/
   ```

## Usage

The basic syntax for using `ccwc` is:

```
ccwc [-mode] <filename>
```

### Modes

- `-c`: Count bytes in the file
- `-l`: Count lines in the file
- `-w`: Count words in the file
- `-m`: Count characters in the file

If no mode is specified, `ccwc` will output the byte count, word count, and line count.

### Examples

1. Count bytes in a file:

   ```
   ccwc -c example.txt
   ```

2. Count words in a file:

   ```
   ccwc -w example.txt
   ```

3. Count lines in a file:

   ```
   ccwc -l example.txt
   ```

4. Count characters in a file:

   ```
   ccwc -m example.txt
   ```

5. Get all counts (bytes, words, lines):
   ```
   ccwc example.txt
   ```

## Features

- Automatically detects file encoding
- Handles various text file formats
- Provides separate modes for different types of counting
- Mimics the basic functionality of the Unix `wc` command

## Error Handling

The script includes basic error handling for common issues such as file not found. If you encounter any problems, make sure the file exists and you have the necessary permissions to read it.
