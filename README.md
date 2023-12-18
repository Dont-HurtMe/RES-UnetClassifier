# **RES-Unet Classifier**

#### **ลำดับการทำงาน folder Model**

<img width="797" alt="image" src="https://github.com/Dont-HurtMe/RES-UnetClassifier/assets/154254885/d66edc23-2080-4b0a-a5d5-2641b3d10ee8">

#### **ผลลัพธ์ โมเดล**
* **Unet (segmentation model)** best evaluate { dice_loss: 0.1329 , dic_coffecients: 0.5584 , iou:0.7725}
class counter {benign: 121 , malignant: 121 , normal: 121}
**Confusion metrics**
<img width="222" alt="image" src="https://github.com/Dont-HurtMe/RES-UnetClassifier/assets/154254885/db4a377c-6c4b-4a65-afba-92e17dd8fa65">



* **ResNet50 (classifier model)** evaluate {CrossEntropyLoss: 0.1725 , accuracy: 0.9946}





