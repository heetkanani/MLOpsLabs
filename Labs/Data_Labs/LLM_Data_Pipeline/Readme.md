# Lab 1: Language Model Data Preprocessing Pipeline

## Overview

This lab implements an end-to-end data preprocessing pipeline for training transformer-based language models. The pipeline loads the WikiText-2 dataset, performs exploratory analysis with visualizations, tokenizes text using GPT-2's BPE tokenizer, groups tokens into fixed-length sequences, and wraps everything in a PyTorch DataLoader ready for causal language model training.

Designed to run on Google Colab with GPU support.

## Quick Start

1. Upload `Lab1.ipynb` to Google Colab
2. Enable GPU: Runtime → Change runtime type → GPU → Save
3. Run all cells: Runtime → Run all
4. Wait for completion: First run downloads the dataset (~1-2 min)

Expected runtime: 3-5 minutes for complete pipeline execution

## Dataset

**WikiText-2** (`wikitext-2-raw-v1`)
- Collection of featured articles from Wikipedia
- Training set: 36,718 lines
- Validation set: 3,760 lines
- Test set: 4,358 lines

## Pipeline Flow

### 1. Environment Setup
- Install required packages (transformers, torch, datasets, matplotlib, seaborn)
- Import libraries and set random seeds for reproducibility

### 2. Dataset Loading
- Load WikiText-2 dataset (train, validation, test splits)
- Print split sizes for verification

### 3. Dataset Exploration & Visualization
- Identify empty vs non-empty lines in the corpus
- Compute text length statistics (mean, median)
- Visualizations:
  - Text length distribution histogram with mean marker
  - Top 20 most frequent words (horizontal bar chart)

### 4. Tokenizer Configuration
- Initialize GPT-2 tokenizer (Byte Pair Encoding)
- Assign `eos_token` as `pad_token`
- Demo tokenization on a sample sentence showing tokens and IDs

### 5. Batch Tokenization
- Apply tokenizer across full dataset using `.map()` with batched processing
- Generate `input_ids` and `attention_mask` columns
- Locate and display a non-empty tokenized example with decoded text

### 6. Token Frequency Analysis & Visualization
- Count total and unique tokens in the corpus
- Calculate vocabulary coverage percentage
- Print top 10 most frequent tokens
- Visualizations:
  - Zipf's Law plot (log-log rank vs frequency)
  - Token frequency distribution histogram (log scale)

### 7. Sequence Grouping
- Concatenate all token streams into a single sequence
- Split into non-overlapping fixed-size blocks (128 tokens)
- Discard leftover tokens that don't fill a complete block

### 8. DataLoader Configuration
- Custom collate function to stack sequences and create labels
- Shuffle enabled for training
- `drop_last=True` for consistent batch shapes

### 9. Validation
- Verify tensor shapes and data types
- Assert sequence length matches `block_size`
- Decode a token snippet for coherence check
- Print final pipeline summary

## Configuration Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| block_size | 128 | Sequence length for training |
| batch_size | 8 | Training batch size |
| random_seed | 42 | Seed for reproducibility |

## Output Summary

### Processed Data
- Training sequences: ~18,667 sequences
- Sequence length: 128 tokens each
- Total training tokens: ~2,389,376 tokens
- Batches per epoch: ~2,333 batches (with batch_size=8)

### Analysis Results
- Non-empty line ratio and text length statistics
- Token frequency distributions
- Vocabulary coverage percentage
- Top frequent words and tokens

### Visualizations
- Text length distribution (histogram)
- Top 20 most frequent words (bar chart)
- Zipf's Law: token rank vs frequency (log-log plot)
- Token frequency distribution (log-scale histogram)

## Architecture

```
Raw Text (WikiText-2)
    ↓
Dataset Loading (train / val / test)
    ↓
Exploratory Analysis & Visualizations
    ↓
Tokenizer Setup (GPT-2 BPE)
    ↓
Batch Tokenization
    ↓
Token Frequency Analysis & Visualizations
    ↓
Sequence Grouping (128-token blocks)
    ↓
DataLoader with Custom Collation
    ↓
Validation & Shape Checks
    ↓
Ready for Model Training
```