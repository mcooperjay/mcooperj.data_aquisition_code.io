# CDC Mortality Data Analysis

## Overview
This repository contains all code and data used to explore mortality statistics in the United States, gathered directly from the **CDC's open data API** (`bi63-dtpu`).  
The dataset provides annual counts of deaths by cause, state, and year, along with the CDC’s **AADR (Age-Adjusted Death Rate)** metric.  

## Objective
The purpose of this project is to answer the question:  
**“Which causes of death contribute most to U.S. mortality, and how do age-adjusted death rates vary across states?”**

## Data Source
Data is pulled from the [CDC Wonder API](https://data.cdc.gov/resource/bi63-dtpu.json), which provides publicly available national mortality data.  
All data is public domain and used in accordance with CDC’s open data terms.

## Files
- **cdc_project.ipynb** – Main analysis and visualization notebook  
- **cdc_mortality_clean.csv** – Cleaned dataset (if small enough to include)  
- **plots/** – Folder containing PNG figures for key visualizations  
- **README.md** – Project description and repository guide  

## Methods
Data were retrieved via the CDC API using Python’s `requests` library, converted into a Pandas DataFrame, cleaned, and analyzed using `matplotlib` and `seaborn`.  
Key visualizations include:
- Top 10 causes of death in the U.S.  
- Top 20 states ranked by average AADR  

## Requirements
Run the following packages before executing the notebook:
```bash
pip install pandas matplotlib seaborn requests
