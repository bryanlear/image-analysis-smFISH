# Utilities and Visualization

This directory contains notebooks for generating visualizations and utility functions.

## Notebooks

### 6_generate_outlines.ipynb
- **Purpose**: Generate segmentation outlines for visualization
- **Input**: Segmentation masks from complete analysis
- **Output**: Outline images overlaid on original data
- **Key Features**:
  - Convert masks to outline contours
  - Overlay outlines on original images
  - Generate publication-quality figures
  - Color-coded visualization by condition

### 7_1_frame_compiler.ipynb
- **Purpose**: Compile individual frames for animation (Part 1)
- **Input**: Segmented images and outlines
- **Output**: Individual frames for GIF animation
- **Key Features**:
  - Frame-by-frame compilation
  - Consistent formatting across conditions
  - Preparation for animation generation

### 7_2_frame_compiler.ipynb
- **Purpose**: Compile individual frames for animation (Part 2)
- **Input**: Compiled frames from Part 1
- **Output**: Final animated GIF files
- **Key Features**:
  - GIF animation generation
  - Optimized frame timing
  - Final visualization products

## Visualization Outputs

The utilities generate:
- **Static Images**: Segmentation outlines overlaid on original data
- **Animated GIFs**: Time-lapse style visualization of segmentation results
- **Publication Figures**: High-quality images for presentations and papers

## Usage

Run in sequence after complete analysis:
1. `6_generate_outlines.ipynb` - Generate outline visualizations
2. `7_1_frame_compiler.ipynb` - Compile animation frames
3. `7_2_frame_compiler.ipynb` - Create final animations

## Dependencies

- matplotlib
- opencv-python
- PIL (Pillow)
- numpy
- tifffile
