# nnU-netv2-dataset-preperation-scripts
Scripts to prepare 3d-ircadb-01 dataset for nnUnet & an example how to run it using the dataset.

## Dataset used
Dataset used was: https://www.ircad.fr/research/data-sets/liver-segmentation-3d-ircadb-01/ which uses dicom files. The scripts are ment to be used on that dataset structure so there will be needed modifications to use it on different dicom datasets.

## Environment 
To use conda please refer to: https://conda.io/projects/conda/en/latest/user-guide/install/index.html

To create conda env run:
```
conda env create -f environment.yml
```

To create docker run:
```
docker build -t nnunet:base -f Dockerfile .
```

To get into the docker run:
```
bash docker_nnUnet.sh
```

## Prepare dataset for nnUnet based on 3Dircadb1
Steps below should be done in order to correctly prepare the data

1. To unpack data run:
```
python unzip_files.py --input_dir 3Dircadb1/
```

2. To change dicom files to nifti run:
```
python change_dicom_to_niftis.py --input_dir 3Dircadb1/ --output_dir Dataset012_3Dircadb1Liver
```

3. To change filenames to the structure introduced in https://github.com/MIC-DKFZ/nnUNet/blob/master/documentation/dataset_format.md#dataset-folder-structure run (not advised to use this script at the moment as it changes data precision which destroys the data. Probably related to shutil.copy, one can try to change the method or do it manually):
* Labels:
```
python change_file_names_to_dataset_ids.py --input_dir Dataset012_3Dircadb1Liver/labelsTr/ --output_dir Dataset012_3Dircadb1Liver/labelsTr/ --file_prefix 3Dircadb1 --create_labels
```
    
* Images:
```
python change_file_names_to_dataset_ids.py --input_dir Dataset012_3Dircadb1Liver/imagesTr/ --output_dir Dataset012_3Dircadb1Liver/imagesTr/ --file_prefix 3Dircadb1
```

4. To pack .nii files to .nii.gz run:
```
Dataset012_3Dircadb1Liver/
gzip -v -r imagesT*
gzip -v -r labelsTr
```

5. To create json dataset description one can use generate_dataset_json.py from nnUnet scripts or for 3Dircadb1 just use dataset.json from this repository and modify it for one's use.

6. To change [0, 255] data labes (and occasional [0, 1, 255]) to [0, 1] used by nnUnet run:
```
python change_255labels_to01.py --input_dir Dataset012_3Dircadb1Liver/labelsTr/ --output_dir Dataset012_3Dircadb1Liver/labelsTr/
```

After that dataset will be ready to be used for training using nnUnet and related frameworks

## Running nnUnet
For installation refer to: https://github.com/MIC-DKFZ/nnUNet/blob/master/documentation/installation_instructions.md

After installation export paths to be used in nnunet assuming that nnUnet_raw is place where Dataset012_3Dircadb1Liver is stored after running above scripts:
```
export nnUNet_raw=nnUNet_raw/ 
export nnUNet_results=nnUnet/results
export nnUNet_preprocessed=nnUnet/preprocessed
```

Running nnUnet Experiment planner where -d 012 is index of the Dataset012_3Dircadb1Liver:
```
nnUNetv2_plan_and_preprocess -d 012 -pl nnUNetPlannerResEncM -gpu_memory_target 8 -np 4
```

Running examplary training:
```
nnUNetv2_train 012 2d 1 -p nnUNetResEncUNetMPlans
```