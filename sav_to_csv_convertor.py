import pyreadstat

def convert_sav_to_csv(input_file):
    try:
        df, meta = pyreadstat.read_sav(input_file)
        output_file = input_file.replace('.sav', '.csv')
        df.to_csv(output_file, index=False)
        print(f"Conversion successful. CSV file saved as '{output_file}'")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python sav_to_csv_converter.py input.sav")
    else:
        input_file = sys.argv[1]
        convert_sav_to_csv(input_file)
