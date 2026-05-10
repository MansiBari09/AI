# Hospital Expert System (Python version of Java code)

class Patient:

    def __init__(self, name, age, symptoms):
        self.name = name
        self.age = age
        self.symptoms = symptoms
        self.diagnosis = None
        self.doctor = None
        self.medicine = None

    def display_info(self):

        print("\nPatient Name:", self.name)
        print("Age:", self.age)

        print("Symptoms:", end=" ")
        for s in self.symptoms:
            print(s, end=", ")
        print()

        print("Diagnosis:", self.diagnosis if self.diagnosis else "Not diagnosed")
        print("Assigned Doctor:", self.doctor if self.doctor else "Not assigned")
        print("Suggested Medicine:", self.medicine if self.medicine else "Not prescribed")


class HospitalExpertSystem:

    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)
        self.diagnose_patient(patient)

    def diagnose_patient(self, patient):

        fever = cough = fatigue = headache = stomachPain = 0

        for symptom in patient.symptoms:

            s = symptom.lower().strip()

            if "fever" in s:
                fever += 1
            if "cough" in s or "couph" in s:
                cough += 1
            if "fatigue" in s:
                fatigue += 1
            if "headache" in s:
                headache += 1
            if "stomach" in s:
                stomachPain += 1

        # Rule-based diagnosis

        if fever > 0 and cough > 0 and fatigue > 0:
            patient.diagnosis = "Influenza (Flu)"
            patient.doctor = "Dr. Sharma (General Physician)"
            patient.medicine = "Paracetamol, Cough Syrup"

        elif fever > 0 and headache > 0:
            patient.diagnosis = "Migraine or Viral Fever"
            patient.doctor = "Dr. Gupta (Neurologist)"
            patient.medicine = "Ibuprofen"

        elif stomachPain > 0 and fatigue > 0:
            patient.diagnosis = "Gastritis or Food Poisoning"
            patient.doctor = "Dr. Patel (Gastroenterologist)"
            patient.medicine = "Antacid, Hydration Fluids"

        elif cough > 0 and fatigue > 0:
            patient.diagnosis = "Common Cold"
            patient.doctor = "Dr. Singh (General Physician)"
            patient.medicine = "Cough Drops, Rest"

        elif fever > 0 and stomachPain > 0:
            patient.diagnosis = "Possible Stomach Infection"
            patient.doctor = "Dr. Patel (Gastroenterologist)"
            patient.medicine = "Antacid, Paracetamol"

        elif cough > 0:
            patient.diagnosis = "Mild Cough"
            patient.doctor = "Dr. Singh (General Physician)"
            patient.medicine = "Cough Drops"

        else:
            patient.diagnosis = "Unable to determine. Consult a specialist."
            patient.doctor = "Not Assigned"
            patient.medicine = "Not Prescribed"

    def display_all_patients(self):

        if len(self.patients) == 0:
            print("No patients in the system.")
            return

        print("\n------ All Patients ------")

        for p in self.patients:
            p.display_info()


# ---------------- MAIN PROGRAM ----------------

def main():

    hospital = HospitalExpertSystem()

    print("Welcome to Hospital Expert System")

    while True:

        print("\n1. Add New Patient")
        print("2. Display All Patients")
        print("3. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:

            name = input("Enter name: ")
            age = int(input("Enter age: "))

            input_symptoms = input("Enter symptoms (comma separated): ")
            symptoms = [s.strip() for s in input_symptoms.split(",")]

            patient = Patient(name, age, symptoms)

            hospital.add_patient(patient)

            print("Patient added successfully!")
            patient.display_info()

        elif choice == 2:

            hospital.display_all_patients()

        elif choice == 3:

            print("Exiting...")
            break

        else:

            print("Invalid choice!")


main()