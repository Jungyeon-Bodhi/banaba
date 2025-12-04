#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Bodhi Global Analysis (Jungyeon Lee)
"""

"""
Please define the parameters for data preprocessing pipeline
"""
import bodhi_data_preprocessing as dp

project_name = "Building Community Resilience and Delivery of Essential Services for Post-Conflict Recovery in BARMM/Lanao del Sur/Marawi (2022 - 2025)"

file_type = 'xlsx' 
# Original data format: xlsx, xls, csv

file_path = "Data/25-UNICEF-PH-1 - Raw Dataset"
# Original data location and name (excluding file extension): "Data/(name)"

file_path_others = "Data/25-UNICEF-PH-1 - Open-End.xlsx"
# Specify the path and name of the Excel sheet where the values from the open-ended columns will be saved (New file)
# For example: "Data/(project name) others.xlsx"

email = 'Email'
phone = 'Phone'
# Original column name for respondents' names (for anonymisation and duplicate removal)

identifiers = [email, phone, '0', '1', '2', '3', '4', 'Module','7','8']
# Identifiers for detecting duplicates (list, do not remove respondent_name)
# Recommendation: At least three identifiers

dates = [] 
# Remove the dates on which the pilot test was conducted from the data
# for example ['2024-07-18', '2024-07-22', '2024-07-23']

cols_new = ['Timestamp', 'Consent', '0', 'Email', 'Phone', '1', '2', '3', '3-1', '4', '5',
 '6a','6b', '6c', '6d', '6e', '6f',
 '7','8', 'A_9-1', 'A_10-1', 'A_11-1', 'A_12-1', 'A_13-1', 'A_9-2', 'A_10-2', 'A_11-2', 'A_12-2', 
 'A_13-2', 'A_9-3', 'A_10-3', 'A_11-3', 'A_12-3', 'A_13-3', 'A_14', 'A_15', 'A_16-1', 'A_16-2',
 'Comment', '5a', '5b', '5c', '5d', '5e', '5_Other',
 'A_14a', 'A_14b', 'A_14c', 'A_14d', 'A_14e', 'A_14f', 'A_14g', 'A_14h', 'A_14i',
 'Module',
 'B_9-1', 'B_10-1', 'B_12-1', 'B_15-1', 'B_9-2', 'B_10-2', 'B_12-2', 'B_15-2',
 'B_9-3', 'B_11-3', 'B_12-3', 'B_15-3', 'B_9-4', 'B_11-4', 'B_12-4', 'B_15-4',
 'B_9-5','B_13', 'B_14', 'B_15-5', 'B_16', 'B_17', 'B_18-1', 'B_18-2', 'B_19', 'B_20-1', 'B_20-2',
 '5f', '5g',
 'B_18_1a', 'B_18_1b', 'B_18_1c', 'B_18_1d', 'B_18_1e', 'B_18_1_Other',
 'C_9-1', 'C_10-1', 'C_12-1', 'C_13-1', 'C_9-2', 'C_10-2', 'C_12-2', 'C_13-2',
 'C_14', 'C_15', 'C_16', 'C_17-1', 'C_17-2', 'C_15a', 'C_15b', 'C_15c', 'C_15d', 'C_15e', 'C_15_Other',
 'D_9-1', 'D_10-1', 'D_11-1', 'D_12-1', 'D_9-2', 'D_10-2', 'D_11-2', 'D_12-2',
 'D_13a', 'D_13b', 'D_13c', 'D_13d', 'D_13e', 'D_13f', 'D_13g', 'D_13h', 'D_14', 'D_15-1', 'D_15-2',
 'E_9-1', 'E_10-1 ','E_11-1', 'E_12-1', 'E_13-1', 'E_9-2', 'E_10-2', 'E_11-2', 'E_12-2', 'E_13-2',
 'E_9-3', 'E_10-3', 'E_11-3', 'E_14',
 'E_15a', 'E_15b', 'E_15c', 'E_15d', 'E_15e', 'E_15f', 'E_15g', 'E_15h',
 'E_16', 'E_17-1', 'E_17-2']
# Specify new column names for data analysis (ensure they match the exact order of the existing columns)

list_del_cols = ['Timestamp','Consent','5', 'A_14', 'B_18-1', 'C_15']
# Specify the columns to be excluded from the data analysis

miss_col = ['1', '2', '3', '4', '7','Module']
# Specify all columns that apply to all respondents for missing value detection

open_cols = ['5_Other', 'B_18_1_Other','A_11-1','A_11-2','A_11-3','A_16-1', 'A_16-2','B_12-1',
            'B_12-2','B_12-3','B_12-4','B_14','B_18_1_Other','B_18-2','B_20-1', 'B_20-2',
            'C_12-1', 'C_12-2', 'C_15_Other', 'C_17-1', 'C_17-2', 'D_11-1', 'D_11-2', 'D_15-1', 'D_15-2',
            'E_11-1', 'E_11-2', 'E_11-3','E_17-1', 'E_17-2', 'Comment']
# Specify the open-ended columns (which will be saved in a separate Excel sheet and removed from the data frame)

age_col = '2'
# If we don't have age group in this dataset, please specify the age columns (as str)

diss_cols = ['6a','6b', '6c', '6d', '6e', '6f']
# If we have WG-SS questions in the dataset, please specify the columns (as list [])

new_cols_order = ['Timestamp', 'Consent', '0', 'Email', 'Phone','Module', '1', '2', '3', '3-1', '4', '5', '5a', '5b', '5c', '5d', '5e',  '5f', '5g',
 '5_Other', '6a','6b', '6c', '6d', '6e', '6f',
 '7','8', 'A_9-1', 'A_10-1', 'A_11-1', 'A_12-1', 'A_13-1', 'A_9-2', 'A_10-2', 'A_11-2', 'A_12-2', 
 'A_13-2', 'A_9-3', 'A_10-3', 'A_11-3', 'A_12-3', 'A_13-3', 'A_14', 'A_14a', 'A_14b', 'A_14c', 'A_14d', 
'A_14e', 'A_14f', 'A_14g', 'A_14h', 'A_14i','A_15', 'A_16-1', 'A_16-2',
 'B_9-1', 'B_10-1', 'B_12-1', 'B_15-1', 'B_9-2', 'B_10-2', 'B_12-2', 'B_15-2',
 'B_9-3', 'B_11-3', 'B_12-3', 'B_15-3', 'B_9-4', 'B_11-4', 'B_12-4', 'B_15-4',
 'B_9-5','B_13', 'B_14', 'B_15-5', 'B_16', 'B_17', 'B_18-1', 'B_18_1a', 'B_18_1b', 
'B_18_1c', 'B_18_1d', 'B_18_1e', 'B_18_1_Other', 'B_18-2', 'B_19', 'B_20-1', 'B_20-2',
 'C_9-1', 'C_10-1', 'C_12-1', 'C_13-1', 'C_9-2', 'C_10-2', 'C_12-2', 'C_13-2',
 'C_14', 'C_15', 'C_15a', 'C_15b', 'C_15c', 'C_15d', 'C_15e', 'C_15_Other', 'C_16', 'C_17-1', 'C_17-2',
 'D_9-1', 'D_10-1', 'D_11-1', 'D_12-1', 'D_9-2', 'D_10-2', 'D_11-2', 'D_12-2',
 'D_13a', 'D_13b', 'D_13c', 'D_13d', 'D_13e', 'D_13f', 'D_13g', 'D_13h', 'D_14', 'D_15-1', 'D_15-2',
 'E_9-1', 'E_10-1 ','E_11-1', 'E_12-1', 'E_13-1', 'E_9-2', 'E_10-2', 'E_11-2', 'E_12-2', 'E_13-2',
 'E_9-3', 'E_10-3', 'E_11-3', 'E_14',
 'E_15a', 'E_15b', 'E_15c', 'E_15d', 'E_15e', 'E_15f', 'E_15g', 'E_15h',
 'E_16', 'E_17-1', 'E_17-2', 'Comment']


"""
Run the pipeline for data preprocessing
del_type = 0 or 1
-> 0: Remove all missing values from the columns where missing values are detected
-> 1: First, remove columns where missing values make up 10% or more of the total data points
      Then, remove all remaining missing values from the columns where they are detected
"""

banaba = dp.Preprocessing(project_name, file_path, file_path_others, list_del_cols, dates, miss_col, email, phone, identifiers, open_cols, cols_new, new_cols_order, age_col, diss_cols, del_type = 0, file_type=file_type)
banaba.processing()