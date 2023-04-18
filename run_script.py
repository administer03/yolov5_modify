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

project_name = "./runs/train/mosaic_tf_sizen"

# os.system("python train.py --img {} \
# --epochs {} --batch-size 4 \
# --data {} \
# --input-ch 7 --target-ch 3 \
# --weights {} --hyp {} --cfg {} \
# --device 0 --exist-ok --patience 0 \
# --name cnn_extraction_out3ch_n6".format(imgsize, epochs, data_, weight, hpy, cfg))

# os.system("python train.py --img {} \
# --epochs {} --batch-size 4 \
# --data {} \
# --input-ch 7 --target-ch 1 \
# --weights {} --hyp {} --cfg {} \
# --device 0 --exist-ok --patience 0 \
# --name cnn_n_nopre --project {}".format(imgsize, epochs, data_, weight_tf, hpy, cfg_tf, project_name))

# os.system("python train.py --img {} \
# --epochs {} --batch-size 4 \
# --data {} \
# --input-ch 7 --target-ch 1 \
# --weights {} --hyp {} --cfg {} \
# --device 0 --exist-ok --patience 0 \
# --name cnn_s_pre_mosaic --project {}".format(imgsize, epochs, data_, weight_tf_ori, hpy, cfg_tf_ori, project_name))

# # -------- sp_filters --------

# os.system("python train.py --img {} \
# --epochs {} --batch-size 8 \
# --data {} \
# --sp-filters 1 \
# --input-ch 3 --target-ch 1 \
# --weights {} --hyp {} --cfg {} \
# --device 0 --exist-ok --patience 0 \
# --name LinearSqrtSquared_n6_2 --project {}".format(imgsize, epochs, data_, weight, hpy, cfg, project_name))


# os.system("python train.py --img {} \
# --epochs {} --batch-size 8 \
# --data {} \
# --sp-filters 2 \
# --input-ch 3 --target-ch 1 \
# --weights {} --hyp {} --cfg {} \
# --device 0 --exist-ok --patience 0 \
# --name LogASINHSqrt_n6 --project {}".format(imgsize, epochs, data_, weight, hpy_wdc, cfg, project_name))

# os.system("python train.py --img {} \
# --epochs {} --batch-size 8 \
# --data {} \
# --sp-filters 2 \
# --input-ch 3 --target-ch 1 \
# --weights '' --hyp {} --cfg {} \
# --device 0 --exist-ok --patience 0 \
# --name LogASINHSqrt_tf_n --project {}".format(imgsize, epochs, data_, hpy_wdc, cfg_tf, project_name))

# os.system("python train.py --img {} \
# --epochs {} --batch-size 8 \
# --data {} \
# --sp-filters 2 \
# --input-ch 3 --target-ch 1 \
# --weights {} --hyp {} --cfg {} \
# --device 0 --exist-ok --patience 0 \
# --name LogASINHSqrt_tf_pre_s --project {}".format(imgsize, epochs, data_, weight_tf_ori, hpy_wdc, cfg_tf_ori, project_name))


## for testing

# os.system("python train.py --img 1024 \
# --epochs 1 --batch-size 8 \
# --data ../running_data/linear_globular_dataset_ds9/data.yaml \
# --sp-filters 2 \
# --input-ch 3 --target-ch 1 \
# --weights yolov5n6.pt --hyp data/hyps/hyp.manual_augment.yaml --cfg yolov5n6.yaml \
# --device 0 --exist-ok --patience 0 \
# --name testing --project ./runs/train/test1")
          
# ----- sp_filters          
       
# os.system("python train.py --img 1024 \
# --epochs 1 --batch-size 8 \
# --data ../running_data/linear_globular_dataset_ds9/data.yaml \
# --sp-filters 1 \
# --input-ch 3 --target-ch 1 \
# --weights '' --hyp data/hyps/hyp.manual_augment.yaml --cfg models/hub/yolov5n-transformer.yaml \
# --device 0 --exist-ok --patience 0 \
# --name testing --project ./runs/train/test1")

# ------- Mosaic with tf
project_name = "./runs/train/mosaic_tf_size_n"

