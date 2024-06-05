import os
from argparse import ArgumentParser
import shutil


def create_x_digit_number(number):
    numberStr = str(number)
    assert number >= 0, f'create_x_digit_number function: number: {number} should be positive'

    while len(numberStr) < 3:
        numberStr = '0' + numberStr
    return numberStr

parser = ArgumentParser()
parser.add_argument("--input_dir",
                    help="dir from which files are moved")
parser.add_argument("--output_dir",
                    help="dir to which files are moved")
parser.add_argument("--file_prefix", default='DatasetSample',
                    help="Prefix used for all files to which patient ID will be apended")
parser.add_argument("--create_labels",
                    action="store_true", default=False,
                    help="Dont add channel info after ID")

args = parser.parse_args()

list_of_dirs = os.listdir(args.input_dir)
number_of_patients = len(list_of_dirs)
patient_id = 0
for name in list_of_dirs:
    # TODO
    # 1. add an option to add channels
    if args.create_labels:
        shutil.copy(os.path.join(args.input_dir, name), os.path.join(args.output_dir, args.file_prefix + '_' + create_x_digit_number(patient_id) + '.nii' + os.path.splitext(name)[1]))
    else:
        shutil.copy(os.path.join(args.input_dir, name), os.path.join(args.output_dir, args.file_prefix + '_' + create_x_digit_number(patient_id) + '_' + '0000' + '.nii' + os.path.splitext(name)[1]))
    patient_id += 1
    print(f'Done {patient_id} out of {number_of_patients}')