from flask import Flask, render_template
from flask import request, jsonify
from joblib import dump, load
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression, Ridge
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, precision_score, recall_score


app = Flask(__name__)
loaded_model = load('RF_model.joblib')


@app.route('/', methods=['GET'])
def dropdown():
    payout_type = [' ', 'ACH', 'CHECK']
    return render_template('index.html', payout_type=payout_type)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/model', methods=['GET', 'POST'])
def model():
    inputs = request.args
    feature = []
    country_codes = ['country_', 'country_A1', 'country_AE',
                     'country_AR', 'country_AT', 'country_AU', 'country_BB', 'country_BE',
                     'country_BG', 'country_BS', 'country_CA', 'country_CH', 'country_CI',
                     'country_CM', 'country_CN', 'country_CO', 'country_CR', 'country_CZ',
                     'country_DE', 'country_DK', 'country_DZ', 'country_EC', 'country_ES',
                     'country_FI', 'country_FR', 'country_GB', 'country_GH', 'country_GR',
                     'country_HR', 'country_HU', 'country_ID', 'country_IE', 'country_IL',
                     'country_IM', 'country_IN', 'country_IS', 'country_IT', 'country_JE',
                     'country_JM', 'country_KE', 'country_KH', 'country_LB', 'country_MA',
                     'country_MX', 'country_MY', 'country_NA', 'country_NG', 'country_NI',
                     'country_NL', 'country_NZ', 'country_PH', 'country_PK', 'country_PR',
                     'country_PS', 'country_PT', 'country_QA', 'country_RO', 'country_RS',
                     'country_RU', 'country_SE', 'country_SG', 'country_SI', 'country_TH',
                     'country_TJ', 'country_TR', 'country_US', 'country_UY', 'country_VE',
                     'country_VI', 'country_VN', 'country_ZA']

    payout_codes = ['payout_type_', 'payout_type_ACH', 'payout_type_CHECK']

    for key, val in inputs.items():
        if key == 'input_2':
            dummy_country = [1 if val in code else 0 for code in country_codes]
        elif key == 'input_5':
            dummy_payout = [1 if val in code else 0 for code in payout_codes]
        else:
            feature.append(val)

    feature = feature + dummy_country + dummy_payout

    co_input = np.array(feature)
    # inp = co_input.reshape(1, -1)  # .astype(np.float64)
    try:
        results = loaded_model.predict([co_input])[0]
        if results == 0:
            res = 'Not a Fraud'
        else:
            res = 'Fraud'
        return jsonify(model_result=res)
    except:
        return jsonify(model_result='Error')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9999, debug=True)