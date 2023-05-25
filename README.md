# Stroke Prediction Machine Learning Model

## Project Description

Stroke is a serious medical condition that occurs when the blood supply to part of the brain is interrupted or reduced, leading to brain damage and potential long-term disability or death. The risk of stroke is affected by a wide range of factors, including age, gender, hypertension, heart disease, obesity, and smoking.

Detecting a stroke in its early stages brings numerous advantages, including timely medical intervention, reduced brain damage, prevention of long-term disabilities, identification of underlying causes, and the facilitation of swift medical decision-making to optimize patient outcomes.

For this project, our objective is to create a machine learning model for early stroke detection, focusing on various causative factors. This model aims to assist clinical teams in predicting or assessing the risk of stroke occurrence, enabling timely medical intervention, minimizing brain damage, preventing long-term disabilities, identifying underlying causes, and facilitating quick medical decision-making to optimize patient outcomes.

## Data Overview
The stroke dataset comprises a compilation of patients' medical records. It encompasses a wide range of information, including patient demographics, medical history, lifestyle factors, and the presence or absence of a stroke for each patient.

 Here is a snippet of the dataset:
 
 <img width="829" alt="image" src="https://github.com/MeerKar/Project-4-Stroke-Predict/assets/116701851/fd542bcf-570c-4474-b891-0a427bdb263a">


## Built With

. Python and Packages (eg. scikit-learn, matplotlib, searborn, pickle, etc.)
. Flask
. HTML
. CSS

# Getting Started

## Prerequisites

Make sure you have installed all of the following prerequisites on your development machine:

. Git
. Python and set up your virtual environment
. pip install flask globally
. Your favoriate code editor (e.g. VScode, etc.)
. Your favoriate browser (e.g. Google Chrome, etc.)

## Installation

1. Clone this repo and save it in your local directory, to clone with URL run the following code in terminal

 git clone (https://github.com/MeerKar/Project-4-Stroke-Predict)

2. Start Flask app by running the following code in terminal

3.  python app.py

Visit localhost: 5000 in your browser and enjoy!

# Machine Learning Pipline

## 1. Data Collection
   Data was collected from Kaggle

## 2. Model Selection

The Random Forest Classifier was selected for this problem due to its reputation for achieving high accuracy in classification tasks. It is a popular choice in the healthcare and medical industry, where precise and reliable predictions are crucial.

# Exploratory Data Analysis (EDA)

The below snippets are some interesting observations we discovered:

1. Data Distribution with Histogram Analysis

<img width="759" alt="image" src="https://github.com/MeerKar/Project-4-Stroke-Predict/assets/116701851/0f1c9678-fb9b-46ec-b69a-42b04a5afc0e">

2. Closer Examination on Target Variable

<img width="700" alt="image" src="https://github.com/MeerKar/Project-4-Stroke-Predict/assets/116701851/0bcac8c9-00ef-443a-8dcf-f9f8730ae62d">

3. Missing Values on 'bmi' column

<img width="618" alt="image" src="https://github.com/MeerKar/Project-4-Stroke-Predict/assets/116701851/ff8e7397-5d20-4d0e-a298-2751913e0c0d">

4. Filled in Missing Values with Imputed values

<img width="960" alt="image" src="https://github.com/MeerKar/Project-4-Stroke-Predict/assets/116701851/7eb64342-4729-490e-a076-e0e78ff90ea2">

5. Singleton Record on 'gender' column

<img width="718" alt="image" src="https://github.com/MeerKar/Project-4-Stroke-Predict/assets/116701851/21796d20-3e9b-4efd-a3fb-2f346382459b">

6. Dropped Singleton Record

<img width="788" alt="image" src="https://github.com/MeerKar/Project-4-Stroke-Predict/assets/116701851/65337cc7-aa67-40ad-898c-880cb0055084">

7. Uneven Distribution 'bmi' values

<img width="588" alt="image" src="https://github.com/MeerKar/Project-4-Stroke-Predict/assets/116701851/b7615e3a-8f34-4740-b461-4609550c79bd">

8. Binning 'bmi' values (Model 3 only) image

<img width="771" alt="image" src="https://github.com/MeerKar/Project-4-Stroke-Predict/assets/116701851/1e1b19b6-d891-4209-bf16-9612be1923d7">

# Data Preprocessing

##  Data was cleaned and prepared for further analysis. This includes:

1. Applied oversampling methods to handle imbalanced data

2. Apllied encoding to categorical varibales

3. Applied feature scaling to transform numerical features into a consistent range

4. Divided data into training and testing sets using train_test_split module

## Modeling Training and Testing

1. Trained 3 models using different resampling methods
2. Tested the models
3. 
# Evaluation

Utilized accuracy scores, confusion matrix and classification reports to compare to access the performance of all 3 models
See more detail about our final model

# Model Deployment with Flask

1. Implemented the model logic in our home route to handle incoming requests
 
2. Created Web-based UI with HTML and CSS

Check out the snippets below:

## Form Page Example:

<img width="1358" alt="image" src="https://github.com/MeerKar/StrokePrediction/assets/116701851/8f846ee6-eeeb-43c2-b4f0-511b6aac19e0">

## Result Page Example:

<img width="1428" alt="image" src="https://github.com/MeerKar/StrokePrediction/assets/116701851/7b93d045-3baa-414a-9fbd-2e0cba0a0f1b">

### Credits

 Kevin Lee

 Kaggle

 UC Berkely Extension Data Analytics Bootcamp


