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
# --name cnn_extraction_out1ch_n6".format(imgsize, epochs, data_, weight, hpy, cfg))

# # -------- sp_filters --------

# os.system("python train.py --img {} \
# --epochs {} --batch-size 8 \
# --data {} \
# --sp-filters 1 \
# --input-ch 3 --target-ch 1 \
# --weights {} --hyp {} --cfg {} \
# --device 0 --exist-ok --patience 0 \
# --name LinearSqrtSquared_n6".format(imgsize, epochs, data_, weight, hpy, cfg))

# os.system("python train.py --img {} \
# --epochs {} --batch-size 8 \
# --data {} \
# --sp-filters 2 \
# --input-ch 3 --target-ch 1 \
# --weights {} --hyp {} --cfg {} \
# --device 0 --exist-ok --patience 0 \
# --name LogASINHSqrt_n6".format(imgsize, epochs, data_, weight, hpy, cfg))

# os.system("python train.py --img {} \
# --epochs {} --batch-size 8 \
# --data {} \
# --sp-filters 3 \
# --input-ch 3 --target-ch 1 \
# --weights {} --hyp {} --cfg {} \
# --device 0 --exist-ok --patience 0 \
# --name PowerSINHSquared_n6".format(imgsize, epochs, data_, weight, hpy, cfg))

## for testing

# os.system("python train.py --img 32 \
# --epochs 2 --batch-size 4 \
# --data ../running_data/linear_globular_dataset_ds9/data.yaml \
# --sp-filters 0 \
# --input-ch 7 --target-ch 3 \
# --weights '' --hyp data/hyps/hyp.manual_augment.yaml --cfg models/hub/yolov5n-transformer.yaml \
# --device 0 --exist-ok --patience 0 \
# --name testing")
          
# ----- sp_filters          
# os.system("python train.py --img 64 \
# --epochs 1 --batch-size 4 \
# --data ../running_data/linear_globular_dataset_ds9/data.yaml \
# --sp-filters 2 \
# --input-ch 3 --target-ch 1 \
# --weights '' --hyp data/hyps/hyp.manual_augment.yaml --cfg models/hub/yolov5n-transformer.yaml \
# --device 0 --exist-ok --patience 0 \
# --name testing")
