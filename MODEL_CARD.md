---
library_name: transformers
tags:
- text-classification
- spanish
- conflict-detection
- xlm-roberta
language:
- es
---

# Model Card for XLM-RoBERTa Spanish Conflict Detection Classifier

<!-- Quick summary of what the model is/does. -->

A fine-tuned XLM-RoBERTa model for detecting social conflict mentions in Spanish news articles. The model is trained on the "Conflicto Social en Noticias" dataset and achieves 91.07% macro-F1 score on test data, making it suitable for automated content classification and conflict-related news filtering.

## Model Details

### Model Description

<!-- Longer summary of what this model is. -->

This is a binary text classification model based on **FacebookAI/xlm-roberta-base** fine-tuned to detect whether Spanish news articles discuss social conflict or not. The model was trained using a rigorous multi-seed approach (10 random seeds) to ensure robustness and generalization.

The classification task is binary:
- **CONFLICTO** (1): News articles that discuss social conflict
- **NO_CONFLICTO** (0): News articles that do not discuss social conflict

The model achieved strong performance across multiple evaluation runs, with consistent metrics indicating reliable predictions on unseen test data.

### Model Details

- **Developed by:** Germán Rosati (Factor~Data, SICSS-Buenos Aires)
- **Model type:** Transformer-based text classification
- **Language(s) (NLP):** Spanish (es)
- **License:** MIT
- **Finetuned from model:** [FacebookAI/xlm-roberta-base](https://huggingface.co/FacebookAI/xlm-roberta-base)

### Model Sources

- **Repository:** https://github.com/gefero/factor_data_tuto_NLP_SICSS
- **Dataset:** [agusnieto77/conflicto-social-noticias-4034](https://huggingface.co/datasets/agusnieto77/conflicto-social-noticias-4034)

## Uses

### Direct Use

This model can be used for:

- **Automated news classification:** Identify news articles discussing social conflict in Spanish-language sources
- **Content moderation:** Flag conflict-related content for review or categorization
- **News aggregation:** Filter and organize news by conflict relevance
- **Research and analytics:** Systematic analysis of conflict coverage in news media
- **Social media monitoring:** Detect posts discussing social conflict

### Downstream Use [optional]

This model can be integrated into:

- News recommendation systems to provide conflict-focused news feeds
- Content management systems for automated news categorization
- Data pipelines for media analysis research
- Misinformation detection systems (as a conflict-detection component)

### Out-of-Scope Use

This model is **not suitable for:**

- Languages other than Spanish (though XLM-RoBERTa is multilingual, the model was fine-tuned only on Spanish data)
- Content moderation decisions without human review (should be used as a scoring/filtering tool, not final arbiter)
- Real-time moderation of live content streams without performance testing in your specific domain
- Classification of informal text, social media, or user-generated content not resembling news articles (model trained on news)

## Bias, Risks, and Limitations

### Limitations

1. **Language:** Model trained exclusively on Spanish news articles. Performance on other languages or dialects is unknown.

2. **Domain:** Model trained on news articles. Performance on other text types (social media, academic text, etc.) may be degraded.

3. **Temporal bias:** Dataset represents a specific time period. Linguistic evolution and emerging conflict narratives may not be captured.

4. **Class balance:** Dataset contains both conflict and non-conflict examples. Performance may vary based on class distribution in your specific use case.

5. **Truncation:** Text is truncated to 256 tokens (matching model's training setup). Very long articles may lose important context.

6. **Context sensitivity:** "Conflict" detection is based on textual patterns. Sarcasm, irony, or indirect references may be misclassified.

### Risks and Biases

- **Labeling bias:** Model inherits any biases present in the original dataset annotation process
- **Geographic bias:** News sources and conflict types in training data may not represent all Spanish-speaking regions equally
- **Media bias:** Model trained on news articles, which may have their own coverage biases
- **Potential overreach:** Model might flag articles mentioning conflict in non-concerning contexts (e.g., historical analysis, conflict resolution discussion)

### Recommendations

1. **Always validate:** Test the model on your specific data before production deployment
2. **Human review:** Use model predictions as a starting point for human review, not as final decisions
3. **Monitor performance:** Track model performance over time and across different domains
4. **Document decisions:** Keep clear records of how the model is being used and any adjustments made
5. **Consider context:** Combine model predictions with other signals for robust classification decisions

## How to Get Started with the Model

### Installation

```bash
pip install transformers torch
```

### Quickstart - Using the Pipeline API

```python
from transformers import pipeline

# Initialize the model
classifier = pipeline(
    "text-classification",
    model="gefero/conflict_detection_ROBERTA_based"
)

# Classify text
texts = [
    "El gobierno anunció nuevas políticas de seguridad social",
    "Miles de personas protestaron en las calles contra las medidas económicas"
]

results = classifier(texts)
for text, result in zip(texts, results):
    print(f"Text: {text[:50]}...")
    print(f"Label: {result['label']} (score: {result['score']:.4f})\n")
```

### Quickstart - Using the Model Directly

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "gefero/conflict_detection_ROBERTA_based"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Prepare input
text = "Manifestantes se enfrentan con la policía"
inputs = tokenizer(
    text,
    truncation=True,
    padding="max_length",
    max_length=256,
    return_tensors="pt"
)

# Get predictions
with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits
    predictions = torch.argmax(logits, dim=-1)
    confidence = torch.softmax(logits, dim=-1).max().item()

labels = {0: "NO_CONFLICTO", 1: "CONFLICTO"}
print(f"Prediction: {labels[predictions.item()]} (confidence: {confidence:.4f})")
```

## Training Details

### Training Data

- **Dataset:** [agusnieto77/conflicto-social-noticias-4034](https://huggingface.co/datasets/agusnieto77/conflicto-social-noticias-4034)
- **Language:** Spanish (es)
- **Domain:** News articles
- **Splits used:**
  - Training set: 70% (~2,823 examples)
  - Development set: 10% (~403 examples)
  - Test set: 20% (~806 examples)

### Training Procedure

#### Preprocessing

- **Tokenization:** XLM-RoBERTa tokenizer
- **Max length:** 256 tokens (increased from default 128 to capture longer articles)
- **Truncation:** Long articles truncated to max_length
- **Padding:** Padded to max_length for batch processing

#### Training Hyperparameters

- **Base model:** FacebookAI/xlm-roberta-base
- **Learning rate:** 2e-5
- **Batch size:** 16 (training), 64 (evaluation)
- **Epochs:** 5
- **Weight decay:** 0.01
- **Warmup steps:** 0.1 (proportion of total training steps)
- **Evaluation strategy:** Evaluate at the end of each epoch
- **Best model selection:** Based on macro-F1 on development set
- **Hardware:** GPU with FP16 (mixed precision) when available
- **Random seeds:** 10 seeds [0, 1, 7, 13, 42, 100, 123, 2024, 31337, 65535] for robust evaluation

#### Training Details

- **Framework:** Hugging Face Transformers
- **Optimizer:** AdamW (default)
- **Metric for best model:** macro-F1 (average of precision and recall across both classes)
- **Multi-seed training:** Model was trained 10 times with different random seeds to ensure robustness and to provide confidence intervals on performance metrics

## Evaluation

### Testing Data, Factors & Metrics

#### Testing Data

- **Split:** Test set (20% of original data, stratified split)
- **Size:** ~806 examples
- **Language:** Spanish
- **Domain:** News articles from the original dataset

#### Metrics

- **Macro-F1** (primary metric): Average F1-score across both classes
  - Used for model selection during training
  - Balances precision and recall
  - Better for imbalanced or binary classification tasks
  
- **Accuracy:** Overall correctness of predictions
- **F1-CONFLICTO:** F1-score specifically for the CONFLICTO class (conflict-related news)
- **Precision:** True positives / (true positives + false positives)
- **Recall:** True positives / (true positives + false negatives)

### Results

#### Official Test Results (10 runs with different seeds)

| Metric | Mean | Std Dev | Min | Max |
|--------|------|---------|-----|-----|
| **Test Macro-F1** | 0.9107 | 0.0071 | 0.8999 | 0.9204 |
| **Test Accuracy** | 0.9394 | 0.0053 | 0.9319 | 0.9468 |
| **Test F1-CONFLICTO** | 0.8602 | 0.0108 | 0.8433 | 0.8746 |
| **Test Precision** | 0.8807 | 0.0296 | 0.8307 | 0.9182 |
| **Test Recall** | 0.8419 | 0.0247 | 0.8156 | 0.8883 |

#### Per-Seed Results

| Seed | Dev Macro-F1 | Test Macro-F1 | Test Accuracy | Test F1-CONFLICTO | Test Precision | Test Recall |
|------|--------------|---------------|---------------|-------------------|----------------|-------------|
| 0 | 0.9113 | 0.9007 | 0.9332 | 0.8439 | 0.8743 | 0.8156 |
| 1 | 0.9116 | 0.8999 | 0.9319 | 0.8433 | 0.8605 | 0.8268 |
| 7 | 0.8975 | 0.9092 | 0.9381 | 0.8580 | 0.8728 | 0.8436 |
| 13 | 0.9187 | 0.9140 | 0.9431 | 0.8639 | 0.9182 | 0.8156 |
| 42 | 0.9154 | 0.9127 | 0.9418 | 0.8622 | 0.9074 | 0.8212 |
| 100 | 0.9219 | 0.9136 | 0.9394 | 0.8665 | 0.8457 | 0.8883 |
| 123 | 0.9146 | 0.9194 | 0.9455 | 0.8736 | 0.8994 | 0.8492 |
| 2024 | 0.9098 | 0.9125 | 0.9406 | 0.8629 | 0.8830 | 0.8436 |
| 31337 | 0.9180 | 0.9204 | 0.9468 | 0.8746 | 0.9146 | 0.8380 |
| 65535 | 0.9168 | 0.9050 | 0.9332 | 0.8533 | 0.8307 | 0.8771 |

#### Summary

The model demonstrates **excellent performance** with:
- **High macro-F1 (0.91):** Balanced and strong predictions on both classes
- **High accuracy (0.94):** Correct classification in 94% of cases
- **Robust across seeds:** Low standard deviation indicates consistent generalization
- **Strong conflict detection (F1-CONFLICTO: 0.86):** Reliably identifies conflict-related news

## Environmental Impact

### Compute Infrastructure

#### Hardware

- **GPU:** NVIDIA GPU (exact model unspecified, but typical for Colab)
- **CPU:** Supporting processors on Colab infrastructure
- **RAM:** Standard Colab allocation

#### Training Time

- **Per seed:** ~5-10 minutes (5 epochs per training run)
- **Total:** ~50-100 minutes for 10 complete runs
- **Cloud Platform:** Google Colaboratory (free tier)

#### Carbon Emissions

Estimated CO2 emissions for multi-seed training approach: **Low to minimal** (Colab's data centers use renewable energy sources). Individual training runs are short (~10 min each) and performed on highly optimized infrastructure.

For detailed calculations, see [ML Impact Calculator](https://mlco2.github.io/impact#compute).

## Technical Specifications

### Model Architecture and Objective

- **Architecture:** Transformer-based sequence classification
  - Base: XLM-RoBERTa (12 layers, 768 hidden dimensions, 110M parameters)
  - Task-specific layer: Linear classification head for 2 classes
  
- **Objective:** Binary cross-entropy loss (standard for text classification)

- **Multilingual base:** XLM-RoBERTa trained on 100+ languages, fine-tuned here for Spanish-specific conflict detection

### Input/Output

- **Input:** Spanish text (news articles)
- **Max length:** 256 tokens
- **Output:** Class probabilities for [NO_CONFLICTO, CONFLICTO]

## Citation [optional]

If you use this model in research, please cite:

**BibTeX:**

```bibtex
@software{rosati2024conflictdetection,
  author = {Rosati, Germán},
  title = {XLM-RoBERTa Spanish Conflict Detection Classifier},
  year = {2024},
  publisher = {Hugging Face Hub},
  url = {https://huggingface.co/gefero/conflict_detection_ROBERTA_based}
}
```

**APA:**

Rosati, G. (2024). XLM-RoBERTa Spanish Conflict Detection Classifier [Machine learning model]. Hugging Face Hub. Retrieved from https://huggingface.co/gefero/conflict_detection_ROBERTA_based

## Model Card Authors

- **Germán Rosati** (Factor~Data, SICSS-Buenos Aires)

## Model Card Contact

- **Email:** german.rosati@gmail.com
- **GitHub:** https://github.com/gefero
