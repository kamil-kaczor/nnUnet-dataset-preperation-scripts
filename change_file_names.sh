#!/bin/bash
set -xe
dir=$1

idx=0
for f in "$dir"/*; do
    if (( idx < 10 )); then
        file_idx=00"$idx"
    elif (( idx < 100 )); then
        file_idx=0"$idx"
    else
        file_idx="$idx"
    fi
    mv $f $dir/train_"$file_idx"_0000.nii
    idx=$((idx+1));
done
