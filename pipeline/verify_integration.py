#!/usr/bin/env python3
"""
Pipeline Integration Verification Script

This script verifies that all notebooks have been properly integrated
and the pipeline structure is complete.
"""

import os
from pathlib import Path

def check_file_exists(filepath, description):
    """Check if a file exists and report status."""
    if os.path.exists(filepath):
        print(f"✓ {description}: {filepath}")
        return True
    else:
        print(f"✗ MISSING {description}: {filepath}")
        return False

def verify_pipeline_structure():
    """Verify the complete pipeline structure."""
    print("=== PIPELINE INTEGRATION VERIFICATION ===\n")
    
    all_good = True
    
    # Check main pipeline files
    print("1. Main Pipeline Files:")
    main_files = [
        ("pipeline/README.md", "Main README"),
        ("pipeline/smfish_analysis_pipeline.ipynb", "Main Pipeline Notebook"),
        ("pipeline/run_pipeline.py", "Command-line Runner"),
        ("pipeline/INTEGRATION_SUMMARY.md", "Integration Summary")
    ]
    
    for filepath, desc in main_files:
        if not check_file_exists(filepath, desc):
            all_good = False
    
    # Check preprocessing notebooks
    print("\n2. Preprocessing Notebooks:")
    preprocessing_files = [
        ("pipeline/01_preprocessing/README.md", "Preprocessing README"),
        ("pipeline/01_preprocessing/1_data_preprocessing.ipynb", "Data Preprocessing"),
        ("pipeline/01_preprocessing/denoising_fish.ipynb", "Fish Denoising"),
        ("pipeline/01_preprocessing/preprocess_for_training.ipynb", "Training Prep")
    ]
    
    for filepath, desc in preprocessing_files:
        if not check_file_exists(filepath, desc):
            all_good = False
    
    # Check segmentation notebooks
    print("\n3. Segmentation Notebooks:")
    segmentation_files = [
        ("pipeline/02_segmentation/README.md", "Segmentation README"),
        ("pipeline/02_segmentation/2_segmentation.ipynb", "Initial Segmentation"),
        ("pipeline/02_segmentation/binary_nucleus.ipynb", "Binary Nucleus"),
        ("pipeline/02_segmentation/5_complete_segmentation.ipynb", "Complete Segmentation")
    ]
    
    for filepath, desc in segmentation_files:
        if not check_file_exists(filepath, desc):
            all_good = False
    
    # Check training notebooks
    print("\n4. Training Notebooks:")
    training_files = [
        ("pipeline/03_training/README.md", "Training README"),
        ("pipeline/03_training/3_model_training.ipynb", "Model Training")
    ]
    
    for filepath, desc in training_files:
        if not check_file_exists(filepath, desc):
            all_good = False
    
    # Check validation notebooks
    print("\n5. Validation Notebooks:")
    validation_files = [
        ("pipeline/04_validation/README.md", "Validation README"),
        ("pipeline/04_validation/4_1_validation_smfish.ipynb", "smFISH Validation"),
        ("pipeline/04_validation/4_2_validation_nucleus.ipynb", "Nucleus Validation")
    ]
    
    for filepath, desc in validation_files:
        if not check_file_exists(filepath, desc):
            all_good = False
    
    # Check analysis notebooks
    print("\n6. Analysis Notebooks:")
    analysis_files = [
        ("pipeline/05_analysis/README.md", "Analysis README"),
        ("pipeline/05_analysis/8_blob_detection.ipynb", "Blob Detection"),
        ("pipeline/05_analysis/9_stats.ipynb", "Statistical Analysis")
    ]
    
    for filepath, desc in analysis_files:
        if not check_file_exists(filepath, desc):
            all_good = False
    
    # Check utility notebooks
    print("\n7. Utility Notebooks:")
    utility_files = [
        ("pipeline/06_utilities/README.md", "Utilities README"),
        ("pipeline/06_utilities/6_generate_outlines.ipynb", "Generate Outlines"),
        ("pipeline/06_utilities/7_1_frame_compiler.ipynb", "Frame Compiler 1"),
        ("pipeline/06_utilities/7_2_frame_compiler.ipynb", "Frame Compiler 2")
    ]
    
    for filepath, desc in utility_files:
        if not check_file_exists(filepath, desc):
            all_good = False
    
    # Check results directory
    print("\n8. Results Directory:")
    results_dirs = [
        ("pipeline/results", "Results Directory"),
        ("pipeline/results/tables", "Results Tables"),
        ("results", "Original Results Directory"),
        ("results/plots", "Results Plots"),
        ("results/tables", "Original Results Tables")
    ]
    
    for dirpath, desc in results_dirs:
        if not check_file_exists(dirpath, desc):
            all_good = False
    
    # Summary
    print("\n" + "="*50)
    if all_good:
        print("🎉 VERIFICATION SUCCESSFUL!")
        print("All pipeline components are properly integrated.")
        print("\nYou can now run the pipeline using:")
        print("  cd pipeline")
        print("  jupyter notebook smfish_analysis_pipeline.ipynb")
        print("  # OR")
        print("  python run_pipeline.py --all")
    else:
        print("❌ VERIFICATION FAILED!")
        print("Some components are missing. Please check the errors above.")
    
    return all_good

def count_notebooks():
    """Count total notebooks in the pipeline."""
    notebook_count = 0
    for root, dirs, files in os.walk("pipeline"):
        for file in files:
            if file.endswith(".ipynb"):
                notebook_count += 1
    
    print(f"\nTotal notebooks in pipeline: {notebook_count}")
    print("Expected: 13 analysis notebooks + 1 main pipeline = 14 total")
    
    return notebook_count

if __name__ == "__main__":
    # Change to project root directory
    script_dir = Path(__file__).parent.parent
    os.chdir(script_dir)
    
    success = verify_pipeline_structure()
    notebook_count = count_notebooks()
    
    if success and notebook_count >= 14:
        print("\n✅ Integration verification completed successfully!")
    else:
        print("\n⚠️  Integration verification found issues.")
        
    print(f"\nCurrent directory: {os.getcwd()}")
    print("Run this script from the project root directory.")
