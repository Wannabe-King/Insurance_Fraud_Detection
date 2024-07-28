import pickle
from pathlib import Path

import pandas as pd
import streamlit as st

import utils


project_dir = Path(__file__).resolve().parents[1]

with open(project_dir / "models" / "best_model.pickle", "rb") as f:
    model = pickle.load(f)


def main():
    st.title("Prediction App")
    
    st.write("Please enter the input data:")

    # Collect input data from the user
    form_data = {
        "field1": st.text_input("Field 1"),
        "field2": st.text_input("Field 2"),
        # Add more fields as needed
    }
    
    if st.button("Predict"):
        preprocessed_data = utils.preprocess(form_data)
        probability = model.predict_proba(pd.DataFrame(preprocessed_data, index=[0]))
        st.write(f"Predicted Probability: {probability[0, 1] * 100:.2f}%")

if __name__ == "__main__":
    main()



# import pickle
# from pathlib import Path

# import pandas as pd
# from flask import Flask, render_template, request

# import utils


# project_dir = Path(__file__).resolve().parents[1]
# app = Flask(__name__)


# with open(project_dir / "models" / "best_model.pickle", "rb") as f:
#     model = pickle.load(f)


# @app.route("/")
# def home():
#     return render_template("index.html")


# @app.route("/predict", methods=["POST"])
# def predict():
#     form_data = request.form.to_dict()
#     preprocessed_data = utils.preprocess(form_data)
#     probability = model.predict_proba(pd.DataFrame(preprocessed_data, index=[0]))
#     return render_template("result.html", probability=f"{probability[0, 1] * 100:.2f}")


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8080)


