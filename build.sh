#!/bin/bash

# Root directory of the project
mkdir llmflow

# Documentation folder
mkdir -p llmflow/docs/api
mkdir -p llmflow/docs/tutorials

# Core library folder
mkdir -p llmflow/llmflow/models
mkdir -p llmflow/llmflow/pipelines
mkdir -p llmflow/llmflow/preprocessing
mkdir -p llmflow/llmflow/transformers
mkdir -p llmflow/llmflow/evaluation
mkdir -p llmflow/llmflow/utils
mkdir -p llmflow/llmflow/datasets

# Tests folder
mkdir -p llmflow/tests

# Examples folder
mkdir -p llmflow/examples

# Website folder (for Docusaurus or similar)
mkdir -p llmflow/website/build
mkdir -p llmflow/website/public
mkdir -p llmflow/website/src

# Create files for project configuration and code quality
touch llmflow/.pre-commit-config.yaml
touch llmflow/.flake8
touch llmflow/pyproject.toml
touch llmflow/setup.py
touch llmflow/README.md
touch llmflow/CONTRIBUTING.md
touch llmflow/LICENSE

# Initialize __init__.py for all Python packages in core library
touch llmflow/llmflow/__init__.py
touch llmflow/llmflow/models/__init__.py
touch llmflow/llmflow/pipelines/__init__.py
touch llmflow/llmflow/preprocessing/__init__.py
touch llmflow/llmflow/transformers/__init__.py
touch llmflow/llmflow/evaluation/__init__.py
touch llmflow/llmflow/utils/__init__.py
touch llmflow/llmflow/datasets/__init__.py

# Create model files
touch llmflow/llmflow/models/classification.py
touch llmflow/llmflow/models/regression.py
touch llmflow/llmflow/models/time_series.py
touch llmflow/llmflow/models/sentiment.py
touch llmflow/llmflow/models/anomaly_detection.py

# Create pipeline files
touch llmflow/llmflow/pipelines/classification_pipeline.py
touch llmflow/llmflow/pipelines/regression_pipeline.py
touch llmflow/llmflow/pipelines/time_series_pipeline.py
touch llmflow/llmflow/pipelines/custom_pipeline.py

# Create preprocessing files
touch llmflow/llmflow/preprocessing/text_preprocessing.py
touch llmflow/llmflow/preprocessing/feature_scaling.py
touch llmflow/llmflow/preprocessing/time_series_prep.py

# Create transformer files
touch llmflow/llmflow/transformers/text_transformer.py
touch llmflow/llmflow/transformers/feature_transformer.py

# Create evaluation files
touch llmflow/llmflow/evaluation/classification_metrics.py
touch llmflow/llmflow/evaluation/regression_metrics.py
touch llmflow/llmflow/evaluation/custom_metrics.py

# Create utility files
touch llmflow/llmflow/utils/data_utils.py
touch llmflow/llmflow/utils/logger.py
touch llmflow/llmflow/utils/config_loader.py

# Create dataset files
touch llmflow/llmflow/datasets/text_datasets.py
touch llmflow/llmflow/datasets/time_series_datasets.py
touch llmflow/llmflow/datasets/anomaly_datasets.py

# Create test files
touch llmflow/tests/test_classification.py
touch llmflow/tests/test_regression.py
touch llmflow/tests/test_pipelines.py
touch llmflow/tests/test_preprocessing.py
touch llmflow/tests/test_transformers.py

# Create example notebooks
touch llmflow/examples/classification.ipynb
touch llmflow/examples/regression.ipynb
touch llmflow/examples/time_series.ipynb
touch llmflow/examples/anomaly_detection.ipynb

echo "Project structure for LLMFlow created successfully!"
