# SAV to CSV Converter

![SPSS Logo](https://upload.wikimedia.org/wikipedia/en/thumb/3/3a/IBM_SPSS_Statistics_logo.svg/200px-IBM_SPSS_Statistics_logo.svg.png)

This Python tool allows you to effortlessly convert SPSS SAV files to CSV format using the `pyreadstat` library.

## Installation

Before using the SAV to CSV Converter, ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

To install the required libraries, simply use `pip`:

```bash
pip install pyreadstat
```

## Usage

1. Download the `sav_to_csv_converter.py` script from this repository.

2. Place your SPSS SAV file (e.g., `input.sav`) in the same directory as the script.

3. Open a terminal or command prompt and navigate to the directory containing the script and your SAV file.

4. Run the following command:

```bash
python sav_to_csv_converter.py input.sav
```

This will swiftly convert the SAV file to CSV format and save it as `input.csv` in the same directory.

## Acknowledgments

This tool relies on the fantastic [pyreadstat](https://github.com/Roche/pyreadstat) library, which provides the capability to read and write data in the SPSS SAV file format.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---