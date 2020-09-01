import random
import json
import getopt
from sys import argv
from faker import Faker

from data_dictionary import DATA_DICTIONARY


fake = Faker()
Faker.seed(42)


HOSPITAL_NAME_WORDS = ["University", "Central", "Northwestern", "Central South", "Main", "General"]


def random_choice_generic(name: str):
    """ Random choice from yes_no etc. options. """

    return random.choice(DATA_DICTIONARY[name])[1]


def random_choice_cv(element1, element2):
    """ Random choice from Controlled vocabularies. """

    return random.choice(DATA_DICTIONARY[element1][element2])[1]


def generate_cancogen_data():
    """ Generates random choices from DATA_DICTIONARY using uniform distribution. """

    data = {
        "identification": {
            "institution_location": str(random.choice(HOSPITAL_NAME_WORDS)) + " Hospital",
            "case_id": fake.ssn()
        },
        "demographics": {
            "age": str(fake.date_of_birth(minimum_age=20, maximum_age=100)),
            "sex": random_choice_cv("demographics", "sex"),
            "ancestry": random_choice_cv("demographics", "ancestry"),
            "country_of_birth": "",
            "height": f"{str(random.randrange(150, 190))} cm",
            "weight": f"{str(random.randrange(50, 190))} Kg",
            "education": random_choice_cv("demographics", "education"),
            "employment": random_choice_cv("demographics", "employment"),
            "household": "",
            "pregnancy_weeks": ""
        },
        "vital_status": {
            "ambulatory": random_choice_cv("vital_status", "ambulatory")
        },
        "risk_factors": {
            "history_of_smoking": random_choice_cv("risk_factors", "history_of_smoking"),
            "rate_of_smoking": random_choice_cv("risk_factors", "rate_of_smoking"),
            "vaping": random_choice_cv("risk_factors", "vaping"),
            "cannabis": random_choice_cv("risk_factors", "cannabis")
        },
        "comorbidities": {
            "immune_system": {
                "hiv": random_choice_generic("yes_no_dontknow"),
                "hiv_viral_load": "see lab tests",
                "immunocompromised_status": random_choice_generic("yes_no_dontknow"),
                "days_from_onset_of_covid19_to_immunocompromisation": "",
                "organ_transplant": random_choice_generic("yes_no_dontknow"),
                "autoimmune_or_rheumatologic_disease": random_choice_generic("yes_no_dontknow"),
                "type_one_diabetes": random_choice_generic("yes_no_dontknow"),
                "type_two_diabetes": random_choice_generic("yes_no_dontknow")
            },
            "respiratory_system": {
                "asthma": random_choice_generic("yes_no_dontknow"),
                "copd": random_choice_generic("yes_no_dontknow"),
                "cystic_fibrosis": random_choice_generic("yes_no_dontknow"),
                "sleep_apnea": random_choice_generic("yes_no_dontknow"),
                "uses_cpap_device": random_choice_generic("yes_no_dontknow")
            },
            "genitourinary_metabolic": {
                "renal_disease": random_choice_generic("yes_no_dontknow"),
                "liver_condition": random_choice_generic("yes_no_dontknow"),
                "callbladder_condition": random_choice_generic("yes_no_dontknow"),
                "pancreas_condition": random_choice_generic("yes_no_dontknow")
            },
            "cardiovascular_system": {
                "angioplasty": random_choice_generic("yes_no_dontknow"),
                "coronary_artery_bypass": random_choice_generic("yes_no_dontknow"),
                "congestive_heart_failure": random_choice_generic("yes_no_dontknow"),
                "hypertension": random_choice_generic("yes_no_dontknow"),
                "myocardial_infarction_type_one": random_choice_generic("yes_no_dontknow"),
                "myocardial_infarction_type_two": random_choice_generic("yes_no_dontknow"),
                "peripheral_vascular_disease": random_choice_generic("yes_no_dontknow"),
                "stroke": random_choice_generic("yes_no_dontknow"),
                "arrythmias": random_choice_generic("yes_no_dontknow")
            },
            "neurological": {
                "dementia": random_choice_generic("yes_no_dontknow"),
                "neurological_neuropsychiatric_condition": random_choice_generic("yes_no_dontknow")
            },
            "cancer": {
                "malignancy": random_choice_generic("yes_no_dontknow"),
                "age_at_diagnosis_with_cancer": "",
                "leukemia": random_choice_generic("yes_no_dontknow"),
                "lymphoma": random_choice_generic("yes_no_dontknow"),
                "sarcoma": random_choice_generic("yes_no_dontknow"),
                "carcinoma": random_choice_generic("yes_no_dontknow"),
                "myeloma": random_choice_generic("yes_no_dontknow"),
                "mixed_types": random_choice_generic("yes_no_dontknow"),
                "location": "",
                "cancer_treatment_in_last_twelve_months": ""
            }
        },
        "symptoms_at_admission_longitudinal": {
            "asymptomatic": random_choice_generic("yes_no"),
            "dry_cough": random_choice_cv("symptoms_at_admission_longitudinal", "dry_cough"),
            "mucus_cough": random_choice_cv("symptoms_at_admission_longitudinal", "mucus_cough"),
            "difficulty_or_pain_with_breathing": random_choice_cv("symptoms_at_admission_longitudinal",
                                                                  "difficulty_or_pain_with_breathing"),
            "wheezing": random_choice_generic("yes_no_dontknow"),
            "fever": f"Temperature {str(round(random.uniform(36.4, 39.5), 1))} C",
            # TODO check
            "days_with_fever": random.choice([f"{str(random.randrange(0, 7))} days", "Don't know"]),
            "heart_rate": f"{str(random.randrange(60, 100))} beats per minute",
            "highest_respiratory_rate": f"{str(random.randrange(10, 20))} breaths per minute",
            "systolic_blood_pressure": f"{str(random.randrange(90, 120, 10))} mmHg",
            "diastolic_blood_pressure": f"{str(random.randrange(60, 80, 10))} mmHg",
            "oxygen_saturation": f"{str(random.randrange(90, 100))} %",
            "oxygen_saturation_on": random_choice_cv("symptoms_at_admission_longitudinal",
                                                     "oxygen_saturation_on"),
            "fatigue": random_choice_generic("yes_no_dontknow"),
            "myalgia": random_choice_generic("yes_no_dontknow"),
            "chest_pain": random_choice_generic("yes_no_dontknow"),
            "ear_pain": random_choice_generic("yes_no_dontknow"),
            "joint_pain": random_choice_generic("yes_no_dontknow"),
            "abdominal_pain": random_choice_generic("yes_no_dontknow"),
            "runny_nose": random_choice_generic("yes_no_dontknow"),
            "nosebleed": random_choice_generic("yes_no_dontknow"),
            "sore_throat": random_choice_generic("yes_no_dontknow"),
            "loss_of_taste_or_smell": random_choice_cv("symptoms_at_admission_longitudinal", "loss_of_taste_or_smell"),
            "diarrhea": random_choice_generic("yes_no_dontknow"),
            "nausea": random_choice_generic("yes_no_dontknow"),
            "conjunctivitis": random_choice_generic("yes_no_dontknow"),
            "headache": random_choice_generic("yes_no_dontknow"),
            "seizures": random_choice_generic("yes_no_dontknow"),
            "bodily_pain": random_choice_generic("yes_no_dontknow"),
            "irritability_or_confusion": random_choice_generic("yes_no_dontknow"),
            "skin_rash": random_choice_generic("yes_no_dontknow"),
            "home_medications": random_choice_cv("symptoms_at_admission_longitudinal", "home_medications"),
            "has_patient_received_bcg_vaccine": random_choice_generic("yes_no_dontknow")
        },
        "hospitalization_information_encounter_complications": {
            "hospitalization": {
                "repeat_hospital_visit_within_30_days": random_choice_generic("yes_no_na"),
                "ct_chest": random_choice_generic("yes_no"),
                "chest_x_ray": random_choice_generic("yes_no"),
                "lung_infilatrates": random_choice_generic("yes_no"),
                "ecg": random_choice_generic("yes_no"),
                "echocardiogram": random_choice_generic("yes_no"),
                "pocus": random_choice_generic("yes_no"),
                "inhaled_no2": random_choice_generic("yes_no_na"),
                "viral_pneumonitis": random_choice_generic("yes_no"),
                "pneumonia": random_choice_generic("yes_no"),
                "cryptogenic_organizing_pneumonia": random_choice_generic("yes_no_na"),
                "bronchiolitis": random_choice_generic("yes_no_na"),
                "pneumothorax": random_choice_generic("yes_no_na"),
                "tracheostomy_inserted": random_choice_generic("yes_no_na"),
                "pancreatitis": random_choice_generic("yes_no_na"),
                "plearal_effusion": random_choice_generic("yes_no_na"),
                "renal_replacement_therapy_or_dialysis": random_choice_generic("yes_no_na"),
                "liver_dysfunction": random_choice_generic("yes_no_na")
            }
        },
        "pathogen_testing": {
            "was_other_pathogen_testing_done_during_this_illness_episode":
                random_choice_cv("pathogen_testing", "was_other_pathogen_testing_done_during_this_illness_episode"),
            "influenza": random_choice_cv("pathogen_testing", "influenza"),
            "coronavirus": random_choice_cv("pathogen_testing", "coronavirus"),
            "rsv": random_choice_generic("yes_no_confirmed_probable"),
            "adenovirus": random_choice_generic("yes_no_confirmed_probable"),
            "enterovirus": random_choice_generic("yes_no_confirmed_probable"),
            "bacteria": random_choice_cv("pathogen_testing", "bacteria"),
            "other_infections_respiratory_diagnosis": random_choice_generic("yes_no_confirmed_probable"),
            "was_there_a_physician_diagnosis_of_pneumonia": random_choice_generic("yes_no_na"),
            "suspected_non_infective": random_choice_generic("yes_no_na")
        },
        "medication_treatment": {
            "any_other_antiobiotic": random_choice_generic("yes_no_na"),
            "antifungal_agent": random_choice_generic("yes_no_na"),
            "corticosteroid": random_choice_generic("yes_no_na"),
            "other_covid_therapy": random_choice_generic("yes_no_na")
        },
        "lab_tests": {
            "white_blood_cell_count": random_choice_generic("yes_no"),
            "lymphocytes": random_choice_generic("yes_no"),
            "neutrophils": random_choice_generic("yes_no"),
            "tropinin_1": random_choice_generic("yes_no"),
            "tropinin_t": random_choice_generic("yes_no"),
            "d_dimer": random_choice_generic("yes_no"),
            "hemoglobin": random_choice_generic("yes_no"),
            "blood_urea_nitrogen": random_choice_generic("yes_no"),
            "haematocrit": random_choice_generic("yes_no"),
            "pt": random_choice_generic("yes_no"),
            "platelets": random_choice_generic("yes_no"),
            "aptt_aptr": random_choice_generic("yes_no"),
            "inr": random_choice_generic("yes_no"),
            "glucose": random_choice_generic("yes_no"),
            "lactate": random_choice_generic("yes_no"),
            "sodium": random_choice_generic("yes_no"),
            "potassium": random_choice_generic("yes_no"),
            "protocalcitonin": random_choice_generic("yes_no"),
            "crp": random_choice_generic("yes_no"),
            "cd4": random_choice_generic("yes_no"),
            "cd8": random_choice_generic("yes_no"),
            "cd4_cd8_ratio": random_choice_generic("yes_no")
        }
    }
    # add conditional properties
    # add type of organ transplant only if organ transplant answer is Yes
    if data["comorbidities"]["immune_system"]["organ_transplant"] == "Yes":
        data["comorbidities"]["immune_system"]["type_of_organ_transplant"] = random.choice(
            DATA_DICTIONARY["comorbidities"]["immune_system"]["type_of_organ_transplant"]
        )[1]
    # if malignancy is No, set all cancer diseases to No
    if data["comorbidities"]["cancer"]["malignancy"] == "No":
        for c in ["leukemia", "lymphoma", "sarcoma", "carcinoma", "myeloma", "mixed_types"]:
            data["comorbidities"]["cancer"][c] = "No"

    # add type of bacteria location only if bacteria answer is Yes confirmed
    if data["pathogen_testing"]["bacteria"] != "No":
        data["pathogen_testing"]["bacteria_location"] = random_choice_cv("pathogen_testing", "bacteria_location")

    return data


def generate_bundle(number_of_patients: int, filename: str):
    bundle = []
    for i in range(number_of_patients):
        data = generate_cancogen_data()
        bundle.append(data)
    with open(f"{filename}.json", "w") as output:
        json.dump(bundle, output)


def main(argv):

    opts, args = getopt.getopt(argv, "", ["number_of_patients=", "filename="])
    number_of_patients = 100
    filename = 'output'

    for opt, arg in opts:
        if opt == '--number_of_patients':
            number_of_patients = int(arg)
        elif opt == '--filename':
            filename = arg

    generate_bundle(number_of_patients, filename)


if __name__ == "__main__":
    main(argv[1:])
