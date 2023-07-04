```python
import spacy

class NLPModule:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def process_input(self, user_input):
        doc = self.nlp(user_input)
        return doc

    def get_entities(self, doc):
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        return entities

    def get_tokens(self, doc):
        tokens = [(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
                token.shape_, token.is_alpha, token.is_stop) for token in doc]
        return tokens
```