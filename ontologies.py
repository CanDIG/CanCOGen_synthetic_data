# Mapping CRF data to Ontologies: SNOMED and HPO

ONTOLOGIES = {
    "comorbidities": {
        "hiv": {
            "label": "Human immunodeficiency virus",
            "id": "SNOMED:19030005"
        },
        "autoimmune_or_rheumatologic_disease": {
            "label": "Autoimmune disease",
            "id": "SNOMED:85828009"
        },
        "type_one_diabetes": {
            "label": "Type 1 diabetes mellitus",
            "id": "SNOMED:46635009"
        },
        "type_two_diabetes": {
            "label": "Type 2 diabetes mellitus",
            "id": "SNOMED:44054006"
        },
        "asthma": {
            "label": "Asthma",
            "id": "SNOMED:195967001"
        },
        "copd": {
            "label": "Chronic obstructive lung disease",
            "id": "SNOMED:13645005"
        },
        "cystic_fibrosis": {
            "label": "Cystic fibrosis",
            "id": "SNOMED:190905008"
        },
        "sleep_apnea": {
            "label": "Sleep apnea",
            "id": "SNOMED:73430006"
        },
        "renal_disease": {
            "label": "Kidney disease",
            "id": "SNOMED:90708001"
        },
        "congestive_heart_failure": {
            "label": "Congestive heart failure",
            "id": "HP:0001635"
        },
        "hypertension": {
            "label": "Hypertension",
            "id": "HP:0000822"
        },
        "myocardial_infarction_type_one": {
            "label": "Myocardial infarction",
            "id": "HP:0001658"
        },
        "myocardial_infarction_type_two": {
            "label": "Myocardial infarction",
            "id": "HP:0001658"
        },
        "peripheral_vascular_disease": {
            "label": "Peripheral arterial stenosis",
            "id": "HP:0004950"
        },
        "stroke": {
            "label": "Cerebrovascular accident",
            "id": "SNOMED:230690007"
        },
        "arrythmias": {
            "label": "Arrhythmia",
            "id": "HP:0011675"
        },
        "dementia": {
            "label": "Dementia",
            "id": "SNOMED:52448006"
        },
        "leukemia": {
            "label": "Leukemia",
            "id": "SNOMED:93143009"
        },
        "lymphoma": {
            "label": "Malignant lymphoma (clinical)",
            "id": "SNOMED:118600007"
        },
        "sarcoma": {
            "label": "Sarcoma",
            "id": "SNOMED:424413001"
        },
        "carcinoma": {
            "label": "Malignant epithelial neoplasm",
            "id": "SNOMED:722688002"
        },
        "myeloma": {
            "label": "Multiple myeloma",
            "id": "SNOMED:109989006"
        }
    },
    "symptoms": {
        "dry_cough": {
            "label": "Dry cough",
            "id": "HP:0031246"
        },
        "mucus_cough": {
            "label": "Wet cough",
            "id": "HP:0031245"
        },
        "difficulty_breathing": {
            "label": "Difficulty breathing",
            "id": "HP:0002098"
        },
        "fever": {
            "label": "Fever",
            "id": "HP:0001945"
        },
        "heart_rate": {
            "label": "Heart rate",
            "id": "SNOMED:364075005"
        },
        "highest_respiratory_rate": {
            "label": "Respiratory rate",
            "id": "SNOMED:86290005"
        },
        "wheezing": {
            "label": "Wheezing",
            "id": "HP:0030828"
        },
        "pulse": {
            "label": "Pulse",
            "id": "SNOMED:8499008"
        },
        "systolic_blood_pressure": {
            "label": "Systolic blood pressure",
            "id": "SNOMED:271649006"
        },
        "diastolic_blood_pressure": {
            "label": "Diastolic blood pressure",
            "id": "SNOMED:271650006"
        },
        "oxygen_saturation": {
            "label": "Finding of oxygen saturation",
            "id": "SNOMED:447755005"
        },
        "fatigue": {
            "label": "Fatigue",
            "id": "HP:0012378"
        },
        "chest_pain": {
            "label": "Chest pain",
            "id": "HP:0100749"
        },
        "ear_pain": {
            "label": "Ear pain",
            "id": "HP:0030766"
        },
        "joint_pain": {
            "label": "Joint pain/Joint inflammation",
            "id": "HP:0005059"
        },
        "abdominal_pain": {
            "label": "Abdominal pain",
            "id": "HP:0002027"
        },
        "runny_nose": {
            "label": "Runny nose",
            "id": "HP:0031417"
        },
        "nosebleed": {
            "label": "Nosebleed",
            "id": "HP:0000421"
        },
        "sore_throat": {
            "label": "Sore throat symptom",
            "id": "SNOMED:267102003"
        },
        "loss_of_taste_or_smell": {
            "loss_of_taste": {
                "label": "Loss of taste",
                "id": "SNOMED:36955009"
            },
            "loss_of_smell": {
                "label": "C/O - loss of smell sense",
                "id": "SNOMED:272028008"
            }
        },
        "diarrhea": {
            "label": "Diarrhea",
            "id": "HP:0002014"
        },
        "nausea": {
            "label": "Nausea",
            "id": "HP:0002018"
        },
        "headache": {
            "label": "Headache",
            "id": "HP:0002315"
        },
        "bodily_pain": {
            "label": "Bodily pain",
            "id": "NCIT:C114901"
        },
        "altered_consciousness_or_confusion": {
            "label": "Confusion",
            "id": "HP:0001289"
        },
        "skin_rash": {
            "label": "Skin rash",
            "id": "HP:0000988"
        },
        "myalgia": {
            "label": "Myalgia",
            "id": "HP:0003326"
        },
        "seizures": {
            "label": "Seizures",
            "id": "HP:0001250"
        },
        "conjunctivitis": {
            "label": "Conjunctivitis",
            "id": "HP:0000509"
        },
        "asymptomatic": {
            "label": "Asymptomatic",
            "id": "SNOMED:84387000"
        }
    },
    "complications": {
        "viral_pneumonitis": {
            "label": "Pneumonitis",
            "id": "SNOMED:205237003"
        },
        "bacterial_pneumonia": {
            "label": "Bacterial pneumonia",
            "id": "SNOMED:53084003"
        },
        "acute_respiratory_distress_syndrome": {
            "label": "Acute respiratory distress syndrome",
            "id": "SNOMED:67782005"
        },
        "pneumothorax": {
            "label": "Pneumothorax",
            "id": "HP:0002107"
        },
        "pleural_effusion": {
            "label": "Pleural effusion",
            "id": "HP:0002202"
        },
        "cryptogenic_organizing_pneumonia": {
            "label": "Cryptogenic organizing pneumonia",
            "id": "HP:0011945"
        },
        "bronchiolitis": {
            "label": "Bronchiolitis",
            "id": "HP:0011950"
        },
        "meningitis": {
            "label": "Meningitis",
            "id": "HP:0001287"
        },
        "encephalitis": {
            "label": "Encephalitis",
            "id": "HP:0002383"
        },
        "seizure": {
            "label": "Seizure",
            "id": "HP:0001250"
        },
        "stroke_cerebrovascular_accident": {
            "label": "Stroke",
            "id": "HP:0001297"
        },
        "congestive_heart_failure": {
            "label": "Congestive heart failure",
            "id": "HP:0001635"
        },
        "cardiac_inflammation": {
            "label": "cardiac inflammation",
            "id": "MP:0001853"
        },
        "cardiac_arrhythmia": {
            "label": "Cardiac arrhythmia",
            "id": "SNOMED:698247007"
        },
        "cardiac_ischaemia": {
            "label": "cardiac ischemia",
            "id": "MP:0004120"
        },
        "cardiac_arrest": {
            "label": "Cardiac arrest",
            "id": "HP:0001695"
        },
        "coagulation_disorder": {
            "label": "Coagulation disorder",
            "id": "SNOMED:64779008"
        },
        "disseminated_intravascular_coagination": {
            "label": "Disseminated intravascular coagulation",
            "id": "HP:0005521"
        },
        "anemia": {
            "label": "Anemia",
            "id": "HP:0001903"
        },
        "rhabdomyolysis": {
            "label": "Rhabdomyolysis",
            "id": "HP:0003201"
        },
        "myositis": {
            "label": "Myositis",
            "id": "HP:0100614"
        },
        "acute_renal_injury": {
            "label": "Acute Renal Failure",
            "id": "NCIT:C26808"
        },
        "gastrointestinal_haemorrhage": {
            "label": "Gastrointestinal hemorrhage",
            "id": "HP:0002239"
        },
        "pancreatitis": {
            "label": "Pancreatitis",
            "id": "HP:0001733"
        },
        "liver_dysfunction": {
            "label": "Liver dysfunction",
            "id": "HP:0001410"
        },
        "hyperglycemia": {
            "label": "Hyperglycemia",
            "id": "HP:0003074"
        },
        "hypoglycemia": {
            "label": "Hypoglycemia",
            "id": "HP:0001943"
        },
        "inflammatory_syndrome": {
            "label": "Systemic inflammatory response syndrome",
            "id": "SNOMED:238149007"
        }
    }

}
