import os

imgsize = 1024
epochs = 1500
batch_size = 4
data_ = "../running_data/linear_globular_dataset_ds9/data.yaml"
task = "test"
project_name = "./runs/val/test1"

## for testing

os.system("python val.py --img {} \
--batch-size 8 \
--data {} --task {} \
--sp-filters 1 \
--weights ./runs/train/7_to_1_ch/cnn_s_pre/weights/last.pt \
--device 0 --exist-ok --single-cls \
--name val1 --project {}".format(imgsize, data_, task, project_name))
          