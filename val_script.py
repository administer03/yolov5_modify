import os

imgsize = 1024
batch_size = 4
data_ = "../running_data/linear_globular_dataset_ds9/data.yaml"
task = "test"
project_name = "./runs/val/test1"
weight_ = "./runs/train/npy_version/augment/scratch_5n/weights/best.pt"

## for testing

os.system("python val.py --img {} \
--batch-size 8 \
--data {} --task {} \
--input-ch 7 --target-ch 1 \
--weights ./runs/train/7_to_1_ch/cnn_s_pre/weights/last.pt \
--device 0 --exist-ok --single-cls \
--name val1 --project {}".format(imgsize, data_, task, project_name))
          