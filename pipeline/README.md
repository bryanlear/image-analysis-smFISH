# smFISH Analysis Pipeline

This directory contains an organized, integrated pipeline for quantitative analysis of single-molecule FISH (smFISH) images. The pipeline processes 3D TIFF stacks through segmentation, quantification, and statistical analysis to measure the effects of therapeutic compounds on gene expression.

## Quick Start

To run the complete pipeline:

```bash
cd pipeline
jupyter notebook smfish_analysis_pipeline.ipynb
```

The main pipeline notebook will execute all stages in the correct order.

## Pipeline Structure

```
pipeline/
├── smfish_analysis_pipeline.ipynb    # Main pipeline notebook
├── 01_preprocessing/                  # Data preprocessing and denoising
│   ├── 1_data_preprocessing.ipynb
│   ├── denoising_fish.ipynb
│   └── preprocess_for_training.ipynb
├── 02_segmentation/                   # Cell and nucleus segmentation
│   ├── 2_segmentation.ipynb
│   ├── binary_nucleus.ipynb
│   └── 5_complete_segmentation.ipynb
├── 03_training/                       # Model training and fine-tuning
│   └── 3_model_training.ipynb
├── 04_validation/                     # Model validation
│   ├── 4_1_validation_smfish.ipynb
│   └── 4_2_validation_nucleus.ipynb
├── 05_analysis/                       # Quantitative analysis
│   ├── 8_blob_detection.ipynb
│   └── 9_stats.ipynb
├── 06_utilities/                      # Visualization and utilities
│   ├── 6_generate_outlines.ipynb
│   ├── 7_1_frame_compiler.ipynb
│   └── 7_2_frame_compiler.ipynb
└── results/                           # Output data and visualizations
    ├── plots/
    └── tables/
```

## Pipeline Stages

### 1. Preprocessing (01_preprocessing/)
- Convert 3D TIFF stacks to 2D maximum intensity projections
- Apply BM3D denoising to enhance signal-to-noise ratio
- Prepare training data for model fine-tuning

### 2. Segmentation (02_segmentation/)
- Initial segmentation with pre-trained Cellpose models
- Binary segmentation approaches for comparison
- Complete dataset segmentation with trained models

### 3. Training (03_training/)
- Fine-tune Cellpose 'cpsam' model for smFISH data
- Optimize parameters for sparse, spotty signals
- Validate training performance

### 4. Validation (04_validation/)
- Validate smFISH segmentation model performance
- Assess nucleus segmentation accuracy
- Quality control before full dataset processing

### 5. Analysis (05_analysis/)
- Detect and count mRNA spots using blob detection
- Perform statistical analysis (Kruskal-Wallis, Dunn's test)
- Generate quantification results

### 6. Utilities (06_utilities/)
- Generate segmentation outline visualizations
- Compile animation frames
- Create publication-quality figures

## Key Features

- **Modular Design**: Each stage can be run independently
- **Comprehensive Documentation**: README files in each directory
- **Reproducible Results**: Consistent parameters and methods
- **Quality Control**: Validation steps throughout the pipeline
- **Statistical Analysis**: Rigorous statistical testing of results

## Dependencies

The pipeline requires the following Python packages:
- cellpose
- numpy
- matplotlib
- tifffile
- opencv-python
- bm3d
- pandas
- scipy
- scikit-posthocs
- scikit-image
- PIL (Pillow)

## Results

The pipeline generates:
- **Segmentation masks** for cells and nuclei
- **mRNA spot counts** per cell for each treatment condition
- **Statistical analysis** showing significant differences between treatments
- **Visualizations** including plots and animated GIFs
- **Publication-ready figures** for presentations and papers

## Usage Notes

1. **Data Requirements**: Place raw 3D TIFF files in the `../data/raw/` directory
2. **Execution Order**: Follow the numbered sequence or use the main pipeline notebook
3. **Customization**: Modify parameters in individual notebooks as needed
4. **Results**: Check the `results/` directory for all outputs

## Citation

If you use this pipeline, please cite the original Cellpose paper:
- Stringer, C., Wang, T., Michaelos, M. et al. Cellpose: a generalist algorithm for cellular segmentation. Nat Methods 18, 100–106 (2021).

## Support

For questions or issues:
1. Check individual notebook documentation
2. Review README files in each directory
3. Examine the main pipeline notebook for workflow understanding
