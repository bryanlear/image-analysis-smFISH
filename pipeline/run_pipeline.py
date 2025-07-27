#!/usr/bin/env python3
"""
smFISH Analysis Pipeline Runner

This script provides a command-line interface to run the complete smFISH analysis pipeline
or individual stages.

Usage:
    python run_pipeline.py --all                    # Run complete pipeline
    python run_pipeline.py --stage preprocessing    # Run specific stage
    python run_pipeline.py --stage segmentation     # Run specific stage
    python run_pipeline.py --list                   # List available stages

Author: Integrated from original notebooks by John Lee Arboleda
"""

import os
import sys
import argparse
import subprocess
from pathlib import Path

# Define pipeline stages and their notebooks
PIPELINE_STAGES = {
    'preprocessing': [
        '01_preprocessing/1_data_preprocessing.ipynb',
        '01_preprocessing/denoising_fish.ipynb', 
        '01_preprocessing/preprocess_for_training.ipynb'
    ],
    'segmentation': [
        '02_segmentation/2_segmentation.ipynb',
        '02_segmentation/binary_nucleus.ipynb'
    ],
    'training': [
        '03_training/3_model_training.ipynb'
    ],
    'validation': [
        '04_validation/4_1_validation_smfish.ipynb',
        '04_validation/4_2_validation_nucleus.ipynb'
    ],
    'complete_segmentation': [
        '02_segmentation/5_complete_segmentation.ipynb'
    ],
    'analysis': [
        '05_analysis/8_blob_detection.ipynb',
        '05_analysis/9_stats.ipynb'
    ],
    'utilities': [
        '06_utilities/6_generate_outlines.ipynb',
        '06_utilities/7_1_frame_compiler.ipynb',
        '06_utilities/7_2_frame_compiler.ipynb'
    ]
}

# Complete pipeline order
COMPLETE_PIPELINE = [
    'preprocessing',
    'segmentation', 
    'training',
    'validation',
    'complete_segmentation',
    'analysis',
    'utilities'
]

def run_notebook(notebook_path):
    """Run a Jupyter notebook using nbconvert."""
    try:
        print(f"Running {notebook_path}...")
        cmd = [
            'jupyter', 'nbconvert', 
            '--to', 'notebook',
            '--execute',
            '--inplace',
            notebook_path
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✓ Successfully completed {notebook_path}")
            return True
        else:
            print(f"✗ Error running {notebook_path}")
            print(f"Error: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"✗ Exception running {notebook_path}: {e}")
        return False

def run_stage(stage_name):
    """Run all notebooks in a specific stage."""
    if stage_name not in PIPELINE_STAGES:
        print(f"Error: Unknown stage '{stage_name}'")
        print(f"Available stages: {list(PIPELINE_STAGES.keys())}")
        return False
    
    print(f"\n=== Running Stage: {stage_name.upper()} ===")
    notebooks = PIPELINE_STAGES[stage_name]
    
    for notebook in notebooks:
        if not os.path.exists(notebook):
            print(f"Warning: Notebook {notebook} not found, skipping...")
            continue
            
        success = run_notebook(notebook)
        if not success:
            print(f"Pipeline stopped due to error in {notebook}")
            return False
    
    print(f"✓ Stage {stage_name} completed successfully")
    return True

def run_complete_pipeline():
    """Run the complete pipeline in order."""
    print("=== STARTING COMPLETE smFISH ANALYSIS PIPELINE ===")
    
    for stage in COMPLETE_PIPELINE:
        success = run_stage(stage)
        if not success:
            print(f"\nPipeline failed at stage: {stage}")
            return False
    
    print("\n🎉 COMPLETE PIPELINE FINISHED SUCCESSFULLY! 🎉")
    print("\nResults can be found in the 'results/' directory")
    return True

def list_stages():
    """List all available pipeline stages."""
    print("Available pipeline stages:")
    print("=" * 40)
    
    for stage, notebooks in PIPELINE_STAGES.items():
        print(f"\n{stage}:")
        for notebook in notebooks:
            print(f"  - {notebook}")
    
    print(f"\nComplete pipeline order: {' → '.join(COMPLETE_PIPELINE)}")

def main():
    parser = argparse.ArgumentParser(
        description="Run the smFISH analysis pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run_pipeline.py --all                    # Run complete pipeline
  python run_pipeline.py --stage preprocessing    # Run preprocessing only
  python run_pipeline.py --stage analysis         # Run analysis only
  python run_pipeline.py --list                   # List all stages
        """
    )
    
    parser.add_argument('--all', action='store_true',
                       help='Run the complete pipeline')
    parser.add_argument('--stage', type=str,
                       help='Run a specific pipeline stage')
    parser.add_argument('--list', action='store_true',
                       help='List available pipeline stages')
    
    args = parser.parse_args()
    
    # Change to pipeline directory
    pipeline_dir = Path(__file__).parent
    os.chdir(pipeline_dir)
    
    if args.list:
        list_stages()
    elif args.all:
        run_complete_pipeline()
    elif args.stage:
        run_stage(args.stage)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
