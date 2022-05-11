# Sparkify Churn Prediction Project

## 1. Project Overview

The motivation behind this project is to predict churn for the fictional music streaming platform Sparkify. This article provides a deep dive into a churn prediction task from both a business and a technical perspective. Using PySpark - a Python library for large data processing - and Google Cloud Dataproc - a fully managed and highly scalable service for running Apache Spark applications on the cloud- we are going to predict churn based on user logs of the fictional music streaming service Sparkify.


A blog post about this project incl. technical configuration is available on [Medium](https://medium.com/@frederik-schmidt/churn-prediction-with-pyspark-and-google-cloud-dataproc-ba9bca6981d4).

### Problem Statement

From a business perspective, churn - which refers to customers that stop buying a company's product or using a company's service - can have a major negative impact on revenue. Companies are interested in using data to understand which customers are likely to churn and prevent them from churning. This is why churn prediction has become a common task for data scientists and analysts in any customer-facing business.

### Data

The underlying data basis was provided by [Udacity](https://www.udacity.com/) and originally covers 26,259,199 events from 22,278 Sparkify users, such as playing the next song, adding a song to a playlist, or upgrading or downgrading the service. In addition, there is a tiny subset (128MB) of the full Sparkify data with 286,500 events from 225 Sparkify users and a medium-sized subset (462MB) with 1,087,410 events from 448 Sparkify users.


Please note that we will not work with the original Sparkify dataset (12GB) in this project but a medium-sized subset (462MB). This is because I wanted to implement the Sparkify pipeline on Google Cloud Platform (GCP). The original dataset is stored on Amazon's S3 located in `s3n://udacity-dsnd/sparkify/sparkify_event_data.json` though and the way it is configured does not allow to easily transfer it to GCP. If so, the pipeline could easily be scaled up and re-executed with the original dataset.

### Metrics

Churn prediction is a classification task. In this case, there are multiple possible metrics:
- Accuracy (= valid choice of evaluation for classification problems which are well-balanced and not skewed)
- Precision (= valid choice of evaluation metric when we want to be very sure of our prediction)
- Recall (= valid choice of evaluation metric when we want to capture as many positives as possible)
- F1 Score (= valid choice of evaluation metric when we want to have a model with both good precision and recall)


In this project, we will optimize for F1 Score since the churned users are a fairly small subset.

## 2. Project Steps

The project contains three steps:

### 2.1 Load Sparkify Data

The code for loading the Sparkify data is present in `load_data.ipynb`. First, it loads the medium-sized Sparkify dataset from video.udacity-data.com into the local directory using the `curl` command below. Second, it loads the medium-sized dataset (462MB) and the mini dataset (128MB) which should be added manually to `/data` into a Cloud Storage bucket. 

### 2.1 Exploratory Data Analysis

The code for the EDA is present in `run_exploratory_data_analysis.ipynb`. The necessary preprocessing steps identified in the EDA is stored in `preprocessing_sparkify.py` so it can be reused in the Spark Machine Learning Pipeline.

### 2.2 Machine Learning Pipeline

The code for the production Machine Learning Pipeline is present in `run_pipe_sparkify.ipynb`. Using the medium-sized dataset, the code takes about 3 hours to execute.

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

### 3.5 Add `mini_sparkify_event_data.json`

The mini Sparkify dataset (128MB) can be downloaded from the Internet. It should be present in the `/data` directory, because it gets loaded into a Cloud Storage bucket in `load_data.ipynb`.


When the packages have been installed, everything is set up and ready to run the project steps described in section 2.

## 4. File Structure

```
.
├── data
├── data_transfer.py
├── LICENSE
├── load_data.ipynb
├── preprocessing_sparkify.py
├── README.md
├── requirements.txt
├── run_exploratory_data_analysis.ipynb
└── run_pipe_sparkify.ipynb
```

## 5. Requirements

The project uses Python 3.8 and additional libraries:
- google
- datetime
- numpy
- os
- pyspark
- time

## 6. Links

- [Udacity Data Scientist Nanodegree](https://www.udacity.com/course/data-scientist-nanodegree--nd025)
- [The 5 Classification Evaluation metrics every Data Scientist must know](https://towardsdatascience.com/the-5-classification-evaluation-metrics-you-must-know-aa97784ff226)