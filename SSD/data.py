import numpy as np
import torch 
import cv2 as cv
import os
from torch.utils.data import Dataset, DataLoader
from torch.nn.functional import one_hot
from tqdm import tqdm
from copy import deepcopy
    

def load_data_from_folder(folder:str):
    images_folder = os.path.join(folder, "images")
    labels_folder = os.path.join(folder, "labels")
    images_names = os.listdir(images_folder)
    labels_names = []
    for image_name in images_names:
        labels_names.append('.'.join(image_name.split('.')[:-1] + ['txt']))
    
    images_lst = []
    labels_lst = []
    for image_name, label_name in zip(images_names, labels_names):
        label_lst = []
        label = open(os.path.join(labels_folder, label_name)).readlines()
        for i in label:
            label_lst.append([float(p) for p in i.split(" ")])
        if label_lst == []:
            continue
        xywh_label = torch.Tensor(label_lst).float()
        xyxy_label = deepcopy(xywh_label)
        xyxy_label[:, 1] = xywh_label[:, 1] - xywh_label[:, 3] / 2
        xyxy_label[:, 2] = xywh_label[:, 2] - xywh_label[:, 4] / 2
        xyxy_label[:, 3] = xywh_label[:, 1] + xywh_label[:, 3] / 2
        xyxy_label[:, 4] = xywh_label[:, 2] + xywh_label[:, 4] / 2
        labels_lst.append(xyxy_label)
        
        image = cv.imread(os.path.join(images_folder, image_name))
        image = cv.resize(image, (256, 256))
        image = torch.from_numpy(image).permute(2, 0, 1).float()
        images_lst.append(image)
    return images_lst, labels_lst

class SSD_dataset(Dataset):
    def __init__(self, images, labels):
        self.images = images
        self.labels = labels
    
    def __getitem__(self, index):
        image = self.images[index]
        label = self.labels[index]
        
        return image, label
    
    def __len__(self):
        return len(self.images)

def collate_fn(batch_data):
    image_lst = [p[0] for p in batch_data]
    label_lst = [p[1] for p in batch_data]
    return torch.stack(image_lst), label_lst

def load_data_from_root_folder(data_root_path:str, batch_size=8, num_workers=0):
    train_images, train_labels = load_data_from_folder(os.path.join(data_root_path, "train"))
    val_images, val_labels = load_data_from_folder(os.path.join(data_root_path, "valid"))
    train_set = SSD_dataset(train_images, train_labels)
    val_set = SSD_dataset(val_images, val_labels)
    train_loader = DataLoader(train_set, batch_size, shuffle=True, num_workers=num_workers, collate_fn=collate_fn)
    val_loader = DataLoader(val_set, batch_size, shuffle=False, num_workers=num_workers, collate_fn=collate_fn)
    return train_loader, val_loader

if __name__ == "__main__":
    train_loader, val_loader = load_data_from_root_folder(r"dataset")
    for i, j in train_loader:
        break
    pass
