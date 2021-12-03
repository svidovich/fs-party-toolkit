import argparse
import csv

from typing import List, Tuple


def mkpairs(file_path: str) -> List[Tuple[str]]:
    with open(file_path, 'r') as file_handle:
        reader = csv.reader(file_handle, delimeter="\t")
    header = next(reader)
    print(header)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--responses-file',
        required=True,
        help='The file containing survery responses, TSV formatted')

    args = parser.parse_args()
    mkpairs(args.responses_file)


if __name__ == '__main__':
    main()
