from torch.utils.data import Dataset, DataLoader # 导入
from PIL import Image # 读取图片
import os

class MyData(Dataset):
    def __init__(self, root_dir, label_dir):
        self.root_dir = root_dir
        self.label_dir = label_dir
        self.path = os.path.join(root_dir, label_dir)
        self.img_path = os.listdir(self.path)

    def __getitem__(self, idx):
        img_name = self.img_path[idx]
        img_item_path = os.path.join(self.root_dir, self.label_dir, img_name)
        img = Image.open(img_item_path)
        label = self.label_dir
        return img, label

    def __len__(self):
        return len(self.img_path)

train_data = MyData("./mnist_dataset/train", "0")
test_data = MyData("./mnist_dataset/test", "0")
for i in range(1, 10):
        dataSetTrain = MyData("./mnist_dataset/train", str(i))
        dataSetTest = MyData("./mnist_dataset/test", str(i))
        train_data = train_data + dataSetTrain
        test_data = test_data + dataSetTest

print(len(train_data))

