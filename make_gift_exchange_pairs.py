import argparse
import csv
import random

from pprint import pprint
from typing import List


def mkpairs(file_path: str) -> List:
    names = list()
    with open(file_path, 'r') as file_handle:
        reader = csv.reader(file_handle, delimiter="\t")
        header: list = next(reader)
        names = list()
        for row in reader:
            names.append({
                'first_name': row[1],
                'last_name': row[2],
                'books': row[3],
                'performance': row[4],
                'music': row[5],
                'visual_art': row[6],
                'movies': row[7],
                'diy': row[8],
                'cooking': row[9],
                'other': row[10],
                'ok_to_receive': row[11],
                'shirts_and_restrictions': row[12],
                'do_not_send': row[13],
            })

        random.shuffle(names)
        classic_method = list()
        for index, name in enumerate(names):
            # If we aren't at the last entry,
            if index != len(names) - 1:
                # the current person sends a gift to the next
                classic_method.append(
                    f"{name['first_name']} {name['last_name']} sends gift to {names[index + 1]['first_name']} {names[index + 1]['last_name']}"
                )
            else:
                classic_method.append(
                    f"{name['first_name']} {name['last_name']} sends gift to {names[0]['first_name']} {names[0]['last_name']}"
                )
        return classic_method


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--responses-file',
        required=True,
        help='The file containing survery responses, TSV formatted')
    parser.add_argument('--output-file',
                        required=False,
                        help='If set, the file to send pairings to.')

    args = parser.parse_args()
    output_file = args.output_file
    output = mkpairs(args.responses_file)
    if output_file:
        with open(output_file, 'w') as file_handle:
            for pairing in output:
                file_handle.write(f'{pairing}\n')
    else:
        for pairing in output:
            print(pairing)


if __name__ == '__main__':
    main()
