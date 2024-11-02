
# File Compression Tool Using Huffman Coding

## Project Overview
This project implements a file compression tool using **Huffman coding**, a lossless data compression algorithm. The tool compresses an arbitrary file by encoding its contents in binary format, significantly reducing its size. Huffman coding is commonly used for data compression in areas where storage efficiency is critical, as it allows frequently used bytes to be represented by shorter binary codes.

## Features
- **Supports Any File Format**: Compresses files in binary format, making it adaptable to any file type.
- **Huffman Encoding**: Utilizes variable-length codes to achieve lossless compression.
- **Binary Output**: Generates a `.huf` compressed file that can later be decompressed using the same Huffman tree.

## Requirements
- **Python 3.x**
- **Required Libraries**: `heapq`, `collections` (both are standard Python libraries)

## How It Works
### Huffman Coding Algorithm
1. **Build Frequency Table**: Reads the file byte-by-byte and counts the frequency of each byte.
2. **Generate Huffman Tree**: Uses a priority queue to create a binary tree where nodes with lower frequencies are closer to the root.
3. **Assign Binary Codes**: Traverses the Huffman tree to assign binary codes to each byte, with shorter codes for more frequent bytes.
4. **Compress Data**: Replaces each byte in the file with its Huffman code and writes this compressed binary data to an output file.

### File Structure
- **`input.txt`**: The file to be compressed.
- **`output.huf`**: The compressed file, storing encoded data in binary format.
- **`codebook.txt`** (optional): If enabled, this file maps each byte to its Huffman code, helping with decompression and debugging.

## Usage
### Running the Code
1. Clone this repository:
   ```bash
   git clone https://github.com/pratikdash07/File-Compression.git
   cd File-Compression
   ```

2. Place the file you wish to compress in the project folder. Name it `input.txt` or change the filename in the code to match your file’s name.

3. Run the compression tool:
   ```bash
   python file_compression.py
   ```

4. After execution, check the project folder for `output.huf` (compressed file) and, optionally, `codebook.txt` (if enabled).

### Example Code
Below is a sample code snippet showing how to set up and use the tool.

```python
from collections import Counter
import heapq

# Define Node and other necessary functions...
# ...

# Example usage
input_path = "input.txt"
output_path = "output.huf"
with open(input_path, 'rb') as f:
    file_data = f.read()

# Step-by-step execution
frequency_table = build_frequency_table(file_data)
root = build_huffman_tree(frequency_table)
codebook = generate_codes(root)
compressed_data = compress_data(file_data, codebook)
write_compressed(output_path, compressed_data)
```

## Results
You should see a significant reduction in the file size for files with repetitive content. To observe the efficiency, compare the sizes of `input.txt` and `output.huf`.

## Future Work
- **Decompression Tool**: Implement a decompression tool to revert `.huf` files back to their original format.
- **Multiple File Formats**: Extend support for specific formats, like `.txt`, `.csv`, or `.json`, with format-specific compression enhancements.
- **Additional Compression Algorithms**: Consider adding support for more advanced algorithms such as LZ77.

## License
This project is licensed under the MIT License.
