# Sparkify Churn Prediction Project

## 1. Project Overview

The motivation behind this project is to predict churn for the fictional music streaming platform Sparkify. From a
technical perspective, the project focuses on the ability to efficiently manipulate large datasets with Spark.

### Problem Statement

Predicting churn rates is a challenging and common problem that data scientists and analysts regularly encounter in any
customer-facing business. From a business perspective, churn can have a major negative impact on a company's revenue. 

### Data

The data used in this project was provided by [Udacity](https://www.udacity.com/). More detailed:
- The dataset contains log data of user events tracked by Udacity. It serves as a starting point for driving insights
  and create a machine learning pipeline to predict churn.
- There is a tiny dataset (128MB) for testing and a full dataset (12GB) for deployment.
- Both datasets contain records of Sparkify events such as playing the next song, adding a song to a
  playlist, or upgrading or downgrading the service.
- The tiny dataset contains 286,500 records and is present in the Udacity workspace.
- The full dataset contains 26,259,199 records and is present at `s3n://udacity-dsnd/sparkify/sparkify_event_data.json`.

### Metrics

Churn prediction is a classification task. In this case, there are multiple possible metrics:
- Accuracy (= valid choice of evaluation for classification problems which are well-balanced and not skewed)
- Precision (= valid choice of evaluation metric when we want to be very sure of our prediction)
- Recall (= valid choice of evaluation metric when we want to capture as many positives as possible)
- F1 Score (= valid choice of evaluation metric when we want to have a model with both good precision and recall)

In this project, we will optimize for F1 Score since the churned users are a fairly small subset.

## 2. Project Steps

The project contains two steps:

### 2.1 Exploratory Data Analysis

The code for the EDA is present in `exploratory_data_analysis.ipynb`. The necessary preprocessing  steps identified in
the EDA is stored in `preprocessing_sparkify.py` so it can be reused in the Spark Machine Learning pipeline.

### 2.2 Spark Machine Learning Pipeline

The code for the production Machine Learning pipeline is present in `sparkify.ipynb`. As this code uses the full
Sparkify dataset (12GB), this code must be executed from an AWS EMR instance.

In addition, there is the notebook `sparkify_dev.ipynb` which can be run locally. This was used for building and
optimizing the pipeline based on the tiny dataset (128MB).

## 3. Installation Guide

### 3.1 Clone the repository

`> git clone https://github.com/frederik-schmidt/Sparkify-churn.git`

### 3.2 Create a virtual environment

It is highly recommended to use virtual environments to install packages.

`> conda create -n sparkify_churn python=3.8 jupyterlab`
(where `sparkify_churn` is the environment name of your choice)

### 3.3 Activate the virtual environment

`> conda activate sparkify_churn`
(or whatever environment name you used)

### 3.4 Install the required packages

```
> cd Sparkify-churn
> pip install -r requirements.txt
```

When the packages have been installed, everything is set up and ready to run the project steps described in section 2.

## 4. File Structure

```
.
├── data
│   └── mini_sparkify_event_data.json
├── exploratory_data_analysis.ipynb
├── preprocessing_sparkify.py
├── README.md
├── requirements.txt
├── sparkify.ipynb
└── sparkify_dev.ipynb
```

## 5. Requirements

The project uses Python 3.8 and additional libraries:
- datetime
- numpy
- plotly
- pyspark
- time

## 6. Links

- [Udacity Data Scientist Nanodegree](https://www.udacity.com/course/data-scientist-nanodegree--nd025)
- [The 5 Classification Evaluation metrics every Data Scientist must know](https://towardsdatascience.com/the-5-classification-evaluation-metrics-you-must-know-aa97784ff226)