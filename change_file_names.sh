#!/bin/bash
set -xe
dir=$1
is_training_sample=$2

if [ $is_training_sample ]; then
    channel='_0000'
fi

idx=0
for f in "$dir"/*; do
    if (( idx < 10 )); then
        file_idx=00"$idx"
    elif (( idx < 100 )); then
        file_idx=0"$idx"
    else
        file_idx="$idx"
    fi
    mv $f $dir/Dircadb_"$file_idx"$channel.nii.gz
    idx=$((idx+1));
done
