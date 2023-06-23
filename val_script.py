import os

imgsize = 1024
batch_size = 4
data_ = "../npy_dataset/data.yaml"
task = "test"
project_name = "./runs/val/test1"
# weight_ = "./runs/train/npy_version/no_augment/scratch_5n/weights/best.pt"
# weight_ = "../weight/lastn_noaug.pt"
weight_ = "../weight/lastn_aug.pt"

## for testing

os.system("python val.py --img {} \
--batch-size {} \
--data {} --task {} \
--weights {} --save-conf --save-txt \
--device 0 --exist-ok --single-cls \
--name val1 --project {}".format(imgsize, batch_size, data_, task, weight_, project_name))
          