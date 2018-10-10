# author: Steven Lakin
# date: Oct 5, 2018
# purpose: takes as input FASTQ file and outputs something


import argparse
import sys


# Functions
def parse_fastq(filepath):
    return_values = []
    with open(filepath, 'r') as f:
        data = f.read().split('\n')
        for line in data:
            if not line:
                continue
            # if working with delimited file
            # entries = line.split(',') or entries = line.split('\t')
            if line[0:3] == '@M0':
                read_name = line[1:]
                return_values.append(read_name)
    return return_values


def parse_fastq2(filepath):
    return_values = {}
    with open(filepath, 'r') as f:
        while True:
            read_name = f.readline()[1:].strip('\n')
            base_pairs = f.readline().strip('\n')
            f.readline()
            quality_scores = f.readline().strip('\n')
            if not read_name or not base_pairs or not quality_scores:
                break
            return_values.setdefault(read_name, [base_pairs, quality_scores])
    return return_values


def write_fasta(read_pair_dictionary):
    for read_name, values in read_pair_dictionary.items():
        # FASTA format: 2 lines, header starts with >, value on second line
        sys.stdout.write('>{}\n{}\n'.format(read_name, values[0]))


# Arguments
parser = argparse.ArgumentParser('parse_fastq.py')  # create argparse object
parser.add_argument('file_path', type=str, help='Path to file for input')


if __name__ == '__main__':
    args = parser.parse_args()
    fastq_file_path = args.file_path
    read_dictionary = parse_fastq2(fastq_file_path)
    write_fasta(read_dictionary)
