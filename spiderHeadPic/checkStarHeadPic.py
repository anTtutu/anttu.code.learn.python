# -*- coding:utf-8 -*-

import os
import face_recognition
from PIL import Image
from PIL import ImageFile
import threading

ImageFile.LOAD_TRUNCATED_IMAGES = True


def process_img(path, new_path):
    dirs = os.listdir(path)
    for pic_dir in dirs:
        print(pic_dir)
        dir_path = os.path.join(path, pic_dir)
        pics = os.listdir(dir_path)
        for pic in pics:
            pic_path = os.path.join(dir_path, pic)
            image = face_recognition.load_image_file(pic_path)
            face_locations = face_recognition.face_locations(image)
            if len(face_locations) == 0:
                continue
            img = Image.open(pic_path)
            new_pic_path = os.path.join(new_path, pic_dir)
            if not os.path.exists(new_pic_path):
                os.makedirs(new_pic_path)
            if len(img.split()) == 4:
                # 利用split和merge将通道从四个转换为三个
                r, g, b, a = img.split()
                toimg = Image.merge("RGB", (r, g, b))
                toimg.save(new_pic_path + '\\' + pic)
            else:
                try:
                    img.save(new_pic_path + '\\' + pic)
                except:
                    continue
        print('Finish......!')


def lock_test(path, new_path):
    mu = threading.Lock()
    if mu.acquire(True):
        process_img(path, new_path)
        mu.release()


if __name__ == '__main__':
    paths = [r'D:\Work\images']
    new_paths = [r'D:\trainA']
    for i in range(len(paths)):
        my_thread = threading.Thread(target=lock_test, args=(paths[i], new_paths[i]))
        my_thread.start()