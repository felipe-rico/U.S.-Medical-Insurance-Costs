import csv

insurance_info = '/Users/Felipe/Documents/Computer Programming/Jupyter Notebook Projects/U.S. Medical Insurance Costs/Insurance.csv'

ages = []
sexes = []
bmis = []
num_children = []
smoker_statuses = []
regions = []
insurance_charges = []

def load_list_data(lst, csv_file, column_name):
    with open(csv_file) as csv_info:
        csv_dict = csv.DictReader(csv_info)
        for row in csv_dict:
            lst.append(row[column_name])
        return lst

load_list_data(ages, insurance_info, 'age')
load_list_data(sexes, insurance_info, 'sex')
load_list_data(bmis, insurance_info, 'bmi')
load_list_data(num_children, insurance_info, 'children')
load_list_data(smoker_statuses, insurance_info, 'smoker')
load_list_data(regions, insurance_info, 'region')
load_list_data(insurance_charges, insurance_info, 'charges')

class PatientsInfo:
    def __init__(self, patients_ages, patients_sexes, patients_bmis, patients_num_children, patients_smoker_statuses, patients_regions, patients_charges):
        self.patients_ages = patients_ages
        self.patients_sexes = patients_sexes
        self.patients_bmis = patients_bmis
        self.patients_num_children = patients_num_children
        self.patients_smoker_statuses = patients_smoker_statuses
        self.patients_regions = patients_regions
        self.patients_charges = patients_charges

    def analyze_ages(self):
        age_sum = 0
        for age in self.patients_ages:
            age_sum += int(age)
        return "Average Patient Age: " + str(round(age_sum / len(self.patients_ages), 2)) + " years"

    def analyze_sexes(self):
        female_count = 0
        male_count = 0
        for sex in self.patients_sexes:
            if sex == "female":
                female_count += 1
            elif sex == "male":
                male_count += 1
        return "Count for female: " + str(female_count) + "\nCount for male: " + str(male_count)

    def unique_regions(self):
        unique_regions = []
        for region in self.patients_regions:
            if region not in unique_regions:
                unique_regions.append(region)
        return "Unique Regions: " + str(unique_regions)

    def average_charges(self):
        charge_sum = 0
        for charge in self.patients_charges:
            charge_sum += float(charge)
        return "Average Yearly Medical Insurance Charges: " + str(round(charge_sum / len(self.patients_charges), 2)) + " dollars"

    def create_dictionary(self):
        self.patients_dictionary = {}
        self.patients_dictionary["age"] = [int(age) for age in self.patients_ages]
        self.patients_dictionary["sex"] = self.patients_sexes
        self.patients_dictionary["bmi"] = [float(bmi) for bmi in self.patients_bmis]
        self.patients_dictionary["children"] = [int(num_children) for num_children in self.patients_num_children]
        self.patients_dictionary["smoker"] = self.patients_smoker_statuses
        self.patients_dictionary["regions"] = self.patients_regions
        self.patients_dictionary["charges"] = [float(charge) for charge in self.patients_charges]
        return self.patients_dictionary

patient_info = PatientsInfo(ages, sexes, bmis, num_children, smoker_statuses, regions, insurance_charges)

# print(patient_info.analyze_ages())
# print(patient_info.analyze_sexes())
# print(patient_info.unique_regions())
# print(patient_info.average_charges())
# print(patient_info.create_dictionary())