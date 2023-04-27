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

project_name = "./runs/train/tf_s_pretrain"

# # -------- sp_filters --------

os.system("python train.py --img {} \
--epochs {} --batch-size 8 \
--data {} \
--sp-filters 1 \
--input-ch 3 --target-ch 1 \
--weights {} --hyp {} --cfg {} \
--device 0 --exist-ok --patience 0 \
--name LinearSqrtSquared --project {}".format(imgsize, epochs, data_, weight_tf_ori, hpy, cfg_tf_ori, project_name))


os.system("python train.py --img {} \
--epochs {} --batch-size 8 \
--data {} \
--sp-filters 2 \
--input-ch 3 --target-ch 1 \
--weights {} --hyp {} --cfg {} \
--device 0 --exist-ok --patience 0 \
--name LogASINHSqrt --project {}".format(imgsize, epochs, data_, weight_tf_ori, hpy, cfg_tf_ori, project_name))

os.system("python train.py --img {} \
--epochs {} --batch-size 8 \
--data {} \
--sp-filters 3 \
--input-ch 3 --target-ch 1 \
--weights {} --hyp {} --cfg {} \
--device 0 --exist-ok --patience 0 \
--name PowerSINHSquared --project {}".format(imgsize, epochs, data_, weight_tf_ori, hpy, cfg_tf_ori, project_name))


os.system("python train.py --img {} \
--epochs {} --batch-size 4 \
--data {} \
--input-ch 7 --target-ch 3 \
--weights {} --hyp {} --cfg {} \
--device 0 --exist-ok --patience 0 \
--name cnn_extraction_out3ch".format(imgsize, epochs, data_, weight_tf_ori, hpy, cfg_tf_ori))