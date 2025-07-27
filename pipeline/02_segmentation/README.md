# Segmentation

This directory contains notebooks for cell and nucleus segmentation using Cellpose.

## Notebooks

### 2_segmentation.ipynb
- **Purpose**: Initial segmentation using pre-trained Cellpose models
- **Input**: Preprocessed 2D images
- **Output**: Initial segmentation masks
- **Key Features**:
  - Pre-trained model evaluation
  - Initial mask generation
  - Performance assessment

### binary_nucleus.ipynb
- **Purpose**: Binary nucleus segmentation for comparison
- **Input**: Nucleus channel images
- **Output**: Binary nucleus masks
- **Key Features**:
  - Simple thresholding approach
  - Comparison with Cellpose results
  - Binary mask generation

### 5_complete_segmentation.ipynb
- **Purpose**: Apply trained models to complete dataset
- **Input**: All processed images, trained models
- **Output**: Final segmentation masks for all conditions
- **Key Features**:
  - Batch processing of all images
  - Application of fine-tuned models
  - Quality control and validation
  - Final mask generation for analysis

## Usage

Run notebooks in order:
1. `2_segmentation.ipynb` - Initial segmentation
2. `binary_nucleus.ipynb` - Binary comparison
3. `5_complete_segmentation.ipynb` - Complete dataset processing (after training)

## Dependencies

- cellpose
- numpy
- matplotlib
- tifffile
- opencv-python
