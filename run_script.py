import os

# os.system("python train.py --img 1024 \
# --epochs 1000 --batch-size 4 \
# --data ../running_data/linear_globular_dataset_ds9/data.yaml \
# --input-ch 7 --target-ch 3 \
# --weights '' --hyp data/hyps/hyp.manual_augment.yaml --cfg models/hub/yolov5n-transformer.yaml \
# --device 0 --exist-ok --patience 0 \
# --name cnn_extraction_out3ch")
          
# os.system("python train.py --img 1024 \
# --epochs 1500 --batch-size 4 \
# --data ../running_data/linear_globular_dataset_ds9/data.yaml \
# --input-ch 7 --target-ch 1 \
# --weights '' --hyp data/hyps/hyp.manual_augment.yaml --cfg models/hub/yolov5n-transformer.yaml \
# --device 0 --exist-ok --patience 0 \
# --name cnn_extraction_out1ch")


## for testing

# os.system("python train.py --img 64 \
# --epochs 1 --batch-size 4 \
# --data ../running_data/linear_globular_dataset_ds9/data.yaml \
# --sp-filters 0 \
# --input-ch 7 --target-ch 3 \
# --weights '' --hyp data/hyps/hyp.manual_augment.yaml --cfg models/hub/yolov5n-transformer.yaml \
# --device 0 --exist-ok --patience 0 \
# --name testing")
          
# ----- sp_filters          
os.system("python train.py --img 64 \
--epochs 1 --batch-size 4 \
--data ../running_data/linear_globular_dataset_ds9/data.yaml \
--sp-filters 2 \
--input-ch 3 --target-ch 1 \
--weights '' --hyp data/hyps/hyp.manual_augment.yaml --cfg models/hub/yolov5n-transformer.yaml \
--device 0 --exist-ok --patience 0 \
--name testing")
