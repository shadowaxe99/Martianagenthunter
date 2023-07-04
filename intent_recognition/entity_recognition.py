```python
import spacy

class EntityRecognition:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def extract_entities(self, user_input):
        doc = self.nlp(user_input)
        entities = {ent.label_: ent.text for ent in doc.ents}
        return entities
```