# LLMFlow
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/your-username/your-repo/blob/main/LICENSE.md)
[![PyPI version](https://badge.fury.io/py/llmflow.svg)](https://badge.fury.io/py/llmflow)
[![Documentation](https://img.shields.io/badge/documentation-llmflow.com-blue.svg)](https://llmflow.com/docs)

[![Build Status](https://img.shields.io/github/workflow/status/cedkoffeto/llmflow/CI)](https://github.com/cedkoffeto/llmflow/actions)




`LLMFlow` is an open-source library that leverages Large Language Models (LLMs) to go beyond traditional machine learning by integrating human domain expertise. Built on top of [LangChain](https://langchain.com), LLMFlow combines the expansive knowledge of LLMs with metadata provided by experts to enhance the accuracy of predictions, classifications, and forecasts. It offers a **scikit-learn-like API** for seamless integration with **DataFrames**.

## Key Features
- **LLMs with Human Expertise**: Combine LLMs' broad general knowledge with domain-specific insights from human experts. The LLMs can access vast contextual information across many fields, while human-provided metadata refines the predictions.
- **scikit-learn Inspired API**: Easily integrate LLMs into your machine learning workflows using a familiar API style, designed for handling both structured and unstructured data.
- **Built on LangChain**: Utilize LangChain’s framework to chain LLM models and automate complex tasks while accessing LLMs’ broad contextual understanding.
- **DataFrame Integration**: Directly handle and manipulate **pandas DataFrames** to fit traditional tabular data while augmenting it with metadata from human experts.
- **Custom Metadata Injection**: Enrich your datasets with human-supplied metadata that reflects domain-specific nuances, improving model predictions beyond what is possible with raw data alone.


## Use Cases
- **Classification**: Easily classify text data with the help of human inputs to fine-tune results.
- **Regression**: Predict complex numerical outcomes by leveraging human analysis to interpret trends.
- **Time Series**: Analyze and forecast time series data while leveraging domain expertise to adjust for outliers.
- **Sentiment Analysis**: Go beyond simple sentiment scores and refine results based on specific human-driven contexts.
- **Anomaly Detection**: Spot anomalies with the added insight of human domain knowledge.

## Installation
Install LLMFlow with pip:
```bash
pip install llmflow
```

## Getting Started
### 1. Simple Text Classification with Human Guidance
```python

import pandas as pd
from llmflow import TextClassifier

# Sample DataFrame with text data
df = pd.DataFrame({
    'text': ['This product is amazing!', 'I had a terrible experience', 'Not bad, but could be better'],
    'label': [1, 0, 1]
})

# Initialize the classifier with a human-in-the-loop approach

classifier = TextClassifier()

# Train the classifier
classifier.fit(df['text'], df['label'])

# Make predictions with optional human analysis
predictions = classifier.predict(['The service was exceptional!'])
print(predictions)
```

### 2. Time Series Forecasting with Expert Input
```python
import pandas as pd
from llmflow import TimeSeriesForecaster

# Sample DataFrame with time-series data
df = pd.DataFrame({
    'date': pd.date_range('2024-01-01', periods=10, freq='D'),
    'value': [10, 12, 14, 15, 16, 15, 14, 13, 16, 18]
})

# Initialize the forecaster
forecaster = TimeSeriesForecaster()

# Train the forecaster
forecaster.fit(df['date'], df['value'])

# Forecast future values with domain knowledge applied
forecast = forecaster.predict(steps=5)
print(forecast)
```

## Documentation
For detailed documentation and examples, visit the LLMFlow Documentation Website.

## Contributing
Contributions are welcome! Please read the CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

---

### **Next Steps**:
1. Set up the initial project structure.
2. Define core API functions for ML tasks.
3. Set up documentation generation using Docusaurus or mkdocs.
4. Start with simple use cases like text classification and anomaly detection.