import os

imgsize = 1024
epochs = 1500
batch_size = 4
data_ = "../running_data/npy_dataset/data.yaml"
hpy_aug = "../running_data/npy_dataset/hyp.manual_augment.yaml"
hpy_no_aug = "../running_data/npy_dataset/hyp.no_augment.yaml"


'''
No Augmentations
'''

project_name = "./runs/train/npy_version/no_augment"

os.system("python train.py --img {} \
--epochs {} --batch-size {} \
--data {} \
--input-ch 7 --target-ch 1 \
--weights '' --hyp {} --cfg yolov5n.yaml \
--device 0 --exist-ok --patience 0 \
--name scratch_5n --project {}".format(imgsize, epochs, batch_size, data_, hpy_no_aug, project_name))

os.system("python train.py --img {} \
--epochs {} --batch-size {} \
--data {} \
--input-ch 7 --target-ch 1 \
--weights '' --hyp {} --cfg yolov5s.yaml \
--device 0 --exist-ok --patience 0 \
--name scratch_5s --project {}".format(imgsize, epochs, batch_size, data_, hpy_no_aug, project_name))

os.system("python train.py --img {} \
--epochs {} --batch-size {} \
--data {} \
--input-ch 7 --target-ch 1 \
--weights '' --hyp {} --cfg yolov5m.yaml \
--device 0 --exist-ok --patience 0 \
--name scratch_5m --project {}".format(imgsize, epochs, batch_size, data_, hpy_no_aug, project_name))



'''
With Augmentations
'''

project_name = "./runs/train/npy_version/augment"

os.system("python train.py --img {} \
--epochs {} --batch-size {} \
--data {} \
--input-ch 7 --target-ch 1 \
--weights '' --hyp {} --cfg yolov5n.yaml \
--device 0 --exist-ok --patience 0 \
--name scratch_5n --project {}".format(imgsize, epochs, batch_size, data_, hpy_aug, project_name))

os.system("python train.py --img {} \
--epochs {} --batch-size {} \
--data {} \
--input-ch 7 --target-ch 1 \
--weights '' --hyp {} --cfg yolov5s.yaml \
--device 0 --exist-ok --patience 0 \
--name scratch_5s --project {}".format(imgsize, epochs, batch_size, data_, hpy_aug, project_name))

os.system("python train.py --img {} \
--epochs {} --batch-size {} \
--data {} \
--input-ch 7 --target-ch 1 \
--weights '' --hyp {} --cfg yolov5m.yaml \
--device 0 --exist-ok --patience 0 \
--name scratch_5m --project {}".format(imgsize, epochs, batch_size, data_, hpy_aug, project_name))
