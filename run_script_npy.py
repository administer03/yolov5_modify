import os

imgsize = 1024
epochs = 1
batch_size = 1
data_ = "../npy_dataset/data.yaml"
hpy_aug = "../npy_dataset/hyp.manual_augment.yaml"
hpy_no_aug = "../npy_dataset/hyp.no_augment.yaml"


'''
No Augmentations
'''

project_name = "./runs/train/npy_version/no_augment"


os.system("python train.py --img {} \
--epochs {} --batch-size {} \
--data {} \
--input-ch 7 --target-ch 1 \
--weights '' --hyp {} --cfg yolov5n.yaml \
--device 0 \
--exist-ok --patience 0 \
--name scratch_5n --project {}".format(imgsize, epochs, batch_size, data_, hpy_no_aug, project_name))

# os.system("python train.py --img {} \
# --epochs {} --batch-size {} \
# --data {} \
# --input-ch 7 --target-ch 3 \
# --weights '' --hyp {} --cfg yolov5s.yaml \
# --device 0 --exist-ok --patience 0 \
# --name scratch_5s --project {}".format(imgsize, epochs, batch_size, data_, hpy_no_aug, project_name))

# os.system("python train.py --img {} \
# --epochs {} --batch-size {} \
# --data {} \
# --input-ch 7 --target-ch 3 \
# --weights '' --hyp {} --cfg yolov5m.yaml \
# --device 0 --exist-ok --patience 0 \
# --name scratch_5m --project {}".format(imgsize, epochs, batch_size, data_, hpy_no_aug, project_name))



# '''
# With Augmentations
# '''

# project_name = "./runs/train/npy_version_YoDa3ch/augment"

# os.system("python train.py --img {} \
# --epochs {} --batch-size {} \
# --data {} \
# --input-ch 7 --target-ch 3 \
# --weights '' --hyp {} --cfg yolov5n.yaml \
# --device 0 --exist-ok --patience 0 \
# --name scratch_5n --project {}".format(imgsize, epochs, batch_size, data_, hpy_aug, project_name))

# os.system("python train.py --img {} \
# --epochs {} --batch-size {} \
# --data {} \
# --input-ch 7 --target-ch 3 \
# --weights '' --hyp {} --cfg yolov5s.yaml \
# --device 0 --exist-ok --patience 0 \
# --name scratch_5s --project {} --resume".format(imgsize, epochs, batch_size, data_, hpy_aug, project_name))

# os.system("python train.py --img {} \
# --epochs {} --batch-size {} \
# --data {} \
# --input-ch 7 --target-ch 3 \
# --weights '' --hyp {} --cfg yolov5m.yaml \
# --device 0 --exist-ok --patience 0 \
# --name scratch_5m --project {}".format(imgsize, epochs, batch_size, data_, hpy_aug, project_name))
