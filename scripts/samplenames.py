# Imports
import sys
import glob
import argparse


# Functions
def get_sample_names(folder_name, number=1):
    return_values = set()
    for file in glob.glob(folder_name + "/*"):   # folder, folder/
        sample_name = '_'.join(file.split('/')[-1].split('_')[0:number])
        return_values.add(sample_name)
    return return_values


# Argument parser
parser = argparse.ArgumentParser("samplename.py")
parser.add_argument("folder", type=str, help="Path to folder of files")
parser.add_argument("-n", "--number", type=int, default=1,
                    help="Number of elements separated by underscores")

# Main code block
if __name__ == "__main__":
    args = parser.parse_args()
    my_folder = args.folder
    for sample in get_sample_names(my_folder, args.number):
        print(sample)
