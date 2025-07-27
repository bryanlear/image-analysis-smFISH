# Data Preprocessing

This directory contains notebooks for preprocessing raw smFISH data.

## Notebooks

### 1_data_preprocessing.ipynb
- **Purpose**: Convert 3D TIFF stacks to 2D maximum intensity projections
- **Input**: Raw 3D multi-channel TIFF files (Z=15, C=2)
- **Output**: 2D projection images separated by channel (nucleus and smFISH)
- **Key Features**:
  - Maximum intensity projection along Z-axis
  - Channel separation (CH0: nucleus, CH1: smFISH)
  - Organized output structure by treatment condition

### denoising_fish.ipynb
- **Purpose**: Apply BM3D denoising algorithm to smFISH images
- **Input**: 2D smFISH projection images
- **Output**: Denoised smFISH images with improved signal-to-noise ratio
- **Key Features**:
  - BM3D (Block-matching and 3D filtering) algorithm
  - Background noise reduction
  - Signal enhancement for better segmentation

### preprocess_for_training.ipynb
- **Purpose**: Prepare training data for model fine-tuning
- **Input**: Processed images and manual annotations
- **Output**: Training-ready image-mask pairs
- **Key Features**:
  - Data organization for Cellpose training
  - Quality control and validation
  - Training set preparation

## Usage

Run notebooks in order:
1. `1_data_preprocessing.ipynb` - Convert raw data
2. `denoising_fish.ipynb` - Denoise smFISH images
3. `preprocess_for_training.ipynb` - Prepare training data

## Dependencies

- tifffile
- numpy
- bm3d
- opencv-python
- matplotlib
