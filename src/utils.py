from pathlib import Path
from typing import Any, Dict

import pandas as pd

project_dir = Path(__file__).resolve().parents[1]

# Load the zip code database
zip_code_database = pd.read_csv(project_dir / "data" / "external" / "zip_code_database.csv")
latitude_and_longitude_lookup = {
    row.zip: (row.latitude, row.longitude) for row in zip_code_database.itertuples()
}

def preprocess(data: Dict[str, Any]) -> Dict[str, Any]:
    # Convert gender
    data["gender"] = "M" if data["gender"] == "Male" else "F"

    # Lookup latitude and longitude based on zip code
    zip_code = int(data.pop("zip_code"))
    if zip_code in latitude_and_longitude_lookup:
        data["latitude"], data["longitude"] = latitude_and_longitude_lookup[zip_code]
    else:
        # Handle missing zip code case
        data["latitude"], data["longitude"] = (None, None)

    # Convert numeric fields
    numeric_features = [
        "annual_income",
        "past_num_of_claims",
        "safty_rating",
        "age_of_driver",
        "claim_est_payout",
        "liab_prct",
        "age_of_vehicle",
        "vehicle_price",
        "vehicle_weight",
    ]
    for feature in numeric_features:
        data[feature] = int(data.get(feature, 0))

    # Convert categorical features
    binary_features = [
        "marital_status",
        "high_education_ind",
        "address_change_ind",
        "witness_present_ind",
        "policy_report_filed_ind",
    ]
    for feature in binary_features:
        data[feature] = 1 if data.get(feature) == "Yes" else 0

    return data



# from pathlib import Path
# from typing import Any, Dict

# import pandas as pd


# project_dir = Path(__file__).resolve().parents[1]


# zip_code_database = pd.read_csv(project_dir / "data" / "external" / "zip_code_database.csv")
# latitude_and_longitude_lookup = {
#     row.zip: (row.latitude, row.longitude) for row in zip_code_database.itertuples()
# }


# def preprocess(data: Dict[str, Any]) -> Dict[str, Any]:
#     data["gender"] = "M" if data["gender"] == "Male" else "F"

#     zip_code = int(data.pop("zip_code"))
#     data["latitude"], data["longitude"] = latitude_and_longitude_lookup[zip_code]

#     for feature in [
#         "annual_income",
#         "past_num_of_claims",
#         "safty_rating",
#         "age_of_driver",
#         "claim_est_payout",
#         "liab_prct",
#         "age_of_vehicle",
#         "vehicle_price",
#         "vehicle_weight",
#     ]:
#         data[feature] = int(data[feature])

#     for feature in [
#         "marital_status",
#         "high_education_ind",
#         "address_change_ind",
#         "witness_present_ind",
#         "policy_report_filed_ind",
#     ]:
#         data[feature] = 1 if data[feature] == "Yes" else 0
#     return data
