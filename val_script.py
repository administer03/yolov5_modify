import os

imgsize = 1024
batch_size = 8
data_ = "../running_data/npy_dataset/data.yaml"
task = "test"
project_name = "./runs/val/test1"
weight_ = "./runs/train/npy_version/augment/scratch_5n/weights/last.pt"

## for testing

os.system("python val.py --img {} \
--batch-size {} \
--data {} --task {} \
--weights {} \
--device 0 --exist-ok --single-cls --save-txt \
--name val1 --project {}".format(imgsize, batch_size, data_, task, weight_, project_name))
          