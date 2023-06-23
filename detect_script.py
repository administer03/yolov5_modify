import os

imgsize = 1024
# source = "../big_npy/images"
source = '../npy_dataset/test/images'
project_name = "./runs/detect"
conf_thres = 0.25
iou_thres = 0.45
# weight_ = "../weight/lastn_noaug.pt"
weight_ = "../weight/lastn_aug.pt"

os.system("python detect.py --imgsz {} \
--source {} --conf-thres {} --iou-thres {}  \
--weights {} --save-conf --save-txt \
--device 0 --exist-ok \
--name val1 --project {}".format(imgsize, source, conf_thres, iou_thres, weight_, project_name))