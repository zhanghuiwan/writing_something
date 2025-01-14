'''
参考资料：《动手学深度学习》
'''

import torch
import torchvision
from torch import nn
from torch.nn import functional as F
from d2l import torch as d2l
from data import load_data_from_root_folder
import cv2 as cv
from tqdm import tqdm

# Defined in file: ./chapter_computer-vision/anchor.md
def multibox_target(anchors, labels):
    """Label anchor boxes using ground-truth bounding boxes."""
    batch_size, anchors = len(labels), anchors.squeeze(0)
    batch_offset, batch_mask, batch_class_labels = [], [], []
    device, num_anchors = anchors.device, anchors.shape[0]
    for i in range(batch_size):
        label = labels[i].to(anchors.device)
        anchors_bbox_map = d2l.assign_anchor_to_bbox(label[:, 1:], anchors,
                                                 device)
        bbox_mask = ((anchors_bbox_map >= 0).float().unsqueeze(-1)).repeat(
            1, 4)
        # Initialize class labels and assigned bounding box coordinates with
        # zeros
        class_labels = torch.zeros(num_anchors, dtype=torch.long,
                                   device=device)
        assigned_bb = torch.zeros((num_anchors, 4), dtype=torch.float32,
                                  device=device)
        # Label classes of anchor boxes using their assigned ground-truth
        # bounding boxes. If an anchor box is not assigned any, we label its
        # class as background (the value remains zero)
        indices_true = torch.nonzero(anchors_bbox_map >= 0)
        bb_idx = anchors_bbox_map[indices_true]
        class_labels[indices_true] = label[bb_idx, 0].long() + 1
        assigned_bb[indices_true] = label[bb_idx, 1:]
        # Offset transformation
        offset = d2l.offset_boxes(anchors, assigned_bb) * bbox_mask
        batch_offset.append(offset.reshape(-1))
        batch_mask.append(bbox_mask.reshape(-1))
        batch_class_labels.append(class_labels)
    bbox_offset = torch.stack(batch_offset)
    bbox_mask = torch.stack(batch_mask)
    class_labels = torch.stack(batch_class_labels)
    return (bbox_offset, bbox_mask, class_labels)

class cls_predictor(nn.Module):
    def __init__(self, num_inputs, num_anchors, num_classes):
        super().__init__()
        self.conv = nn.Conv2d(num_inputs, num_anchors * (num_classes + 1),
                     kernel_size=3, padding=1)

    def forward(self, X):
        return self.conv(X)



class bbox_predictor(nn.Module):
    def __init__(self, num_inputs, num_anchors):
        super().__init__()
        self.conv = nn.Conv2d(num_inputs, num_anchors * 4, kernel_size=3, padding=1)
        
    def forward(self, X):
        return self.conv(X)

layer = bbox_predictor(16, 5)
aaa = torch.ones(1, 16, 32, 32)
bbb = layer(aaa)
pass

def flatten_pred(pred):
    return torch.flatten(pred.permute(0, 2, 3, 1), start_dim=1)

def concat_preds(preds):
    return torch.cat([flatten_pred(p) for p in preds], dim=1)

class down_sample_blk(nn.Module):
    def __init__(self, in_channels, out_channels):
        super().__init__()
        self.conv_blk = nn.Sequential()
        for _ in range(2):
            self.conv_blk.append(nn.Conv2d(in_channels, out_channels,
                             kernel_size=3, padding=1))
            self.conv_blk.append(nn.BatchNorm2d(out_channels))
            self.conv_blk.append(nn.ReLU())
            in_channels = out_channels
        self.max_pool = nn.MaxPool2d(2)
        
    def forward(self, X):
        X = self.conv_blk(X)
        X = self.max_pool(X)
        return X

class base_net(nn.Module):
    def __init__(self):
        super().__init__()
        self.blk = nn.Sequential()
        num_filters = [3, 16, 32, 64]
        for i in range(len(num_filters) - 1):
            self.blk.append(down_sample_blk(num_filters[i], num_filters[i+1]))
    
    def forward(self, X):
        return self.blk(X)

def blk_forward(X, blk, size, ratio, cls_predictor, bbox_predictor):
    Y = blk(X)
    anchors = d2l.multibox_prior(Y, sizes=size, ratios=ratio)
    cls_preds = cls_predictor(Y)
    bbox_preds = bbox_predictor(Y)
    return (Y, anchors, cls_preds, bbox_preds)

sizes = [[0.2, 0.272], [0.37, 0.447], [0.54, 0.619], [0.71, 0.79],
         [0.88, 0.961]]
ratios = [[1, 2, 0.5]] * 5
num_anchors = len(sizes[0]) + len(ratios[0]) - 1

