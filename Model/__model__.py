import numpy as np
import torch
from torch.utils.data import DataLoader
from torchvision import transforms
import matplotlib.pyplot as plt
import cv2 
import numpy as np
from PIL import Image


# STEP :
# load image -> transform dataset -> DataLoad by pytorch -> image.to(device) -> model predict 

    
class UnetResClassifier():

    def __init__(self,device='cuda'):
       
        self.classifier = torch.load('../example/Model/bestmodel-resnet50-classification.pth')
        self.segment = torch.load('../example/Model/resnet50-200epoch.pth')
        self.device = device
    
    def Predict(self,image):
        
        seg_img,classifier_img = clean_image(image)
        ''' 
        unet return image'''
        seg_pred = self.segment(seg_img)
        '''
        resnet50 return label 0 1 2'''
        label_pred = self.classifier(classifier_img)
        
        return seg_pred , label_pred
    
    def Plot(self,
             seg_pred,
             label_pred,
             image,
             save_image,
             height_output,
             width_output):
        
        label_pred = self.Classes(reverse=True)[label_pred.item()]
        
        fig, ax = plt.subplots(figsize=(height_output, width_output))
        
        ax.set_title(label_pred)        
        ax.imshow(Polygons(np.squeeze(seg_pred.cpu().detach().numpy()),0.0,0.01))
        ax.imshow(image[0].cpu().detach().numpy().squeeze().transpose((1, 2, 0)),alpha=0.5)
        
        if save_image == True :
            plt.savefig('../example/Model/output_image/output.png')
            print(f'Save output success!! where : Model/output_image/...')
        
    def Classifier(self,
                   image,
                   height_output=12,
                   width_output=10,
                   save_image=False):
        
        seg_pred , label_pred = self.Predict(image) 
        label_pred = (torch.max(torch.exp(label_pred), 1)[1]).data.cpu().numpy()
        image = clean_image(image)
        self.Plot(seg_pred,label_pred,image,save_image,height_output,width_output)

    def Classes(self,reverse=False):
        if reverse is True : 
            return {1:'benign', 2:'malignant', 0:'normal'}
        else :
            return {'benign':1, 'malignant':2, 'normal':0}
            
    
def TransformImage(image):
    segment_transforms = transforms.Compose([transforms.Resize((256, 256)),
                                             transforms.ToTensor(),])
    classifier_transform = transforms.Compose([transforms.Resize((224, 224)),
                                               transforms.ToTensor(),
                                               transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),])
    return segment_transforms(image),classifier_transform(image) 

def clean_image(image) : 
    img_seg ,img_classifier = TransformImage(image)
    img_seg ,img_classifier = img_seg.unsqueeze(0) ,img_classifier.unsqueeze(0)
    
    return img_seg.cuda() ,img_classifier.cuda()

        
def image_from_path(path):
    """load image, returns cuda tensor"""
    image = Image.open(image_name)
    img_seg ,img_classifier = TransformImage(image)
    img_seg ,img_classifier = img_seg.unsqueeze(0) ,img_classifier.unsqueeze(0)
    
    return img_seg.cuda() ,img_classifier.cuda()
        

def Polygons(img,
             epls=0,
             min_=0.1):
    _, binary_image = cv2.threshold(img, min_, 255, cv2.THRESH_BINARY)
    binary_image = binary_image.astype(np.uint8)

    # Find contours in the binary mask
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Find the vertices of each contour and draw polylines
    polygons = []
    
    for contour in contours:
        
        # Convert contours to polygon approximation
        epsilon = epls * cv2.arcLength(contour, True)
        approx_polygon = cv2.approxPolyDP(contour, epsilon, True)
        
        polygons.append(approx_polygon)
        
    return cv2.polylines(img,polygons,isClosed=True, color=(255,0,0) ,thickness = 2)
 
        
        
        
        
       