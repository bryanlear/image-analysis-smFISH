# Quantitative Analysis

This directory contains notebooks for mRNA spot detection and statistical analysis.

## Notebooks

### 8_blob_detection.ipynb
- **Purpose**: Detect and count mRNA spots within segmented cells
- **Input**: Segmented cell masks, smFISH images
- **Output**: Quantified spot counts per cell, intensity measurements
- **Key Features**:
  - Blob detection algorithm for mRNA spots
  - Spot counting within cell boundaries
  - Intensity quantification for nascent transcription sites
  - Per-cell and per-condition analysis
  - Export to CSV for statistical analysis

### 9_stats.ipynb
- **Purpose**: Statistical analysis of mRNA spot counts across conditions
- **Input**: Quantification results from blob detection
- **Output**: Statistical test results, significance analysis
- **Key Features**:
  - Kruskal-Wallis H-test for group comparisons
  - Dunn's post-hoc test for pairwise comparisons
  - Box plots and distribution visualizations
  - P-value calculations and significance assessment

## Analysis Workflow

1. **Spot Detection**: Identify mRNA spots using blob detection
2. **Quantification**: Count spots per cell for each treatment condition
3. **Statistical Testing**: Compare distributions across conditions
4. **Visualization**: Generate plots showing treatment effects

## Key Results

The analysis demonstrates:
- **DMSO (Control)**: Highest median mRNA count
- **JQ1 Treatment**: Significantly reduced mRNA count (p < 0.05)
- **TSA Treatment**: Lowest mRNA count, significantly different from control (p < 0.05)
- **JQ1 vs TSA**: No significant difference (p > 0.05)

## Dependencies

- pandas
- numpy
- matplotlib
- scipy
- scikit-posthocs
- scikit-image
