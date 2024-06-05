# start docker service
sudo service docker start

# activate env
cd $HOME/doktorat/nnUnetDocker
source ~/miniconda3/etc/profile.d/conda.sh # this one is needed to run next command in bash file
conda activate pypy

# setup env variables
export DOCKER_NAME=unet3d_mlcommons_lits
export DOKTORAT_PATH=/home/kamkac/doktorat/
export IMAGE_SEGM_PATH=/home/kamkac/doktorat/mlcommons/training/image_segmentation/pytorch/
export SMALL_LITS_PATH=/home/kamkac/doktorat/lits_smaller/

# delete docker if it's already running
docker stop $DOCKER_NAME | xargs docker rm

# create docker
docker run -td \
    -v $DOKTORAT_PATH:/root/doktorat \
    -v $SMALL_LITS_PATH:/root/small_lits \
    -v $IMAGE_SEGM_PATH:/root/image_segmentation/pytorch \
    --gpus all \
    --shm-size 8G \
    --name $DOCKER_NAME nnunet:base 

# get inside the running docker
docker exec -it $DOCKER_NAME bash
