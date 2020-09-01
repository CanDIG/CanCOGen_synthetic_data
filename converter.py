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
    symptoms = []
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
    if "comorbidities" in obj:
        if "immune_system" in obj["comorbidities"]:
            if "hiv" in obj["comorbidities"]["immune_system"]:
                if obj["comorbidities"]["immune_system"]["hiv"] == "Yes":
                    disease = {
                        "term": ONTOLOGIES["comorbidities"]["hiv"],
                        "extra_properties": {
                            "comorbidities_group": "immune_system"
                        }
                    }
                    diseases.append(disease)
            if "autoimmune_or_rheumatologic_disease" in obj["comorbidities"]["immune_system"]:
                if obj["comorbidities"]["immune_system"]["autoimmune_or_rheumatologic_disease"] == "Yes":
                    disease = {
                        "term": ONTOLOGIES["comorbidities"]["autoimmune_or_rheumatologic_disease"],
                        "extra_properties": {
                            "comorbidities_group": "immune_system"
                        }
                    }
                    diseases.append(disease)
            if "type_one_diabetes" in obj["comorbidities"]["immune_system"]:
                if obj["comorbidities"]["immune_system"]["type_one_diabetes"] == "Yes":
                    disease = {
                        "term": ONTOLOGIES["comorbidities"]["type_one_diabetes"],
                        "extra_properties": {
                            "comorbidities_group": "immune_system"
                        }
                    }
                    diseases.append(disease)
            if "type_two_diabetes" in obj["comorbidities"]["immune_system"]:
                if obj["comorbidities"]["immune_system"]["type_two_diabetes"] == "Yes":
                    disease = {
                        "term": ONTOLOGIES["comorbidities"]["type_two_diabetes"],
                        "extra_properties": {
                            "comorbidities_group": "immune_system"
                        }
                    }
                    diseases.append(disease)
        if "respiratory_system" in obj["comorbidities"]:
            if "asthma" in obj["comorbidities"]["respiratory_system"]:
                if obj["comorbidities"]["respiratory_system"]["asthma"] == "Yes":
                    disease = {
                        "term": ONTOLOGIES["comorbidities"]["asthma"],
                        "extra_properties": {
                            "comorbidities_group": "respiratory_system"
                        }
                    }
                    diseases.append(disease)
            if "copd" in obj["comorbidities"]["respiratory_system"]:
                if obj["comorbidities"]["respiratory_system"]["copd"] == "Yes":
                    disease = {
                        "term": ONTOLOGIES["comorbidities"]["copd"],
                        "extra_properties": {
                            "comorbidities_group": "respiratory_system"
                        }
                    }
                    diseases.append(disease)
            if "cystic_fibrosis" in obj["comorbidities"]["respiratory_system"]:
                if obj["comorbidities"]["respiratory_system"]["cystic_fibrosis"] == "Yes":
                    disease = {
                        "term": ONTOLOGIES["comorbidities"]["cystic_fibrosis"],
                        "extra_properties": {
                            "comorbidities_group": "respiratory_system"
                        }
                    }
                    diseases.append(disease)
            if "sleep_apnea" in obj["comorbidities"]["respiratory_system"]:
                if obj["comorbidities"]["respiratory_system"]["sleep_apnea"] == "Yes":
                    disease = {
                        "term": ONTOLOGIES["comorbidities"]["sleep_apnea"],
                        "extra_properties": {
                            "comorbidities_group": "respiratory_system"
                        }
                    }
                    diseases.append(disease)
        if "genitourinary_metabolic" in obj["comorbidities"]:
            if "renal_disease" in obj["comorbidities"]["genitourinary_metabolic"]:
                if obj["comorbidities"]["genitourinary_metabolic"]["renal_disease"] == "Yes":
                    disease = {
                        "term": ONTOLOGIES["comorbidities"]["renal_disease"],
                        "extra_properties": {
                            "comorbidities_group": "genitourinary_metabolic"
                        }
                    }
                    diseases.append(disease)
        # Mapping Hypertension and congestive heart failure to PhenotypicFeature
        if "cardiovascular_system" in obj["comorbidities"]:
            if "congestive_heart_failure" in obj["comorbidities"]["cardiovascular_system"]:
                if obj["comorbidities"]["cardiovascular_system"]["congestive_heart_failure"] == "Yes":
                    phenotypic_feature = {
                        "type": ONTOLOGIES["comorbidities"]["congestive_heart_failure"],
                        "extra_properties": {
                            "comorbidities_group": "cardiovascular_system"
                        }
                    }
                    phenotypic_features.append(phenotypic_feature)
            if "hypertension" in obj["comorbidities"]["cardiovascular_system"]:
                if obj["comorbidities"]["cardiovascular_system"]["hypertension"] == "Yes":
                    phenotypic_feature = {
                        "type": ONTOLOGIES["comorbidities"]["hypertension"],
                        "extra_properties": {
                            "comorbidities_group": "cardiovascular_system"
                        }
                    }
                    phenotypic_features.append(phenotypic_feature)
            if "myocardial_infarction_type_one" in obj["comorbidities"]["cardiovascular_system"]:
                if obj["comorbidities"]["cardiovascular_system"]["myocardial_infarction_type_one"] == "Yes":
                    phenotypic_feature = {
                        "type": ONTOLOGIES["comorbidities"]["myocardial_infarction_type_one"],
                        "extra_properties": {
                            "comorbidities_group": "cardiovascular_system"
                        }
                    }
                    phenotypic_features.append(phenotypic_feature)
            if "myocardial_infarction_type_two" in obj["comorbidities"]["cardiovascular_system"]:
                if obj["comorbidities"]["cardiovascular_system"]["myocardial_infarction_type_two"] == "Yes":
                    phenotypic_feature = {
                        "type": ONTOLOGIES["comorbidities"]["myocardial_infarction_type_two"],
                        "extra_properties": {
                            "comorbidities_group": "cardiovascular_system"
                        }
                    }
                    phenotypic_features.append(phenotypic_feature)
            if "peripheral_vascular_disease" in obj["comorbidities"]["cardiovascular_system"]:
                if obj["comorbidities"]["cardiovascular_system"]["peripheral_vascular_disease"] == "Yes":
                    phenotypic_feature = {
                        "type": ONTOLOGIES["comorbidities"]["peripheral_vascular_disease"],
                        "extra_properties": {
                            "comorbidities_group": "cardiovascular_system"
                        }
                    }
                    phenotypic_features.append(phenotypic_feature)
            # TODO make Stroke a disease ?
            if "stroke" in obj["comorbidities"]["cardiovascular_system"]:
                if obj["comorbidities"]["cardiovascular_system"]["stroke"] == "Yes":
                    disease = {
                        "term": ONTOLOGIES["comorbidities"]["stroke"],
                        "extra_properties": {
                            "comorbidities_group": "cardiovascular_system"
                        }
                    }
                    diseases.append(disease)
            if "arrythmias" in obj["comorbidities"]["cardiovascular_system"]:
                if obj["comorbidities"]["cardiovascular_system"]["arrythmias"] == "Yes":
                    phenotypic_feature = {
                        "type": ONTOLOGIES["comorbidities"]["arrythmias"],
                        "extra_properties": {
                            "comorbidities_group": "cardiovascular_system"
                        }
                    }
                    phenotypic_features.append(phenotypic_feature)
        if "neurological" in obj["comorbidities"]:
            if "dementia" in obj["comorbidities"]["neurological"]:
                if obj["comorbidities"]["neurological"]["dementia"] == "Yes":
                    disease = {
                        "term": ONTOLOGIES["comorbidities"]["dementia"],
                        "extra_properties": {
                            "comorbidities_group": "neurological"
                        }
                    }
                    diseases.append(disease)
        if "cancer" in obj["comorbidities"]:
            if "leukemia" in obj["comorbidities"]["cancer"]:
                if obj["comorbidities"]["cancer"]["leukemia"] == "Yes":
                    disease = {
                        "term": ONTOLOGIES["comorbidities"]["leukemia"],
                        "extra_properties": {
                            "comorbidities_group": "cancer"
                        }
                    }
                    diseases.append(disease)
            if "lymphoma" in obj["comorbidities"]["cancer"]:
                if obj["comorbidities"]["cancer"]["lymphoma"] == "Yes":
                    disease = {
                        "term": ONTOLOGIES["comorbidities"]["lymphoma"],
                        "extra_properties": {
                            "comorbidities_group": "cancer"
                        }
                    }
                    diseases.append(disease)
            if "sarcoma" in obj["comorbidities"]["cancer"]:
                if obj["comorbidities"]["cancer"]["sarcoma"] == "Yes":
                    disease = {
                        "term": ONTOLOGIES["comorbidities"]["sarcoma"],
                        "extra_properties": {
                            "comorbidities_group": "cancer"
                        }
                    }
                    diseases.append(disease)
            if "carcinoma" in obj["comorbidities"]["cancer"]:
                if obj["comorbidities"]["cancer"]["carcinoma"] == "Yes":
                    disease = {
                        "term": ONTOLOGIES["comorbidities"]["carcinoma"],
                        "extra_properties": {
                            "comorbidities_group": "cancer"
                        }
                    }
                    diseases.append(disease)
            if "myeloma" in obj["comorbidities"]["cancer"]:
                if obj["comorbidities"]["cancer"]["myeloma"] == "Yes":
                    disease = {
                        "term": ONTOLOGIES["comorbidities"]["myeloma"],
                        "extra_properties": {
                            "comorbidities_group": "cancer"
                        }
                    }
                    diseases.append(disease)
    # TODO
    if "symptoms_at_admission_longitudinal" in obj:
        if "dry_cough" in obj["symptoms_at_admission_longitudinal"]:
            symptom = {
                "type": ONTOLOGIES["symptoms"]["dry_cough"],
                "extra_properties": {
                    "datatype": "symptoms"
                }
            }
            if "Yes" in obj["symptoms_at_admission_longitudinal"]["dry_cough"]:
                symptom["negated"] = False
                symptom["description"] = obj["symptoms_at_admission_longitudinal"]["dry_cough"]
            else:
                symptom["negated"] = True
                symptom["description"] = "The phenotype was looked for, but found to be absent."
            phenotypic_features.append(symptom)
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
