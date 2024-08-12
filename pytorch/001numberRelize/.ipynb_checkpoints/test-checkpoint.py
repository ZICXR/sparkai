import torch
import torchvision
from torchvision import transforms
from matplotlib import pyplot as plt
from torch import nn
from torch.nn import functional as F
from utils import plot_image,plot_curve,one_hot
from torch import optim
 
class Net(nn.Module):

    def __init__(self,input_dim,layer1_dim,layer2_dim,output_dim):  
        super(Net,self).__init__()
        #三层全连接层
        #wx+b
        self.flatten = nn.Flatten() 
        self.layer1 = nn.Sequential(nn.Linear(input_dim,layer1_dim),nn.ReLU())
        self.layer2 = nn.Sequential(nn.Linear(layer1_dim,layer2_dim),nn.ReLU())
        self.out = nn.Sequential(nn.Linear(layer2_dim,output_dim),nn.ReLU())
 
    def forward(self, x):
        x = self.flatten(x)
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.out(x)
 
        return x
 
batch_size = 512
#一次处理的图片的数量
# 读入数据
transform = transforms.Compose([
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Normalize((0.1307,), (0.3081,))
])
 
 
trainset = torchvision.datasets.MNIST(
    root='dataset/',
    train=True,  #如果为True，从 training.pt 创建数据，否则从 test.pt 创建数据。
    download=True, #如果为true，则从 Internet 下载数据集并将其放在根目录中。 如果已下载数据集，则不会再次下载。
    transform=transform
)
 
train_loader = torch.utils.data.DataLoader(
    dataset=trainset,
    batch_size=batch_size,
    shuffle=True  #在加载的时候将图片随机打散
)
 
testset = torchvision.datasets.MNIST(
    root='dataset/',
    train=False,
    download=True,
    transform=transform
)
 
test_loader = torch.utils.data.DataLoader(
    dataset=testset,
    batch_size=batch_size,
    shuffle=True
)
 
# 初始化网络中的值
input_dim,layer1_dim,layer2_dim,output_dim=28*28,512,128,10
model = Net(input_dim,layer1_dim,layer2_dim,output_dim)
print(model)
 
        

optimizer = optim.SGD(model.parameters(), lr=1e-3, momentum=0.9)
for epoch in range(3):
 
    #train_loader长度118
    for idx, data in enumerate(train_loader): #当然这里你也可以写next(iter(train_loader))
        inputs, labels = data
        #inputs和labels的 len都是512的
        #intpus 是 [512, 1, 28, 28]
        #labels 是 [512]
 
        inputs = inputs.view(inputs.size(0), 28*28)
        #现在inputs是[512, 28*28]
 
        outputs = model(inputs)
        #outputs是[512,10]
 
        labels_onehot = one_hot(labels)
        # 就是将y转成onehot
        # y是512个label值，是一个512*1的tensor数组
        # y_onehot是512个10维的，即512*10的tensor数组
        # 例如y的label是2，那么对应的y_onehot就是0，1，2，第三个位置为1，其余位置为0这样
 
        loss = F.mse_loss(outputs, labels_onehot) #用torch.nn.MSELoss()也行
 
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
 
        if idx % 10 == 0:
          print(epoch, idx, loss.item())
        
plot_curve(train_loss)
 
 
 
 
total_correct = 0
for idx, data in enumerate(test_loader):
    inputs, labels = data
    inputs = inputs.view(inputs.size(0), 28*28)
 
    outputs = net(inputs)
    pred = outputs.argmax(dim=1)
    correct = pred.eq(labels).sum().float().item()
    #correct的结果就是220，386，......, 表示每次512张图片中有几个是预测对了的
    # print(correct)
    total_correct += correct
 
accuracy = total_correct / len(test_loader.dataset)  #或者len(testset)
print('test accuracy: ', accuracy)
 
 
#显示图片和预测的label
inputs, labels = next(iter(test_loader))
outputs = net(inputs.view(inputs.size(0), 28*28))
pred = outputs.argmax(dim=1) #得到预测值
plot_image(inputs, pred, 'test')