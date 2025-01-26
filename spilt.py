import os
import shutil
import random


def split_dataset(image_dir, label_dir, train_image_dir, test_image_dir, train_label_dir, test_label_dir,
                  test_ratio=0.2):
    images = [f for f in os.listdir(image_dir) if f.endswith('.jpg') or f.endswith('.png')]
    random.shuffle(images)
    split_index = int(len(images) * (1 - test_ratio))

    train_images = images[:split_index]
    test_images = images[split_index:]

    for image in train_images:
        label = image.replace('.jpg', '.txt').replace('.png', '.txt')
        image_path = os.path.join(image_dir, image)
        label_path = os.path.join(label_dir, label)

        if os.path.exists(label_path):
            shutil.move(image_path, os.path.join(train_image_dir, image))
            shutil.move(label_path, os.path.join(train_label_dir, label))
        else:
            print(f"Warning: Label for {image} not found.")

    for image in test_images:
        label = image.replace('.jpg', '.txt').replace('.png', '.txt')
        image_path = os.path.join(image_dir, image)
        label_path = os.path.join(label_dir, label)

        if os.path.exists(label_path):
            shutil.move(image_path, os.path.join(test_image_dir, image))
            shutil.move(label_path, os.path.join(test_label_dir, label))
        else:
            print(f"Warning: Label for {image} not found.")


if __name__ == '__main__':
    base_dir = r'D:\runa\segment\dataset'  # 基础目录
    image_dir = os.path.join(base_dir, 'images')  # 图片目录
    label_dir = os.path.join(base_dir, 'labels')  # 标签目录

    # 创建 train 和 test 文件夹
    train_image_dir = os.path.join(base_dir, 'train', 'images')
    test_image_dir = os.path.join(base_dir, 'test', 'images')
    train_label_dir = os.path.join(base_dir, 'train', 'labels')
    test_label_dir = os.path.join(base_dir, 'test', 'labels')
    os.makedirs(train_image_dir, exist_ok=True)
    os.makedirs(test_image_dir, exist_ok=True)
    os.makedirs(train_label_dir, exist_ok=True)
    os.makedirs(test_label_dir, exist_ok=True)

    # 分割数据集并移动文件
    split_dataset(image_dir, label_dir, train_image_dir, test_image_dir, train_label_dir, test_label_dir,
                  test_ratio=0.2)
