# **RES-Unet Classifier**

#### **ลำดับการทำงาน folder Model**

<img width="797" alt="image" src="https://github.com/Dont-HurtMe/RES-UnetClassifier/assets/154254885/d66edc23-2080-4b0a-a5d5-2641b3d10ee8">

--------------------------------------------------------------------------------------------------------------------------------------------
#### **ผลลัพธ์ โมเดล**
**Unet (segmentation model)** best evaluate { dice_loss: 0.1329 , dic_coffecients: 0.5584 , iou:0.7725}

**iou logs**

<img width="612" alt="image" src="https://github.com/Dont-HurtMe/RES-UnetClassifier/assets/154254885/957fe9a1-c909-443b-adb0-a05a92f0717e">

**dic_loss logs**

<img width="619" alt="image" src="https://github.com/Dont-HurtMe/RES-UnetClassifier/assets/154254885/dc9e37bd-cbe4-4442-90a1-83ba923dd535">

**Example predict mask with test-set**

<img width="384" alt="image" src="https://github.com/Dont-HurtMe/RES-UnetClassifier/assets/154254885/59c13b44-d9ce-4515-8846-573a3df17c58">

<img width="383" alt="image" src="https://github.com/Dont-HurtMe/RES-UnetClassifier/assets/154254885/2d58c1de-4f95-4a6f-8fd3-ac1f91550118">

--------------------------------------------------------------------------------------------------------------------------------------------

**ResNet50 (classifier model)** 

**class counter** {benign: 121 , malignant: 121 , normal: 121}

**Evaluate** {CrossEntropyLoss: 0.1725 , accuracy: 0.9946}

**Logs CrossEntropyLoss**

<img width="605" alt="image" src="https://github.com/Dont-HurtMe/RES-UnetClassifier/assets/154254885/de2ee5c7-6fb8-4962-89eb-c00f133e5454">

**Confusion metrics**

<img width="90" alt="image" src="https://github.com/Dont-HurtMe/RES-UnetClassifier/assets/154254885/279fc5a6-2051-44e1-9189-c7c66bbd9336">

<img width="222" alt="image" src="https://github.com/Dont-HurtMe/RES-UnetClassifier/assets/154254885/db4a377c-6c4b-4a65-afba-92e17dd8fa65">




