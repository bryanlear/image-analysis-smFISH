# Model Training

This directory contains notebooks for training and fine-tuning Cellpose models.

## Notebooks

### 3_model_training.ipynb
- **Purpose**: Fine-tune pre-trained Cellpose models for smFISH data
- **Input**: Training image-mask pairs, pre-trained models
- **Output**: Fine-tuned models optimized for smFISH segmentation
- **Key Features**:
  - Fine-tuning of 'cpsam' model for smFISH cells
  - Training on denoised images
  - Custom training parameters optimization
  - Model validation and performance metrics

## Training Parameters

The notebook uses the following optimized parameters:
- **n_epochs**: 400
- **learning_rate**: 0.005
- **batch_size**: 4
- **weight_decay**: 0.0001
- **min_train_masks**: 1

## Model Selection

- **smFISH Segmentation**: Fine-tuned 'cpsam' model
  - Better performance on sparse, spotty signals
  - Optimized for denoised images
  
- **Nucleus Segmentation**: Pre-trained 'nuclei' model
  - Excellent performance without fine-tuning
  - Reliable for nuclear staining

## Usage

1. Ensure training data is prepared (run preprocessing notebooks first)
2. Execute `3_model_training.ipynb`
3. Models will be saved for use in validation and complete segmentation

## Dependencies

- cellpose
- torch
- numpy
- matplotlib
- tifffile
