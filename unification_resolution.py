class DiagnosisSystem:
    def __init__(self):
        self.knowledge_base = {
            'Common Cold': {'cough', 'sneezing', 'fever'},
            'Influenza': {'cough', 'fever', 'body_ache', 'weakness'},
            'Allergy': {'sneezing', 'itchy_eyes', 'nasal_congestion'}
        }
    def diagnose(self, symptoms):
        possible_diseases = []
        for disease, known_symptoms in self.knowledge_base.items():
            if all(symptom in symptoms for symptom in known_symptoms):
                possible_diseases.append(disease)
        return possible_diseases
def interactive_diagnosis():
    system = DiagnosisSystem()

    print("Welcome to the Diagnosis System!")
    print("Please provide the symptoms you are experiencing, separated by commas.")
    user_input = input("Symptoms: ").strip().lower()

    user_symptoms = set(user_input.split(','))

    diagnoses = system.diagnose(user_symptoms)

    if diagnoses:
        print("\nBased on the symptoms you provided, possible conditions may include:")
        for disease in diagnoses:
            print("- " + disease)
        print("\nPlease consult with a healthcare professional for further evaluation.")
    else:
        print("\nNo diagnosis possible based on the provided symptoms.")
        print("It's always a good idea to consult with a healthcare professional.")
if __name__ == "__main__":
    interactive_diagnosis()