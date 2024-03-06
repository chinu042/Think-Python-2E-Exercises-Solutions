def sed(s, replace_string, input_file, output_file):
    try:
        with open(input_file, 'r') as fin, open(output_file, 'w') as fout:
            # Create translation table
            trans_table = str.maketrans(s, replace_string)

            for line in fin:
                # Translate each line
                new_line = line.translate(trans_table)
                fout.write(new_line)
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")

if __name__ == '__main__':
    sed('p', 'q', 'test.txt', 'output.txt')