# 7 to 3
os.system("python train.py --img {} \
--epochs {} --batch-size 4 \
--data {} \
--input-ch 7 --target-ch 3 \
--weights {} --hyp {} --cfg {} \
--device 0 --exist-ok --patience 0 \
--name cnn_extraction_out3ch --project {}".format(imgsize, epochs, data_, weight_tf, hpy, cfg_tf, project_name))

# 7 to 1
os.system("python train.py --img {} \
--epochs {} --batch-size 4 \
--data {} \
--input-ch 7 --target-ch 1 \
--weights {} --hyp {} --cfg {} \
--device 0 --exist-ok --patience 0 \
--name cnn_extraction_out1ch --project {}".format(imgsize, epochs, data_, weight_tf, hpy, cfg_tf, project_name))

# # -------- sp_filters --------

os.system("python train.py --img {} \
--epochs {} --batch-size 8 \
--data {} \
--sp-filters 1 \
--input-ch 3 --target-ch 1 \
--weights {} --hyp {} --cfg {} \
--device 0 --exist-ok --patience 0 \
--name LinearSqrtSquared --project {}".format(imgsize, epochs, data_, weight_tf, hpy, cfg_tf, project_name))


os.system("python train.py --img {} \
--epochs {} --batch-size 8 \
--data {} \
--sp-filters 2 \
--input-ch 3 --target-ch 1 \
--weights {} --hyp {} --cfg {} \
--device 0 --exist-ok --patience 0 \
--name LogASINHSqrt --project {}".format(imgsize, epochs, data_, weight_tf, hpy, cfg_tf, project_name))

os.system("python train.py --img {} \
--epochs {} --batch-size 8 \
--data {} \
--sp-filters 3 \
--input-ch 3 --target-ch 1 \
--weights {} --hyp {} --cfg {} \
--device 0 --exist-ok --patience 0 \
--name PowerSINHSquared --project {}".format(imgsize, epochs, data_, weight_tf, hpy, cfg_tf, project_name))

# ------- Mosaic with n
project_name = "./runs/train/mosaic_size_n"

# 7 to 3
os.system("python train.py --img {} \
--epochs {} --batch-size 4 \
--data {} \
--input-ch 7 --target-ch 3 \
--weights {} --hyp {} --cfg {} \
--device 0 --exist-ok --patience 0 \
--name cnn_extraction_out3ch --project {}".format(imgsize, epochs, data_, weight_n, hpy, cfg_n, project_name))

# 7 to 1
os.system("python train.py --img {} \
--epochs {} --batch-size 4 \
--data {} \
--input-ch 7 --target-ch 1 \
--weights {} --hyp {} --cfg {} \
--device 0 --exist-ok --patience 0 \
--name cnn_extraction_out1ch --project {}".format(imgsize, epochs, data_, weight_n, hpy, cfg_n, project_name))

# # -------- sp_filters --------

os.system("python train.py --img {} \
--epochs {} --batch-size 8 \
--data {} \
--sp-filters 1 \
--input-ch 3 --target-ch 1 \
--weights {} --hyp {} --cfg {} \
--device 0 --exist-ok --patience 0 \
--name LinearSqrtSquared --project {}".format(imgsize, epochs, data_, weight_n, hpy, cfg_n, project_name))


os.system("python train.py --img {} \
--epochs {} --batch-size 8 \
--data {} \
--sp-filters 2 \
--input-ch 3 --target-ch 1 \
--weights {} --hyp {} --cfg {} \
--device 0 --exist-ok --patience 0 \
--name LogASINHSqrt --project {}".format(imgsize, epochs, data_, weight_n, hpy, cfg_n, project_name))

os.system("python train.py --img {} \
--epochs {} --batch-size 8 \
--data {} \
--sp-filters 3 \
--input-ch 3 --target-ch 1 \
--weights {} --hyp {} --cfg {} \
--device 0 --exist-ok --patience 0 \
--name PowerSINHSquared --project {}".format(imgsize, epochs, data_, weight_n, hpy, cfg_n, project_name))