import os
import shutil
import numpy as np
from sklearn.model_selection import train_test_split

# path to your dataset folder
images_path = 'dataset/images'
labels_path = 'dataset/labels'

# get a list of image and label filenames
image_filenames = np.array(sorted(os.listdir(images_path)))
label_filenames = np.array(sorted(os.listdir(labels_path)))

# ensure the labels correspond to the images
assert np.all([img_fname.split('.')[0] == lbl_fname.split('.')[0] for img_fname, lbl_fname in zip(image_filenames, label_filenames)])

# split dataset into train and test sets
train_images, test_images, train_labels, test_labels = train_test_split(image_filenames, label_filenames, test_size=0.2, random_state=42)

# create directories for train and test datasets
os.makedirs('train_images/images/train', exist_ok=True)
os.makedirs('train_images/labels/train', exist_ok=True)
os.makedirs('train_images/images/val', exist_ok=True)
os.makedirs('train_images/labels/val', exist_ok=True)

# define a function to copy files
def copy_files(src_dir, dst_dir, filenames):
    for filename in filenames:
        src_file = os.path.join(src_dir, filename)
        dst_file = os.path.join(dst_dir, filename)
        shutil.copy(src_file, dst_file)

# copy files
copy_files(images_path, 'train_images/images/train', train_images)
copy_files(labels_path, 'train_images/labels/train', train_labels)
copy_files(images_path, 'train_images/images/val', test_images)
copy_files(labels_path, 'train_images/labels/val', test_labels)