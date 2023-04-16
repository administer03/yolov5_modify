import os

imgsize = 1024
epochs = 1500
batch_size = 4
data_ = "../running_data/linear_globular_dataset_ds9/data.yaml"
# weight = ""
# cfg = "models/hub/yolov5n-transformer.yaml"
weight = "yolov5n6.pt"
cfg = "yolov5n6.yaml"
hpy = "data/hyps/hyp.manual_augment.yaml"

project_name = "./runs/val/test1"

## for testing

os.system("python val.py --img {} \
--batch-size 8 \
--data {} \
--sp-filters 1 \
--weights ./runs/train/n6_v2/LogASINHSqrt_n6_2/weights/best.pt \
--device 0 --exist-ok \
--name val1 --project {}".format(imgsize, data_, project_name))
          