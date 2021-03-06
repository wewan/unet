from __future__ import print_function

import os
import numpy as np

from scipy import misc

data_original_path = '/opt/day2/'
data_creation_path = ''

image_rows = 1024
image_cols = 1024


def create_train_data():
    train_data_path = os.path.join(data_original_path, 'train_jsrt')
    images = os.listdir(train_data_path)
    total = len(images) / 2

    imgs = np.ndarray((total, 1, image_rows, image_cols), dtype=np.uint8)
    imgs_mask = np.ndarray((total, 1, image_rows, image_cols), dtype=np.uint8)

    i = 0
    print('-'*30)
    print('Creating training images...')
    print('-'*30)
    for image_name in images:
        if 'mask' in image_name:
            continue
        image_mask_name = image_name.split('.')[0] + '_mask.tif'
        img = misc.imread(os.path.join(train_data_path, image_name))
        img_mask = misc.imread(os.path.join(train_data_path, image_mask_name))

        img = np.array([img])
        img_mask = np.array([img_mask])

        imgs[i] = img
        imgs_mask[i] = img_mask

        if i % 100 == 0:
            print('Done: {0}/{1} images'.format(i, total))
        i += 1
    print('Loading done.')

    np.save(os.path.join(data_creation_path, 'imgs_train.npy'), imgs)
    np.save(os.path.join(data_creation_path, 'imgs_mask_train.npy'), imgs_mask)
    print('Saving to .npy files done.')


def load_train_data():
    imgs_train = np.load(os.path.join(data_creation_path, 'imgs_train.npy'))
    imgs_mask_train = np.load(os.path.join(data_creation_path, 'imgs_mask_train.npy'))
    return imgs_train, imgs_mask_train


def create_test_data():
    train_data_path = os.path.join(data_original_path, 'test_jsrt')
    images = os.listdir(train_data_path)
    total = len(images)/2

    imgs = np.ndarray((total, 1, image_rows, image_cols), dtype=np.uint8)
    imgs_mask = np.ndarray((total, 1, image_rows, image_cols), dtype=np.uint8)

    i = 0
    print('-'*30)
    print('Creating test images...')
    print('-'*30)
    for image_name in images:
        if 'mask' in image_name:
            continue
        image_mask_name = image_name.split('.')[0] + '_mask.tif'
        img = misc.imread(os.path.join(train_data_path, image_name))
        img_mask = misc.imread(os.path.join(train_data_path, image_mask_name))
        img = np.array([img])
        img_mask = np.array([img_mask])

        imgs[i] = img
        imgs_mask[i] = img_mask

        if i % 100 == 0:
            print('Done: {0}/{1} images'.format(i, total))
        i += 1
    print('Loading done.')

    #np.save(os.path.join(data_creation_path, 'imgs_test.npy', imgs))
    np.save('imgs_test.npy', imgs)
    np.save('imgs_mask_test.npy', imgs_mask)
    print('Saving to .npy files done.')


def load_test_data():
    imgs_test = np.load(os.path.join(data_creation_path, 'imgs_test.npy'))
    imgs_mask = np.load(os.path.join(data_creation_path, 'imgs_mask_test.npy'))
    return imgs_test, imgs_mask

if __name__ == '__main__':
    create_train_data()
    create_test_data()
