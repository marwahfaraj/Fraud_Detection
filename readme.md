# Fraud Detection

### Overview

This repository implements a fraud detection model using Flask and machine learning techniques. It allows users to input information about a transaction and receive a prediction of whether it's likely fraudulent.

### Key Features

- Leverages a trained Random Forest model for accurate fraud detection.
- Provides a user-friendly Flask interface for easy prediction.
- Handles both GET and POST requests for flexibility.
- Offers clear model results through JSON responses.

### Project Structure

```
fraud_detection/app/
├── app.py              # Flask application main script
├── RF_model.joblib        # Serialized Random Forest model
├── requirements.txt     # Dependency list for project execution
├── setup.sh            # Optional script for initial setup (if needed)
├── run.sh              # Optional script to start the Flask app (if needed)
├── static/             # Contains static assets like CSS or JavaScript
└── template/           # Holds Jinja2 templates for HTML rendering
    ├── index.html      # Main web page template
```

### Dependencies

```
- Flask
- scikit-learn
- joblib
- pandas
- numpy
```

### Installation

1. Ensure you have Python and pip installed.
2. Create a virtual environment (recommended): `python3 -m venv venv`
3. Activate the virtual environment: `. venv/bin/activate` (Windows: `venv\Scripts\activate`)
4. Install required dependencies: `pip3 install -r requirements.txt`

### Running the App

1. Open a terminal in the project directory.
2. Execute: `sh run.sh` (or replace with your preferred startup method).
3. Access the app in your browser: http://localhost:9999/

### Using the App

1. Visit the web page in your browser.
2. Select the payout type from the dropdown or enter relevant information in the input fields.
3. Click "Submit" or press Enter.
4. The app will display a prediction: "Not a Fraud" or "Fraud".

### Model Details

- The model is a Random Forest classifier trained on labeled transaction data.
- It uses various features like country codes and payout types for prediction.
- The model's performance metrics (accuracy, precision, recall) can be found in the app.py file or within the training process of your model.

### Tools

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Anaconda](https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white) ![Render](https://img.shields.io/badge/Render-%46E3B7.svg?style=for-the-badge&logo=render&logoColor=white) 
