# Model Validation

This directory contains notebooks for validating trained models.

## Notebooks

### 4_1_validation_smfish.ipynb
- **Purpose**: Validate fine-tuned smFISH segmentation model
- **Input**: Training images, fine-tuned cpsam model, ground truth masks
- **Output**: Validation metrics and comparison visualizations
- **Key Features**:
  - Performance evaluation on training set
  - Comparison with ground truth annotations
  - Visual validation of segmentation quality
  - Model performance metrics

### 4_2_validation_nucleus.ipynb
- **Purpose**: Validate nucleus segmentation model
- **Input**: Nucleus images, nuclei model, ground truth masks
- **Output**: Validation metrics for nucleus segmentation
- **Key Features**:
  - Evaluation of pre-trained nuclei model
  - Comparison with manual annotations
  - Assessment of segmentation accuracy
  - Quality control metrics

## Validation Metrics

The notebooks evaluate models using:
- **Visual Inspection**: Side-by-side comparison of predictions vs ground truth
- **Mask Overlap**: Intersection over Union (IoU) metrics
- **Segmentation Quality**: Cell boundary accuracy
- **False Positive/Negative Analysis**: Detection accuracy assessment

## Usage

Run after model training:
1. `4_1_validation_smfish.ipynb` - Validate smFISH model
2. `4_2_validation_nucleus.ipynb` - Validate nucleus model

These notebooks help ensure model quality before applying to the complete dataset.

## Dependencies

- cellpose
- numpy
- matplotlib
- tifffile
- scikit-image
