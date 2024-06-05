import zipfile
from argparse import ArgumentParser
import os

parser = ArgumentParser()
parser.add_argument("--input_dir",
                    help="dir from which files are moved")
parser.add_argument("--output_dir",
                    help="dir to which files are moved")
args = parser.parse_args()

list_of_patient_firs = os.listdir(args.input_dir)
number_of_patients = len(list_of_patient_firs)

index = 0
for patient_dir in number_of_patients:
    for file_name in os.listdir(args.input_dir + patient_dir):
        if file_name.endswith('.zip'):
            with zipfile.ZipFile(args.input_dir + patient_dir + '/' + file_name, 'r') as zip_ref:
                zip_ref.extractall(args.input_dir + patient_dir + '/')
            print(args.input_dir + patient_dir + '/' + file_name)
    index += 1
    print(f'Done {index} out of {number_of_patients}')
        

