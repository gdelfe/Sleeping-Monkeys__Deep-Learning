#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 18:15:14 2021

@author: bijanadmin
"""
import torch
from torch import nn
import torch.nn.functional as F
import pdb
import matplotlib.pyplot as plt


# class CNN(nn.Module):
#     def __init__(self):
#         super(CNN,self).__init__()
    
#         # convolutional layer (sees 1x100x10 image tensor)
#         self.conv1 = nn.Conv2d(in_channels=62, out_channels=2,kernel_size=(3,3),stride=(1,1),padding=(1,1))
#         # convolutional layer (sees 2x50x5 tensor)
#         self.conv2 = nn.Conv2d(in_channels=2, out_channels=4,kernel_size=(3,3),stride=(1,1),padding=(1,1))
#         # sees a layer 4x25x2
#         self.fc1 = nn.Linear(4*25*2,1)
        
#         # Max pooling
#         self.pool = nn.MaxPool2d(2,2)
#         # dropout layer 
#         self.dropout = nn.Dropout(0.2)
#          # batch normalization 
#         self.bn1 = nn.BatchNorm2d(2)
#         self.bn2 = nn.BatchNorm2d(4)
      
#     def forward(self,x):
        
#         pdb.set_trace()
#         print('x shape 1',x.shape)
       
#         x = x.float()
#         conv_x1 = self.conv1(x)
#         x = self.pool(F.relu(self.bn1(conv_x1))) # Convolution 1:
            
#         print('x shape after 1 cnn',x.shape)
#         pdb.set_trace()

#         conv_x2 = self.conv2(x)
#         x = self.pool(F.relu(self.bn1(conv_x2))) # Convolution 2:
            
#         print('x shape after 2 cnn',x.shape)
#         pdb.set_trace()

#         x = x.view(x.shape[0],-1) # flatten image input
        
#         print('x before fully connected',x.shape)
#         pdb.set_trace()
        
#         x = self.dropout(x) # dropout
#         x = self.fc1(x) # Fully connected layer
        
#         return x
    
    
    
class GLM(nn.Module):
    def __init__(self, input_dim=100*10*62, output_dim=1):
        super(GLM, self).__init__()
        self.linear = torch.nn.Linear(input_dim, output_dim) # by default, add an intercept

    def forward(self, x):
        x = x.reshape([x.shape[0], 1, -1]).float()
        outputs = self.linear(x)
        return outputs