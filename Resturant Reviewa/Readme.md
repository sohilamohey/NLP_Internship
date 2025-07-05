# Sentiment Analysis for Text Reviews

This project implements a machine learning model for sentiment analysis, classifying English text reviews as Positive (1) or Negative (0). It uses Python with scikit-learn, NLTK, and pandas for preprocessing, feature extraction, and classification.

## Overview

The model processes a dataset of pre-cleaned English reviews and their sentiment labels. It employs a pipeline with TfidfVectorizer for feature extraction, SelectKBest for feature selection, and LinearSVC for classification. Hyperparameter tuning is performed using GridSearchCV.

## Features

### Preprocessing: Lowercasing, punctuation removal, and negation handling (e.g., "not bad" → "not_bad").

### Feature Extraction: TF-IDF with unigrams, bigrams, and sublinear term frequency scaling.

### Feature Selection: Chi-squared to select top 3000 features.

## Model: LinearSVC with balanced class weights.

### Evaluation: Accuracy, precision, recall, F1-score, and confusion matrix.

### Test Function: Predicts sentiment for new reviews with confidence scores.

## Results

The model was trained on a balanced dataset (100 positive, 100 negative reviews in the test set). Below are the results:

## Dataset:
 From Kaggle <https://www.kaggle.com/datasets/mdtamzidulislam/resturant-reviews>

## Best Parameters (from GridSearchCV):
clf__C: 0.1
tfidf__max_features: 3000
tfidf__ngram_range: (1, 2)
Cross-Validation Accuracy: 76.63%


# Test Accuracy: 78.5%