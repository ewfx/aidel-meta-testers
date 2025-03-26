from transformers import pipeline
import re

# Load Named Entity Recognition (NER) model
ner_pipeline = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")

def extract_entities(text):
    """
    Extracts organization names from unstructured text using NLP.
    """
    entities = [entity['word'] for entity in ner_pipeline(text) if entity['entity'].startswith("B-ORG")]
    
    # Clean extracted names
    cleaned_entities = list(set(re.sub(r"[^a-zA-Z0-9\s]", "", entity).strip() for entity in entities))
    
    return [entity for entity in cleaned_entities if entity]  # Remove empty strings

# Example usage
if __name__ == "__main__":
    sample_text = "Payment to ABC Corp and XYZ Non-Profit on Jan 5."
    print(extract_entities(sample_text))  # Output: ['ABC Corp', 'XYZ Non-Profit']
