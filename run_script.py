import os

os.system("python train.py --img 256 \
--epochs 1 --batch-size 4 \
--data ../running_data/linear_globular_dataset_ds9/data.yaml \
--input-ch 7 --target-ch 1 \
--weights '' --hyp data/hyps/hyp.manual_augment.yaml --cfg models/hub/yolov5n-transformer.yaml \
--device 0 --exist-ok --patience 0 \
--name test")
