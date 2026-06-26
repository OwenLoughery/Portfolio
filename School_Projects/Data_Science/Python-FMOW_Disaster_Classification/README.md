# Post-Disaster Satellite Image Classification (DATA 402)

**Technologies:** Python, PyTorch, scikit-learn, boto3/AWS S3, CNNs, ResNet-18 transfer learning, ImageNet pretraining

A multi-class satellite image classification project that automatically sorts image tiles into 8 disaster-response categories spanning visible damage (flooded roads, debris), critical infrastructure (hospitals, fire stations), and residential zones. The project builds a clean three-tier model comparison where each model adds exactly one capability over the last: logistic regression on flattened pixels (baseline), a from-scratch CNN (adds spatial structure), and a fine-tuned ResNet-18 (adds ImageNet prior knowledge).

A custom `boto3` pipeline downloads only the needed images from the 200GB+ fMoW dataset on AWS S3, then crops to bounding boxes, resizes to 224x224, augments, and handles class imbalance with weighted loss.

**Dataset:** Functional Map of the World (fMoW), RGB version, IARPA 2018

**Test set results (macro-F1):** Logistic Regression 0.188 → CNN 0.505 → ResNet-18 0.653

**Repository:**  
https://github.com/OwenLoughery/FMOW-Disaster-Image-Classification

**Key files:** `Final_Report.md`, `DisasterClassifier.ipynb`, `data_loader.py`
