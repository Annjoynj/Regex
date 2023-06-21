# Statement Parser

This project is a Python script that extracts transaction information from text statements and converts it into a structured CSV file using regular expressions and pandas.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Statement Parser is a utility script designed to process text statements and extract specific transaction information such as (#codes, sender names, balances, dates, times, and transaction types). It utilizes regular expressions for pattern matching and pandas for data manipulation. The extracted data is then saved as a CSV file for further analysis. This code uses the structure of mpesa messages sent by Safaricom Mpesa but can be modified to fit any set of data

## Features

- Extracts transaction information from text statements using regular expressions.
- Creates a structured DataFrame from the extracted data.
- Saves the extracted data as a CSV file for easy analysis.

## Installation

1. Clone the repository or download the code files.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Ensure that Python and the necessary libraries are installed on your system.

## Usage

1. Place your text statements in a file named "Statements.txt".
2. Run the script using the command `python statement_parser.py`.
3. The extracted transaction information will be saved as a CSV file named "Output.csv".
4. You can find the output file in the same directory as the script.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request following the guidelines outlined in the CONTRIBUTING.md file.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any questions or inquiries, please feel free to contact me at [annjoynjoroge@gmail.com](mailto:annjoynjoroge@gmail.com).
