import os

imgsize = 1024
epochs = 1500
batch_size = 4
data_ = "../running_data/linear_globular_dataset_ds9/data.yaml"

weight_tf = "\'\'"
cfg_tf = "models/hub/yolov5n-transformer.yaml"

weight_tf_ori = "yolov5s.pt"
cfg_tf_ori = "yolov5s-transformer.yaml"

weight = "yolov5n6.pt"
cfg = "yolov5n6.yaml"

weight_n = "yolov5n.pt"
cfg_n = "yolov5n.yaml"

hpy = "data/hyps/hyp.manual_augment.yaml"
hpy_wdc = "data/hyps/hyp.manual_augment_wdc.yaml"

# 7 to 3
project_name = "./runs/train/comparison_method/YoDa/no_finetune_3ch"

# YOLO size n 
os.system("python train.py --img {} \
--epochs {} --batch-size 4 \
--data {} \
--sp-filters 0 \
--input-ch 7 --target-ch 3 \
--weights '' --hyp {} --cfg yolov5n.yaml \
--device 0 --exist-ok --patience 0 \
--name yolo5n --project {}".format(imgsize, epochs, data_, hpy, project_name))

# YOLO size s
os.system("python train.py --img {} \
--epochs {} --batch-size 4 \
--data {} \
--sp-filters 0 \
--input-ch 7 --target-ch 3 \
--weights '' --hyp {} --cfg yolov5s.yaml \
--device 0 --exist-ok --patience 0 \
--name yolo5s --project {}".format(imgsize, epochs, data_, hpy, project_name))

# YOLO size m
os.system("python train.py --img {} \
--epochs {} --batch-size 4 \
--data {} \
--sp-filters 0 \
--input-ch 7 --target-ch 3 \
--weights '' --hyp {} --cfg yolov5m.yaml \
--device 0 --exist-ok --patience 0 \
--name yolo5m --project {}".format(imgsize, epochs, data_, hpy, project_name))

# YOLO size l
os.system("python train.py --img {} \
--epochs {} --batch-size 2 \
--data {} \
--sp-filters 0 \
--input-ch 7 --target-ch 3 \
--weights '' --hyp {} --cfg yolov5l.yaml \
--device 0 --exist-ok --patience 0 \
--name yolo5l --project {}".format(imgsize, epochs, data_, hpy, project_name))

# finetuning 
# 7 to 3
project_name = "./runs/train/comparison_method/YoDa/finetune_3ch"

# YOLO size n 
os.system("python train.py --img {} \
--epochs {} --batch-size 4 \
--data {} \
--sp-filters 0 \
--input-ch 7 --target-ch 3 \
--weights yolov5n.pt --hyp {} --cfg yolov5n.yaml \
--device 0 --exist-ok --patience 0 \
--name yolo5n --project {}".format(imgsize, epochs, data_, hpy, project_name))

# YOLO size s
os.system("python train.py --img {} \
--epochs {} --batch-size 4 \
--data {} \
--sp-filters 0 \
--input-ch 7 --target-ch 3 \
--weights yolov5s.pt --hyp {} --cfg yolov5s.yaml \
--device 0 --exist-ok --patience 0 \
--name yolo5s --project {}".format(imgsize, epochs, data_, hpy, project_name))

# YOLO size m
os.system("python train.py --img {} \
--epochs {} --batch-size 4 \
--data {} \
--sp-filters 0 \
--input-ch 7 --target-ch 3 \
--weights yolov5m.pt --hyp {} --cfg yolov5m.yaml \
--device 0 --exist-ok --patience 0 \
--name yolo5m --project {}".format(imgsize, epochs, data_, hpy, project_name))

# YOLO size l
os.system("python train.py --img {} \
--epochs {} --batch-size 2 \
--data {} \
--sp-filters 0 \
--input-ch 7 --target-ch 3 \
--weights yolov5l.pt --hyp {} --cfg yolov5l.yaml \
--device 0 --exist-ok --patience 0 \
--name yolo5l --project {}".format(imgsize, epochs, data_, hpy, project_name))
