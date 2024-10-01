from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.metrics import accuracy_score
from transformers import pipeline
from langchain.llms.base import BaseLLM
from metadatas import BaseMetadata
from langchain.prompts import FewShotPromptTemplate

class LLMBaseClassifier(BaseEstimator, ClassifierMixin):
    """
    Base Classifier that integrates Large Language Models (LLMs) through langchain librarie for classification tasks.
    This class provides a scikit-learn-like API (fit, predict, score) for building classifiers 
    using LLMs, and can be extended by domain-specific models.

    Parameters
    ----------
    llm : LLM
        The Large Language Model to use for classification.
    metadata : Metadata
        The metadata of the target task 
    """
    def __init__(self, llm: BaseLLM, metadata: BaseMetadata):
        self.llm = llm
        self.metadata = metadata

    def fit(self, X, y):
        """
        Fit the model on training data
        The training consist of using llm (langchain) with a specific prompt to get a list of directives or rules
        to be used to classify the data.
        
        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            The input data.
        y : array-like of shape (n_samples,)
            The target values.

        """
        # Create a  langchain prompt that includes the metadata and the data
        prompt = FewShotPromptTemplate(self.metadata, X).generate_prompt()
        # Generate prompt using langchain functions
        prompt = self.llm.generate_prompt(self.metadata, X)

        # Create a chain to process the prompt and get the output text
        chain = pipeline("text-generation", model=self.llm.model)
        output = chain(prompt, max_length=100)[0]['generated_text']

        # Use the output text as the prompt for classification
        prompt = FewShotPromptTemplate(self.metadata, X).generate_prompt(prompt=output)
        
        

    def predict(self, X):
        """
        Predict the target values for the input data.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            The input data.

        Returns
        -------
        y : array-like of shape (n_samples,)
            The predicted target values.
        """
        return self.clf(X)

    def score(self, X, y):
        """
        Compute the accuracy of the model on the input data.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            The input data.
        y : array-like of shape (n_samples,)
            The target values.

        Returns
        -------
        score : float
            The accuracy of the model.
        """
        y_pred = self.predict(X)
        return accuracy_score(y, y_pred)
    
 