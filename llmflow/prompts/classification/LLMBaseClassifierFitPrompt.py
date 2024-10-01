from langchain.prompts import FewShotPromptTemplate
import pandas as pd
import json

class MetadataFewShotPromptTemplate(FewShotPromptTemplate):
    def __init__(self, learned_rules: dict, metadata: dict, **kwargs):
        """
        :param learned_rules: Previously learned rules in the format {X_column_name: Y_rule}
        :param metadata: Metadata to guide the modification of previous rules or addition of new rules
        :param kwargs: Other parameters for FewShotPromptTemplate (like examples, prompt template, etc.)
        """
        super().__init__(**kwargs)
        self.learned_rules = learned_rules
        self.metadata = metadata

    def generate_prompt(self, x_batch: pd.DataFrame, y_batch: pd.Series) -> str:
        """
        Generates a prompt to update the learned knowledge based on new mini-batch data and metadata.

        :param x_batch: pandas DataFrame, mini-batch dataset (X) 
        :param y_batch: pandas Series, mini-batch target values (y) for classification
        :return: Generated prompt as a string
        """
        # Reference the existing rules
        prompt = "The model has previously learned the following rules:\n"
        for x_col, rule in self.learned_rules.items():
            prompt += f"- If {x_col}, then {rule}\n"
        
        # Add metadata information for context
        prompt += "\nThe following metadata is provided to modify or update the rules:\n"
        for meta_key, meta_value in self.metadata.items():
            prompt += f"- {meta_key}: {meta_value}\n"

        # Incorporate the new batch of data
        prompt += "\nNew data samples and their target classes are as follows:\n"
        for idx, row in x_batch.iterrows():
            x_str = ', '.join([f"{col}={val}" for col, val in row.items()])
            y_value = y_batch.iloc[idx]
            prompt += f"- {x_str} -> target: {y_value}\n"
        
        # Directive to output new rules in a structured format
        prompt += (
            "\nBased on this new data and metadata, please update the existing rules or "
            "add new rules. Output the updated rules in the following structured format (JSON):\n\n"
            "{\n"
            '  "updated_rules": {\n'
            '    "feature_name": "rule_description",\n'
            '    "...": "..."   # additional rules here\n'
            "  }\n"
            "}"
        )
        
        return prompt
