import SimpleITK as sitk
import numpy as np
from argparse import ArgumentParser
import os
import nibabel as nib

parser = ArgumentParser()
parser.add_argument("--input_dir",
                    help="dir from which files are moved")
parser.add_argument("--output_dir",
                    help="dir to which files are moved")

args = parser.parse_args()

for file in os.listdir(args.input_dir):
    # A path to a .nii image:
    t1_fn = args.input_dir + file
    print(f'Converting: {t1_fn}')

    # Read the .nii image containing the volume with SimpleITK:
    try:
        img = nib.load(args.input_dir+file)
    except:
        print(f'ERROR: File {file} not possible to be read by SimpleITK')

    # # and access the numpy array:
    data = img.get_fdata()
    data = data.astype(int)

    #get unique values (expected to get {0, 255} or {0, 1, 255})
    unique_values = np.unique(data)
    print(f'Unique values before: {unique_values}')

    # in a case of {0, 255} change 255 to 1 and in a case of {0, 1, 255}) change 255 to 0
    no_of_unique_values = len(unique_values)
    if no_of_unique_values == 2:
        data[data > 1] = 1
    elif no_of_unique_values == 3:
        data[data > 1] = 0
    else:
        print(f'ERROR: Found {no_of_unique_values} values while expecting 2 or 3. Please check the file: {file}')
    print(f'Unique values after: {np.unique(data)}')

    preprocessed_image = nib.Nifti1Image(data, img.affine, img.header)

    nib.save(preprocessed_image, args.input_dir+file)
    

