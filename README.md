# Placement Prediction using Machine Learning

This project focuses on predicting student placement and salary in campus recruitment using Random Forest classifiers. The goal is to help students and educational institutions understand the factors that influence placement success and expected salary.

## Final Result
<img src="static/images/pl1.png" alt="Alt text" width=100%>
<img src="static/images/pl2.png" alt="Alt text" width=100%>
<img src="static/images/pl3.png" alt="Alt text" width=100%>

## Table of Contents
- [Overview](#overview)
- [Dataset](#dataset)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Data Preprocessing](#data-preprocessing)
- [Model Training](#model-training)
- [Evaluation](#evaluation)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Overview

Campus placement is a crucial event for students and educational institutions. Predicting placement outcomes and potential salaries can help students prepare better and institutions improve their placement strategies. This project uses Random Forest classifiers to predict both placement probability and expected salary based on various student features.

## Dataset

The dataset used in this project includes student information such as:
- Academic performance (CGPA)
- Skills
- Weather the Candidate has done Intership
- Weather the Candidate has Participated in hackathons
- Other relevant features

The dataset contains features for predicting both placement status and salary.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   git clone https://github.com/charans2702/Placement_Prediction_Using_Machine-Learning.git
   cd placement-prediction
2. Install the required packages:
   pip install -r requirements.txt

## Project Structure

- `data/`: Contains the dataset files
- `notebooks/`: Jupyter notebooks for data exploration and model development
- `Exploratory_Data_Analysis.ipynb`: Initial data exploration
- `Placement_Prediction_Model.ipynb`: Model for predicting placement
- `Salary_Prediction_Model.ipynb`: Model for predicting salary
- `src/`: Source code for the project
- `data_preprocessing.py`: Script for data cleaning and preprocessing
- `model_training.py`: Script for training the models
- `evaluation.py`: Script for model evaluation
- `models/`: Saved model files
- `results/`: Evaluation results and visualizations
- `app.py`: Flask application for model deployment
- `requirements.txt`: List of required Python packages
- `README.md`: Project documentation

## Data Preprocessing

The data preprocessing steps include:
1. Handling missing values
2. Encoding categorical variables
3. Feature scaling
4. Feature selection

## Model Training

Two Random Forest classifiers are trained:
1. Placement Prediction Model: Predicts whether a student will be placed
2. Salary Prediction Model: Predicts the salary for placed students

The training process involves:
1. Splitting the data into training and testing sets
2. Initializing the Random Forest classifiers
3. Training the models on the training set
4. Fine-tuning hyperparameters using techniques like Grid Search or Random Search

## Evaluation

The models' performance is evaluated using various metrics, including:
- Accuracy
- Precision
- Recall
- F1 Score
- Mean Absolute Error (for salary prediction)
- R-squared score (for salary prediction)

## Results

### Placement Prediction Model
- Accuracy: X%
- Precision: X
- Recall: X
- F1 Score: X

### Salary Prediction Model
- Mean Absolute Error: $X
- R-squared Score: X

[Include visualizations like confusion matrices, feature importance plots, etc.]

## Flask App

The trained models are deployed using a Flask web application. The app allows users to input student details and receive predictions for placement probability and expected salary.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue.

## License

[Include your chosen license here]
