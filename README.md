# Stroke Classifier

## Project Description

Stroke is a serious medical condition that occurs when the blood supply to part of the brain is interrupted or reduced, leading to brain damage and potential long-term disability or death. The risk of stroke is affected by a wide range of factors, including age, gender, hypertension, heart disease, obesity, and smoking.Stroke is an emergency condition that needs to be treated as soon as possible, because brain cells can die in just a matter of minutes. Prompt and appropriate treatment measures can minimize the level of brain damage and prevent possible complications.

In this machine learning project, the overall topic that will be resolved is in the health sector regarding stroke, where it will try to predict the possibility of a stroke in a person with certain conditions based on several factors including: age, certain diseases (hypertension, heart disease) who are at high risk of developing stroke. strokes, cigarettes, etc.

As previously explained, stroke can kill the sufferer in a matter of minutes. Detecting stroke with the existing causative factors with the help of machine learning can be very useful in the world of health to detect stroke early in order to increase the sense of heart among sufferers so that strokes can be prevented early.



## Objective 

The project objective is to  develop a machine learning model for early stroke prediction.


##  Dataset 

The stroke dataset is a collection of medical records for patients. The dataset includes information on patient demographics, medical history, and lifestyle factors, as well as whether or not each patient had a stroke.

https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset?select=healthcare-dataset-stroke-data.csv 

The goal of this dataset is to develop a predictive model that can accurately identify patients who are at high risk of stroke, so that appropriate preventative measures can be taken to reduce their risk.

<img width="846" alt="image" src="https://github.com/yeyanwang/stroke_classifier/assets/116701851/65f71358-7d88-4b14-bb81-04aba45e9336">




## Solution 

Making Machine Learning models with the Random Forest Algorithm that can classify someone who has the potential to have a stroke.

# Exploratory Data Analysis (EDA) 

### Examine & Impute Missing Values

 <img width="783" alt="image" src="https://github.com/yeyanwang/stroke_classifier/assets/116701851/45df1501-6554-42c1-a717-b3f7a679c4ee">

### Examine Data Distribution on Feature Variables 

<img width="659" alt="image" src="https://github.com/yeyanwang/stroke_classifier/assets/116701851/23b59170-d4cb-4be7-a8ca-572a2b48ce13">

### Examine Data Distribution on Target Variable

<img width="792" alt="image" src="https://github.com/yeyanwang/stroke_classifier/assets/116701851/33abaa73-a197-48a0-ab27-410523997c5c">

### Examine & Handle Singleton Record

<img width="762" alt="image" src="https://github.com/yeyanwang/stroke_classifier/assets/116701851/21795c44-4329-4391-a511-01c4f0fb45c1">


# Data Preprocessing

Data Preprocessing is divided into four different parts.

1. Handle Imbalanced data 
 
2. Feature Scaling
 
3. Encode Categorical Variables
 
4. Train test split.





