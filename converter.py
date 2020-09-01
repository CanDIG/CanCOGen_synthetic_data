from datetime import datetime
import json
import os
import getopt
from sys import argv

from ontologies import ONTOLOGIES, RESOURCES

DIR_FILES = os.path.dirname(os.path.realpath(__file__))

SEX_TO_SEX_MAPPING = {
    "Male": "MALE",
    "Female": "FEMALE",
    "Not Specified": "UNKNOWN_SEX"
}


def symptom_to_pf(obj, symptom, contains_value=False):
    if symptom in obj:
        pf = {
            "type": ONTOLOGIES["symptoms"][symptom],
            "extra_properties": {
                "datatype": "symptom"
            }
        }
        if "Yes" in obj[symptom]:
            pf["negated"] = False
            pf["description"] = f"{obj[symptom]} - Original value extracted from the source CRF."
        elif contains_value:
            pf["negated"] = False
            pf["description"] = f"{obj[symptom]} - Original value extracted from the source CRF."
        else:
            pf["negated"] = True
            pf["description"] = f"{obj[symptom]} - Original value extracted from the source CRF." \
                                f"The phenotype was looked for, but found to be absent."
        return pf


def comorbidity_to_disease(obj, comorbidity, comorbidities_group):
    if comorbidity in obj:
        if obj[comorbidity] == "Yes":
            disease = {
                "term": ONTOLOGIES["comorbidities"][comorbidities_group][comorbidity],
                "extra_properties": {
                    "comorbidities_group": comorbidities_group.replace('_', ' '),
                    "datatype": "comorbidity"
                }
            }
            return disease
        else:
            return None


def convert_to_phenopacket(obj):
    """ Takes single CanCoGen json crf object and converts it to a phenopacket. """

    phenopacket = {
        "id": obj["identification"]["case_id"],
        "meta_data": {
            "created": str(datetime.now()),
            "phenopacket_schema_version": "1.0.0-RC3",
            "created_by": "Ksenia Zaytseva",
            "submitted_by": "Ksenia Zaytseva",
            "resources": [
                RESOURCES["NCBITaxon"],
                RESOURCES["SNOMED"],
                RESOURCES["HP"],
                RESOURCES["MP"],
                RESOURCES["NCIT"],
            ]
        }
    }
    subject = {
        "id": obj["identification"]["case_id"],
        "taxonomy": {
            "label": "Homo sapiens",
            "id": "NCBITaxon:9606"
        }
    }
    diseases = []
    phenotypic_features = []
    # Demographics
    if "demographics" in obj:
        subject["date_of_birth"] = obj["demographics"].get("age", None)
        sex = obj["demographics"].get("sex", None)
        if sex:
            subject["sex"] = SEX_TO_SEX_MAPPING[sex]
        subject["ethnicity"] = obj["demographics"].get("ancestry", None)
        subject["extra_properties"] = {
            "height": obj["demographics"].get("height", None),
            "weight": obj["demographics"].get("weight", None),
            "education": obj["demographics"].get("education", None)
        }
    # Comorbidities
    if "comorbidities" in obj:
        for system in ["immune_system", "respiratory_system", "genitourinary_metabolic", "cardiovascular_system",
                       "neurological", "cancer"]:
            if system in obj["comorbidities"]:
                for comorbidity in ONTOLOGIES["comorbidities"][system].keys():
                    disease = comorbidity_to_disease(obj["comorbidities"][system], comorbidity, system)
                    if disease:
                        diseases.append(disease)
    # Symptoms
    if "symptoms_at_admission_longitudinal" in obj:
        # yes no na symptoms
        for pf in ["dry_cough", "mucus_cough", "difficulty_breathing", "fatigue", "myalgia",
                   "runny_nose", "sore_throat", "nosebleed", "ear_pain", "wheezing",
                   "chest_pain", "joint_pain", "headache", "seizures",
                   "altered_consciousness_or_confusion", "abdominal_pain",
                   "diarrhea", "nausea", "conjunctivitis", "skin_rash",
                   "asymptomatic", "bodily_pain"]:
            new_pf = symptom_to_pf(obj["symptoms_at_admission_longitudinal"], pf)
            phenotypic_features.append(new_pf)
        # symptoms with values
        # TODO oxygen_saturation_on - not in ontologies
        for value_pf in ["fever", "heart_rate", "highest_respiratory_rate",
                         "systolic_blood_pressure", "diastolic_blood_pressure",
                         "oxygen_saturation"]:
            new_value_pf = symptom_to_pf(obj["symptoms_at_admission_longitudinal"], value_pf, True)
            phenotypic_features.append(new_value_pf)

        # TODO loss_of_taste_or_smell

    phenopacket["subject"] = subject
    phenopacket["diseases"] = diseases
    phenopacket["phenotypic_features"] = phenotypic_features
    return phenopacket


def convert_bundle(input_filename, output_filename):
    input = os.path.join(DIR_FILES, input_filename)
    phenopackets = []
    with open(input, "r") as input_file:
        cancogen_data = json.load(input_file)
        if isinstance(cancogen_data, list):
            for item in cancogen_data:
                phenopacket = convert_to_phenopacket(item)
                phenopackets.append(phenopacket)
        else:
            return "The CanCoGen data is malformed."
    with open(f"{output_filename}.json", "w") as output_file:
        json.dump(phenopackets, output_file)
        return


def main(argv):
    opts, args = getopt.getopt(argv, "", ["input_file=", "output_filename="])
    input_file = ''
    output_filename = 'phenopackets_output'

    for opt, arg in opts:
        if opt == '--input_file':
            input_file = arg
        elif opt == '--output_filename':
            output_filename = arg

    if input_file == '':
        help()
        exit()

    convert_bundle(input_file, output_filename)


def help():
    print("Usage: python converter.py --input_file=file.json [--output_filename=output]")
    return


if __name__ == "__main__":
    main(argv[1:])
