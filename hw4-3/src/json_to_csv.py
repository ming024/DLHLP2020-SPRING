import argparse
import json

def main(input_file, output_file):
    predictions = json.load(open(input_file, 'r'))
    with open(output_file, 'w') as f:
        f.write('ID,Answer\n')
        for key, value in predictions.items():
            f.write(f'{key}, {value.replace(",", "")}\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type=str)
    parser.add_argument('output_file', type=str)
    main(**vars(parser.parse_args()))