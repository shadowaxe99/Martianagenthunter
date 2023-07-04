```python
import spacy

class IntentClassifier:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def classify_intent(self, user_input):
        doc = self.nlp(user_input)
        intents = {
            'set_meeting': ['meeting', 'schedule', 'appointment'],
            'edit_file': ['edit', 'change', 'modify'],
            'combine_folder': ['combine', 'merge', 'join'],
            'set_reminder': ['reminder', 'remind', 'alarm'],
            'send_invite': ['invite', 'send', 'mail'],
            # Add more intents as per requirement
        }

        for intent, keywords in intents.items():
            if any(token.lemma_ in keywords for token in doc):
                return intent

        return 'unknown_intent'

if __name__ == "__main__":
    classifier = IntentClassifier()
    user_input = input("Enter your command: ")
    intent = classifier.classify_intent(user_input)
    print(f"Identified intent: {intent}")
```