class TinySSD(nn.Module):
    def __init__(self, num_classes, **kwargs):
        super(TinySSD, self).__init__(**kwargs)
        self.num_classes = num_classes
        self.blk = nn.Sequential()
        self.cls = nn.Sequential()
        self.box = nn.Sequential()
        channel_lst = [64, 128, 128, 128, 128]
        for i in range(0, 5):
            if i == 0:
                self.blk.append(base_net())
            elif i == 1:
                self.blk.append(down_sample_blk(64, 128))
            elif i == 4:
                self.blk.append(nn.AdaptiveAvgPool2d((1, 1)))
            else:
                self.blk.append(down_sample_blk(128, 128))
            self.cls.append(cls_predictor(channel_lst[i], num_anchors, num_classes))
            self.box.append(bbox_predictor(channel_lst[i], num_anchors))

    def forward(self, X):
        anchors, cls_preds, bbox_preds = [None] * 5, [None] * 5, [None] * 5
        for i in range(5):
            X, anchors[i], cls_preds[i], bbox_preds[i] = blk_forward(X, self.blk[i], sizes[i], ratios[i], self.cls[i], self.box[i])
        anchors = torch.cat(anchors, dim=1)
        cls_preds = concat_preds(cls_preds)
        cls_preds = cls_preds.reshape(
            cls_preds.shape[0], -1, self.num_classes + 1)
        bbox_preds = concat_preds(bbox_preds)
        return anchors, cls_preds, bbox_preds
    
    def train_(self, batch_size=32, device=d2l.try_gpu(), num_epochs=20):
        train_loader, val_loader = load_data_from_root_folder(r"banana_dataset\banana-detection", batch_size)
        # train_loader, _ = d2l.load_data_bananas(batch_size)
        trainer = torch.optim.SGD(self.parameters(), lr=0.2, weight_decay=5e-4)
        self.cls_loss = nn.CrossEntropyLoss(reduction='none')
        self.bbox_loss = nn.L1Loss(reduction='none')
        for epoch in range(num_epochs):
        # 训练精确度的和，训练精确度的和中的示例数
        # 绝对误差的和，绝对误差的和中的示例数
            self.train()
            t = tqdm(train_loader)
            for features, target in t:
                trainer.zero_grad()
                X, Y = features.to(device), target
                # 生成多尺度的锚框，为每个锚框预测类别和偏移量
                anchors, cls_preds, bbox_preds = self(X)
                # 为每个锚框标注类别和偏移量
                bbox_labels, bbox_masks, cls_labels = multibox_target(anchors, Y)
                # 根据类别和偏移量的预测和标注值计算损失函数
                l = self.calc_loss(cls_preds, cls_labels, bbox_preds, bbox_labels,
                            bbox_masks)
                l.mean().backward()
                trainer.step()
                cls_err, bbox_mae = self.cls_eval(cls_preds, cls_labels) / cls_labels.numel(), \
                    self.bbox_eval(bbox_preds, bbox_labels, bbox_masks) / bbox_labels.numel()
                # print(1 - cls_err, "   ", bbox_mae)
                t.set_description("epoch: {}  cls_err: {}  box_err: {}".format(epoch, round(1 - cls_err, 4), round(bbox_mae, 4)))
            torch.save(self.state_dict(), "last.pt")
    
    def calc_loss(self, cls_preds, cls_labels, bbox_preds, bbox_labels, bbox_masks):
        batch_size, num_classes = cls_preds.shape[0], cls_preds.shape[2]
        cls = self.cls_loss(cls_preds.reshape(-1, num_classes),
                    cls_labels.reshape(-1)).reshape(batch_size, -1).mean(dim=1)
        bbox = self.bbox_loss(bbox_preds * bbox_masks,
                        bbox_labels * bbox_masks).mean(dim=1)
        return cls + bbox

    def cls_eval(self, cls_preds, cls_labels):
        # 由于类别预测结果放在最后一维，argmax需要指定最后一维。
        return float((cls_preds.argmax(dim=-1).type(
            cls_labels.dtype) == cls_labels).sum())

    def bbox_eval(self, bbox_preds, bbox_labels, bbox_masks):
        return float((torch.abs((bbox_labels - bbox_preds) * bbox_masks)).sum())

def train():
    device = d2l.try_gpu()
    net = TinySSD(num_classes=1).to(device)
    net.train_()

def test():
    device = d2l.try_gpu()
    net = TinySSD(num_classes=1).to(device)
    net.load_state_dict(torch.load("last.pt"))
    img = cv.imread(r"banana_dataset\banana-detection\valid\images\17.png")
    X = torch.from_numpy(img).permute(2, 0, 1).unsqueeze(0).to(device).float()
    anchors, cls_preds, bbox_preds = net(X.to(device))
    cls_probs = F.softmax(cls_preds, dim=2).permute(0, 2, 1)
    # xyxy格式
    output = d2l.multibox_detection(cls_probs, bbox_preds, anchors)
    box = [p for p in output[0] if p[1] > 0.8 and p[0] == 0]
    whwh = torch.tensor((img.shape[0], img.shape[1], img.shape[0], img.shape[1]))
    for i in range(len(box)):
        draw_box = (box[i][2:].cpu() * whwh).int().tolist()
        img = cv.rectangle(img, draw_box[:2], draw_box[2:], color=(0, 128, 0), thickness=1)
    cv.imwrite("tmp.png", img)

if __name__ == "__main__":
    train()
    test()
    
    
    
