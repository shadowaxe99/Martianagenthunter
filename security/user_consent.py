```python
import os
import json

class UserConsent:
    def __init__(self):
        self.consent_file = "user_consent.json"

    def check_consent(self):
        if os.path.exists(self.consent_file):
            with open(self.consent_file, 'r') as file:
                consent_data = json.load(file)
                return consent_data.get('consent', False)
        else:
            return False

    def update_consent(self, consent):
        consent_data = {'consent': consent}
        with open(self.consent_file, 'w') as file:
            json.dump(consent_data, file)

    def get_user_consent(self):
        consent = self.check_consent()
        if not consent:
            print("We need your consent to access personal files and information.")
            user_input = input("Do you give your consent? (yes/no): ")
            if user_input.lower() == 'yes':
                self.update_consent(True)
                print("Thank you for your consent.")
            else:
                print("Without your consent, some functionalities might not work.")
        return consent
```