# Script to change dicom files into nifti
# Uses dicom2nifti but because it merges all files in a dir 
# we first copy each file to seperate dir and then use the tool
# after that we remove

import os
import dicom2nifti
from time import sleep
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--input_dir",
                    help="dir from which files are moved")
parser.add_argument("--output_dir",
                    help="dir to which files are moved")
args = parser.parse_args()

os.makedirs(args.output_dir + '/' + 'imagesTr/', exist_ok=True)
os.makedirs(args.output_dir + '/' + 'imagesTs/', exist_ok=True)
os.makedirs(args.output_dir + '/' + 'labelsTr/', exist_ok=True)

training_output_dir = args.output_dir + '/' + 'imagesTr/'
labels_output_dir = args.output_dir + '/' + 'labelsTr/'

list_of_patient_dirs = os.listdir(args.input_dir)
number_of_patients = len(list_of_patient_dirs)
index=0
for dir_name in list_of_patient_dirs:
    tr_patient_data_dir = args.input_dir + '/' + dir_name + '/' + 'PATIENT_DICOM/'
    dicom2nifti.dicom_series_to_nifti(tr_patient_data_dir, training_output_dir+str(index))
    label_patient_data_dir = args.input_dir + '/' + dir_name + '/' + 'MASKS_DICOM/liver/'
    dicom2nifti.dicom_series_to_nifti(label_patient_data_dir, labels_output_dir+str(index))
    index += 1
    print(f'Done: {index} out of {number_of_patients}')
