# DATA DICTIONARY is derived from provided CRF

DATA_DICTIONARY = {
    "yes_no": [(0, "No"), (1, "Yes")],
    "yes_no_dontknow": [(0, "No"), (1, "Yes"), (-1, "Don't know")],
    "yes_no_na": [(0, "No"), (1, "Yes"), (-1, "NA")],
    "yes_no_confirmed_probable": [(0, "No"), (1, "Yes, confirmed"), (2, "Yes, probable")],
    "demographics": {
        "gender": [(0, "Male"), (1, "Female"), (2, "Not Specified")],
        "race_or_ethnicity": [
            (0, "White"),
            (1, "Black"),
            (2, "Hispanic"),
            (3, "East Asian/Pacific Islander"),
            (4, "South Asian"),
            (5, "Middle Eastern or Central Asian"),
            (6, "More than one race"),
            (-1, "Don't know")
        ],
        "education": [
            (0, "Elementary/primary school"),
            (1, "High school"),
            (2, "Vocational school/2 year college"),
            (3, "Bachelor's degree/4 year college"),
            (4, "Master's degree or higher"),
            (-1, "Don't know")
        ]
    },
    "vital_status": {
        "ambulatory": [
            (0, "Non-hospitalized, no limitation of activities"),
            (1, "Non-hospitilized, limitation of activities")
        ],
    },
    "risk_factors": {
        "history_of_smoking": [
            (0, "Haven't smoked 100 cigarettes"),
            (1, "Yes but not smoking now: quit _ years ago"),
            (2, "Yes and currently smoking"),
            (-1, "Don't know")
        ],
        "rate_of_smoking": [
            (0, "Don't smoke regularly"),
            (1, "Smoke about __ cigarettes daily"),
            (-1, "Do not know"),
            (-3, "Prefer not to answer")
        ],
        "vaping": [
            (0, "No"),
            (1, "Yes, if yes, __ cartridge per week over past 6 mo")
        ],
        "cannabis": [
            (0, "No"),
            (1, "Yes, if yes, __ joint/bong per week over past 6 mo")
        ]
    },
    "comorbidities": {
        "immune_system": {
            "type_of_organ_transplant": [
            (1, "Heart"),
            (2, "Kidney"),
            (3, "Liver"),
            (4, "Pancreas"),
            (5, "Intestine"),
            (6, "Lung"),
            (7, "Eye (Cornea)"),
            (8, "Blood/bone marrow"),
            (9, "Blood vessel"),
            (10, "Other")
        ]
        },
        "cancer": {
            "location": [
                (0, "Skin"),
                (1, "Lungs"),
                (2, "Breast"),
                (3, "Head and Neck"),
                (4, "Digestive/Gastrointenstinal"),
                (5, "Gynecologic"),
                (6, "Genitourinary"),
                (7, "Eye"),
                (8, "Musculoskeletal"),
                (9, "Germ cell/CNS"),
                (10, "Other"),
                (-1, "Don't know")
            ],
            "cancer_treatment_in_last_twelve_months": [
                (0, "Surgery"),
                (1, "Chemotherapy"),
                (2, "Radiation therapy"),
                (3, "HSCT"),
                (4, "Immunotherapy"),
                (5, "Hormone therapy"),
                (6, "Clinical Trials"),
                (7, "Other (specify)"),
                (-1, "Don't know")
            ]
        }
    },
    "symptoms_at_admission_longitudinal": {
        "dry_cough": [
            (0, "No"),
            (1, "Yes"),
            (2, "Yes, with sputum production"),
            (3, "Yes, bloody sputum/haemoptysis")
        ],
        "mucus_cough": [
            (0, "No"),
            (1, "Yes"),
            (2, "Yes, with sputum production"),
            (3, "Yes, bloody sputum/haemoptysis")
        ],
        "difficulty_or_pain_with_breathing": [
            (0, "No"),
            (1, "Yes, slight"),
            (2, "Yes, moderate"),
            (3, "Yes, severe"),
            (4, "Don't know")
        ],
        "loss_of_taste_or_smell": [
            (0, "No"),
            (1, "Only smell"),
            (2, "Only taste"),
            (3, "Both smell and taste"),
            (-1, "Don't know")
        ],
        "home_medications": [
            (1, "ACE inhibitor or Angiotensin receptor blocker"),
            (2, "Steroids"),
            (3, "Other immunosuppressive medication"),
            (4, "NSAIDs"),
            (5, "Other (specify)")
        ]
    },
    "hospitalization_information_encounter_complications": {
        "repeat_hospital_visit_within_30_days": [(0, "No"), (1, "Yes"), (2, "Unknown")]
    },
    "pathogen_testing": {
        "was_other_pathogen_testing_done_during_this_illness_episode": [
            (0, "No"),
            (1, "1 Yes, complete section")
        ],
        "influenza": [
            (0, "No"),
            (1, "Yes, confirmed. A/H3N2"),
            (2, "Yes, confirmed. A/H1N1pdm09"),
            (3, "Yes, confirmed. A/H5N1"),
            (4, "Yes, confirmed. A"),
            (5, "Yes, confirmed. not typed"),
            (6, "Yes, confirmed. B"),
            (7, "Yes, confirmed. Other"),
            (8, "Yes, probable. A/H3N2"),
            (9, "Yes, probable. A/H1N1pdm09"),
            (10, "Yes, probable. A/H5N1"),
            (11, "Yes, probable. A"),
            (12, "Yes, probable. not typed"),
            (13, "Yes, probable. B"),
            (14, "Yes, probable. Other")
        ],
        "coronavirus": [
            (0, "No"),
            (1, "Yes, confirmed. Novel CoV"),
            (2, "Yes, confirmed. MERS CoV"),
            (3, "Yes, confirmed. Other CoV"),
            (4, "Yes, probable. Novel CoV"),
            (5, "Yes, probable. MERS CoV"),
            (6, "Yes, probable. Other CoV")
        ],
        "bacteria": [
            (0, "No"),
            (1, "Yes, confirmed. Streptococcuus pneumoniae"),
            (2, "Yes, confirmed. Staph aureus"),
            (3, "Yes, confirmed. Group A streptococcus"),
            (4, "Yes, confirmed. E. coli"),
            (5, "Yes, confirmed. Klebsiella pneumoniae"),
            (6, "Yes, confirmed. Other")
        ],
        "bacteria_location": [
            (0, "Blood"),
            (1, "Lower respiratory tract"),
            (2, "Urine"),
            (3, "Bone or joint"),
            (4, "CNS"),
            (5, "Other")
        ]
    }
}
