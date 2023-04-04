import os

os.system("python train.py --img 1024 \
--epochs 1500 --batch-size 4 \
--data ../running_data/linear_globular_dataset_ds9/data.yaml \
--weights '' --hyp data/hyps/hyp.manual_augment.yaml --cfg models/hub/yolov5n-transformer.yaml \
--device 0 --exist-ok --patience 0 \
--name target_1ch")
