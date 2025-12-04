#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ijeong-yeon
"""

import bodhi_indicator as bd
import bodhi_PMF as pmf
import pandas as pd

"""
Evaluation
"""
# Specify the file path for the clean dataset
df = pd.read_excel('data/25-UNICEF-PH-1 - Clean Dataset.xlsx')

# Create indicators and provide additional details as needed (Evaluation)
def statistics(df, indicators):
    
    module = bd.Indicator(df, "Module", 0, ['Module'], i_cal=None, i_type='count', description='Module distribution', period='endline', target = None)
    module.add_var_order(['A', 'B', 'C', 'D', 'E'])
    indicators.append(module)
    
    gender = bd.Indicator(df, "Gender", 0, ['1'], i_cal=None, i_type='count', description='1. What is your sex/gender?', period='endline', target = None)
    gender.add_breakdown({'Module':'Module'})
    gender.add_var_order(['Female', 'Male'])
    indicators.append(gender)
    
    region = bd.Indicator(df, "Province", 0, ['3'], i_cal=None, i_type='count', description='3. Which province are you a resident of?', period='endline', target = None)
    region.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    region.add_var_order(['Lanao del Sur', 'Bukidnon', 'Lanao del Norte'])
    indicators.append(region)
    
    age = bd.Indicator(df, "Age group", 0, ['Age Group'], i_cal=None, i_type='count', description='Age Group distribution', period='endline', target = None)
    age.add_breakdown({'Module':'Module','1':'Gender'})
    age.add_var_order(['18 - 24','25 - 34', '35 - 44', '45 - 54', '55 - 64'])
    indicators.append(age)
    
    disability = bd.Indicator(df, "Disability", 0, ['Disability'], i_cal=None, i_type='count', description='Disability distribution', period='endline', target = None)
    disability.add_breakdown({'Module':'Module','1':'Gender'})
    disability.add_var_order(['No Disability', 'Disability'])
    indicators.append(disability)
    
    education = bd.Indicator(df, "Education", 0, ['4'], i_cal=None, i_type='count', description='4. What is the highest level of school you have ever attended? ', period='endline', target = None)
    education.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    education.add_var_order(['Higher', 'Upper secondary', 'Lower secondary','Primary', 'Ece/ed','Unsure'])
    indicators.append(education)
    
    role = bd.Indicator(df, "Position", 0, ['5a', '5b', '5c', '5d', '5e',  '5f', '5g'], i_cal=None, i_type='count', description='5. What is your current position related to this project?', period='endline', target = None, visual = False)
    role.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    role.add_var_change({1: "Yes", 0: "No"})
    role.add_var_order([1, 0])
    role.add_label(["Local government official",
                    "Health office personnel (Municipal health officer)",
                    "Healthcare worker",
                    "NGO stakeholder",
                    "School head",
                    "Social worker",
                    "Teacher"])
    indicators.append(role)
    
    donour1 = bd.Indicator(df, "Donour_1", 0, ['7'], i_cal=None, i_type='count', description='7. Are you aware of the donor of the activities you have participated in?', period='endline', target = None)
    donour1.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    donour1.add_var_order(['Yes', 'No'])
    indicators.append(donour1)  
    
    donour2 = bd.Indicator(df, "Donour_2", 0, ['8'], i_cal=None, i_type='count', description='8. Who is the donor of the activities provided by UNICEF?', period='endline', target = None)
    donour2.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    donour2.add_var_order(['EU', 'USAID', 'JICA', 'GIZ', 'KOICA','Other'])
    indicators.append(donour2)  
    
    # Module A
    
    a_9_1 = bd.Indicator(df, "Module_A_9_1", 0, ['A_9-1'], i_cal=None, i_type='count', description='Have you participated in "Training on National Immunization Program"?', period='endline', target = None, visual = False)
    a_9_1.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    a_9_1.add_var_order(["Yes",
                           "No"])
    indicators.append(a_9_1)
    
    a_10_1 = bd.Indicator(df, "Module_A_10_1", 0, ['A_10-1'], i_cal=None, i_type='count', description="To what extent have you applied knowledge from Training on National Immunization Program in your work over the past six months?", period='endline', target = None, visual = False)
    a_10_1.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    a_10_1.add_var_order(["5 - To a very great extent",
                           "4 - To a great extent",
                           "3 - To some extent"])
    indicators.append(a_10_1)  
    
    a_12_1 = bd.Indicator(df, "Module_A_12_1", 0, ['A_12-1'], i_cal=None, i_type='count', description="Did Training on National Immunization Program include a component on integrating gender equality into your work?", period='endline', target = None, visual = False)
    a_12_1.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    a_12_1.add_var_order(["Yes",
                           "No"])
    indicators.append(a_12_1)  
    
    a_13_1 = bd.Indicator(df, "Module_A_13_1", 0, ['A_13-1'], i_cal=None, i_type='count', description="To what extent do you try to apply gender equality in your work?", period='endline', target = None, visual = False)
    a_13_1.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    a_13_1.add_var_order([1,
                           2,
                           3,
                           4,
                           5])
    indicators.append(a_13_1)
    
    a_9_2 = bd.Indicator(df, "Module_A_9_2", 0, ['A_9-2'], i_cal=None, i_type='count', description="Have you participated in Training on the Philippine Approach to Sustainable Sanitation (PHATSS)?", period='endline', target = None, visual = False)
    a_9_2.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    a_9_2.add_var_order(["Yes",
                           "No"])
    indicators.append(a_9_2)
    
    a_10_2 = bd.Indicator(df, "Module_A_10_2", 0, ['A_10-2'], i_cal=None, i_type='count', description="To what extent have you applied knowledge from Training on PHATSS in your work over the past six months?", period='endline', target = None, visual = False)
    a_10_2.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    a_10_2.add_var_order(["5 - To a very great extent",
                           "4 - To a great extent",
                           "3 - To some extent",
                           "2 - To a small extent"])
    indicators.append(a_10_2)
    
    a_12_2 = bd.Indicator(df, "Module_A_12_2", 0, ['A_12-2'], i_cal=None, i_type='count', description="Did Training on PHATSS include a component on integrating gender equality into your work?", period='endline', target = None, visual = False)
    a_12_2.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    a_12_2.add_var_order(["Yes",
                           "No"])
    indicators.append(a_12_2)
    
    a_13_2 = bd.Indicator(df, "Module_A_13_2", 0, ['A_13-2'], i_cal=None, i_type='count', description="To what extent do you try to apply gender equality in your work?", period='endline', target = None, visual = False)
    a_13_2.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    a_13_2.add_var_order([1,
                           2,
                           3,
                           4,
                           5])
    indicators.append(a_13_2)
    
    a_9_3 = bd.Indicator(df, "Module_A_9_3", 0, ['A_9-3'], i_cal=None, i_type='count', description="Have you participated in WASH in Emergencies Training?", period='endline', target = None, visual = False)
    a_9_3.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    a_9_3.add_var_order(["Yes",
                           "No"])
    indicators.append(a_9_3)
    
    a_10_3 = bd.Indicator(df, "Module_A_10_3", 0, ['A_10-3'], i_cal=None, i_type='count', description="To what extent have you applied knowledge from WASH in Emergencies Training in your work over the past six months?", period='endline', target = None, visual = False)
    a_10_3.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    a_10_3.add_var_order(["5 - To a very great extent",
                           "4 - To a great extent",
                           "3 - To some extent",
                           "2 - To a small extent"])
    indicators.append(a_10_3)
    
    a_12_3 = bd.Indicator(df, "Module_A_12_3", 0, ['A_12-3'], i_cal=None, i_type='count', description="Did WASH in Emergencies Training include a component on integrating gender equality into your work?", period='endline', target = None, visual = False)
    a_12_3.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    a_12_3.add_var_order(["Yes",
                           "No"])
    indicators.append(a_12_3)
    
    a_13_3 = bd.Indicator(df, "Module_A_13_3", 0, ['A_13-3'], i_cal=None, i_type='count', description="To what extent do you try to apply gender equality in your work?", period='endline', target = None, visual = False)
    a_13_3.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    a_13_3.add_var_order([1,
                           2,
                           3,
                           4,
                           5])
    indicators.append(a_13_3)
    
    a_14 = bd.Indicator(df, "Module_A_14", 0, ['A_14a', 'A_14b', 'A_14c', 'A_14d', 'A_14e', 'A_14f', 'A_14g', 'A_14h', 'A_14i'], i_cal=None, i_type='count', description="Over the past six months, who have your Health/Nutrition/WASH services targeted?", period='endline', target = None, visual = False)
    a_14.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    a_14.add_var_change({1: "Yes", 0: "No"})
    a_14.add_var_order([1, 0])
    a_14.add_label(["Boys",
                    "None of them",
                    "Adolescents",
                    "Persons with disabilities",
                    "Internally displaced persons (IDPs)",
                    "Grils",
                    "Women (Adult)",
                    "Men (Adult)",
                    "Refugee"])
    indicators.append(a_14)
    
    a_15 = bd.Indicator(df, "Module_A_15", 0, ['A_15'], i_cal=None, i_type='count', description="Overall, to what extent has your capacity to deliver health, nutrition, or WASH services improved through UNICEF", period='endline', target = None, visual = False)
    a_15.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    a_15.add_var_order(["5 - To a very great extent",
                           "4 - To a great extent",
                           "3 - To some extent",
                           "2 - To a small extent",
                           "Unsure"])
    indicators.append(a_15)
    
    # Module B
    
    b_9_1 = bd.Indicator(df, "Module_B_9_1", 0, ['B_9-1'], i_cal=None, i_type='count', description="Have you participated in ECCD Strategic Planning Workshop?", period='endline', target = None, visual = False)
    b_9_1.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    b_9_1.add_var_order(["Yes",
                           "No"])
    indicators.append(b_9_1)
    
    b_10_1 = bd.Indicator(df, "Module_B_10_1", 0, ['B_10-1'], i_cal=None, i_type='count', description="In the past six months, to what extent have you applied what you learned from early learning activities in your work?", period='endline', target = None, visual = False)
    b_10_1.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    b_10_1.add_var_order(["5 - To a very great extent",
                           "4 - To a great extent",
                           "3 - To some extent",
                           "2 - To a small extent"])
    indicators.append(b_10_1)
    
    b_15_1 = bd.Indicator(df, "Module_B_15_1", 0, ['B_15-1'], i_cal=None, i_type='count', description="Did ECCD Strategic Planning Workshop include a component on integrating gender equality into education?", period='endline', target = None, visual = False)
    b_15_1.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    b_15_1.add_var_order(["Yes",
                           "No",
                           "Unsure"])
    indicators.append(b_15_1)
    
    b_9_2 = bd.Indicator(df, "Module_B_9_2", 0, ['B_9-2'], i_cal=None, i_type='count', description="Have you participated in Expansion of Early Learning Services?", period='endline', target = None, visual = False)
    b_9_2.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    b_9_2.add_var_order(["Yes",
                           "No"])
    indicators.append(b_9_2)
    
    b_10_2 = bd.Indicator(df, "Module_B_10_2", 0, ['B_10-2'], i_cal=None, i_type='count', description="In the past six months, to what extent have you applied what you learned from early learning activities in your work?", period='endline', target = None, visual = False)
    b_10_2.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    b_10_2.add_var_order(["5 - To a very great extent",
                           "4 - To a great extent",
                           "3 - To some extent",
                           "2 - To a small extent"])
    indicators.append(b_10_2)
    
    b_15_2 = bd.Indicator(df, "Module_B_15_2", 0, ['B_15-2'], i_cal=None, i_type='count', description="Did Expansion of Early Learning Services include a component on integrating gender equality into education?", period='endline', target = None, visual = False)
    b_15_2.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    b_15_2.add_var_order(["Yes",
                           "No",
                           "Unsure"])
    indicators.append(b_15_2)
    
    b_9_3 = bd.Indicator(df, "Module_B_9_3", 0, ['B_9-3'], i_cal=None, i_type='count', description="Have you participated in Training on curriculum and teaching methods?", period='endline', target = None, visual = False)
    b_9_3.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    b_9_3.add_var_order(["Yes",
                           "No"])
    indicators.append(b_9_3)
    
    b_11_3 = bd.Indicator(df, "Module_B_11_3", 0, ['B_11-3'], i_cal=None, i_type='count', description="Since participating in training on curriculum and teaching methods or ALS, to what extent have you applied the new teaching curriculum and methods, or ALS teaching methods, in your class?", period='endline', target = None, visual = False)
    b_11_3.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    b_11_3.add_var_order(["5 - To a very great extent",
                           "4 - To a great extent",
                           "3 - To some extent",
                           "2 - To a small extent",
                           "1 - Not at all"])
    indicators.append(b_11_3)
    
    b_15_3 = bd.Indicator(df, "Module_B_15_3", 0, ['B_15-3'], i_cal=None, i_type='count', description="Did Training on curriculum and teaching methods include a component on integrating gender equality into education?", period='endline', target = None, visual = False)
    b_15_3.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    b_15_3.add_var_order(["Yes",
                           "No",
                           "Unsure"])
    indicators.append(b_15_3)
    
    b_9_4 = bd.Indicator(df, "Module_B_9_4", 0, ['B_9-4'], i_cal=None, i_type='count', description="Have you participated in Training on ALS?", period='endline', target = None, visual = False)
    b_9_4.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    b_9_4.add_var_order(["Yes",
                           "No"])
    indicators.append(b_9_4)
    
    b_11_4 = bd.Indicator(df, "Module_B_11_4", 0, ['B_11-4'], i_cal=None, i_type='count', description="Since participating in training on curriculum and teaching methods or ALS, to what extent have you applied the new teaching curriculum and methods, or ALS teaching methods, in your class?", period='endline', target = None, visual = False)
    b_11_4.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    b_11_4.add_var_order(["5 - To a very great extent",
                           "4 - To a great extent",
                           "3 - To some extent",
                           "2 - To a small extent",
                           "1 - Not at all"])
    indicators.append(b_11_4)
    
    b_15_4 = bd.Indicator(df, "Module_B_15_4", 0, ['B_15-4'], i_cal=None, i_type='count', description="Did Training on ALS include a component on integrating gender equality into education?", period='endline', target = None, visual = False)
    b_15_4.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    b_15_4.add_var_order(["Yes",
                           "No",
                           "Unsure"])
    indicators.append(b_15_4)
    
    b_9_5 = bd.Indicator(df, "Module_B_9_5", 0, ['B_9-5'], i_cal=None, i_type='count', description="Have you participated in School-Based Management (SBM) Fundamentals course?", period='endline', target = None, visual = False)
    b_9_5.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    b_9_5.add_var_order(["Yes",
                           "No"])
    indicators.append(b_9_5)
    
    b_13 = bd.Indicator(df, "Module_B_13", 0, ['B_13'], i_cal=None, i_type='count', description="Since your training on the SBM Fundamentals course,\nhave you changed or adapted your school management practices?", period='endline', target = None)
    b_13.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    b_13.add_var_order(["Yes",
                           "No"])
    indicators.append(b_13)
    
    b_15_5 = bd.Indicator(df, "Module_B_15_5", 0, ['B_15-5'], i_cal=None, i_type='count', description="Did School-Based Management Fundamentals course include a component on integrating gender equality into education?", period='endline', target = None, visual = False)
    b_15_5.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    b_15_5.add_var_order(["Yes",
                           "No",
                           "Unsure"])
    indicators.append(b_15_5)
    
    b_16 = bd.Indicator(df, "Module_B_16", 0, ['B_16'], i_cal=None, i_type='count', description="Is there a school improvement plan currently ongoing or planned at your school?", period='endline', target = None)
    b_16.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    b_16.add_var_order(["Yes",
                           "No",
                           "Unsure"])
    indicators.append(b_16)
    
    b_17 = bd.Indicator(df, "Module_B_17", 0, ['B_17'], i_cal=None, i_type='count', description="Have WASH components been included in your school improvement plan?", period='endline', target = None, visual = False)
    b_17.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    b_17.add_var_order(["Yes",
                           "No",
                           "Unsure"])
    indicators.append(b_17)
    
    b_18_1 = bd.Indicator(df, "Module_B_18_1", 0, ['B_18_1a', 'B_18_1b', 'B_18_1c', 'B_18_1d', 'B_18_1e'], i_cal=None, i_type='count', description='What WASH components have been included in your school improvement plan?', period='endline', target = None, visual = False)
    b_18_1.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    b_18_1.add_var_change({1: "Yes", 0: "No"})
    b_18_1.add_var_order([1, 0])
    b_18_1.add_label(["Menstrual hygiene management",
                      "Upgrade of toilet",
                      "Upgrade of handwashing facilities",
                      "Hygiene promotion",
                      "Upgrade of water",])
    indicators.append(b_18_1)
    
    b_19 = bd.Indicator(df, "Module_B_19", 0, ['B_19'], i_cal=None, i_type='count', description="Overall, to what extent has your capacity to deliver education services improved through UNICEF", period='endline', target = None, visual = False)
    b_19.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    b_19.add_var_order(["5 - To a very great extent",
                           "4 - To a great extent",
                           "3 - To some extent",
                           "2 - To a small extent",
                           "1 - Not at all"])
    indicators.append(b_19)
    
    # Module C
    
    c_9_1 = bd.Indicator(df, "Module_C_9_1", 0, ['C_9-1'], i_cal=None, i_type='count', description="Have you participated in Training on\nthe Monitoring and Reporting Mechanism related to the protection of children and women?", period='endline', target = None)
    c_9_1.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    c_9_1.add_var_order(["Yes",
                         "No"])
    indicators.append(c_9_1)
    
    c_10_1 = bd.Indicator(df, "Module_C_10_1", 0, ['C_10-1'], i_cal=None, i_type='count', description="Have you applied the skills from Training on the Monitoring and Reporting Mechanism related to the protection of children and women in responding to child protection cases?", period='endline', target = None, visual = False)
    c_10_1.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    c_10_1.add_var_order(["Yes",
                         "No"])
    indicators.append(c_10_1)
    
    c_13_1 = bd.Indicator(df, "Module_C_13_1", 0, ['C_13-1'], i_cal=None, i_type='count', description="Did Training on the Monitoring and Reporting Mechanism related to the protection of children and women include a component on integrating gender equality into your work?", period='endline', target = None, visual = False)
    c_13_1.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    c_13_1.add_var_order(["Yes",
                         "No"])
    indicators.append(c_13_1)
    
    c_9_2 = bd.Indicator(df, "Module_C_9_2", 0, ['C_9-2'], i_cal=None, i_type='count', description="Have you participated in Training on the Child Protection and Case Management?", period='endline', target = None)
    c_9_2.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    c_9_2.add_var_order(["Yes",
                         "No"])
    indicators.append(c_9_2)
    
    c_10_2 = bd.Indicator(df, "Module_C_10_2", 0, ['C_10-2'], i_cal=None, i_type='count', description="Have you applied the skills from Training on the Child Protection and Case Management in responding to child protection cases?", period='endline', target = None, visual = False)
    c_10_2.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    c_10_2.add_var_order(["Yes",
                         "No"])
    indicators.append(c_10_2)
    
    c_13_2 = bd.Indicator(df, "Module_C_13_2", 0, ['C_13-2'], i_cal=None, i_type='count', description="Did Training on the Child Protection and Case Management include a component on integrating gender equality into your work?", period='endline', target = None, visual = False)
    c_13_2.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    c_13_2.add_var_order(["Yes",
                         "No"])
    indicators.append(c_13_2)
    
    c_14 = bd.Indicator(df, "Module_C_14", 0, ['C_14'], i_cal=None, i_type='count', description="To what extent do you try to apply gender equality in your work?", period='endline', target = None, visual = False)
    c_14.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    c_14.add_var_order([1,
                           2,
                           3,
                           4,
                           5])
    indicators.append(c_14)
    
    c_15 = bd.Indicator(df, "Module_C_15", 0, ['C_15a', 'C_15b', 'C_15c', 'C_15d', 'C_15e'], i_cal=None, i_type='count', description='Over the past six months, who have your child protection services targeted?', period='endline', target = None, visual = False)
    c_15.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    c_15.add_var_change({1: "Yes", 0: "No"})
    c_15.add_var_order([1, 0])
    c_15.add_label(["Boys",
                    "Adolescents",
                    "Girls",
                    "Children with disabilities",
                    "Displaced children"])
    indicators.append(c_15)
    
    c_16 = bd.Indicator(df, "Module_C_16", 0, ['C_16'], i_cal=None, i_type='count', description="Overall, to what extent has your capacity to deliver child protection services improved through UNICEF", period='endline', target = None, visual = False)
    c_16.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    c_16.add_var_order(["5 - To a very great extent",
                           "4 - To a great extent",
                           "3 - To some extent",
                           "2 - To a small extent",
                           "1 - Not at all"])
    indicators.append(c_16)
    
    # Module D
    
    d_9_1 = bd.Indicator(df, "Module_D_9_1", 0, ['D_9-1'], i_cal=None, i_type='count', description="Have you participated in Capacity-building activities for the upcoming Child-Friendly Local Governance Audit (CFLGA)?", period='endline', target = None, visual = False)
    d_9_1.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    d_9_1.add_var_order(["Yes",
                         "No"])
    indicators.append(d_9_1)
    
    d_10_1 = bd.Indicator(df, "Module_D_10_1", 0, ['D_10-1'], i_cal=None, i_type='count', description="To what extent have you applied knowledge from Capacity-building activities for the upcoming Child-Friendly Local Governance Audit (CFLGA) in your work over the past six months?", period='endline', target = None, visual = False)
    d_10_1.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    d_10_1.add_var_order(["5 - To a very great extent",
                           "4 - To a great extent",
                           "3 - To some extent",
                           "2 - To a small extent",
                           "1 - Not at all"])
    indicators.append(d_10_1)
    
    d_12_1 = bd.Indicator(df, "Module_D_12_1", 0, ['D_12-1'], i_cal=None, i_type='count', description="Since the training on child-friendly local governance/DRR, has your LGU integrated gender priorities into its plans or budget?", period='endline', target = None, visual = False)
    d_12_1.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    d_12_1.add_var_order(["Yes",
                         "No",
                         "Unsure"])
    indicators.append(d_12_1)
    
    d_9_2 = bd.Indicator(df, "Module_D_9_2", 0, ['D_9-2'], i_cal=None, i_type='count', description="Have you participated in Coaching and Mentoring sessions for the upcoming CFLGA?", period='endline', target = None, visual = False)
    d_9_2.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    d_9_2.add_var_order(["Yes",
                         "No"])
    indicators.append(d_9_2)
    
    d_10_2 = bd.Indicator(df, "Module_D_10_2", 0, ['D_10-2'], i_cal=None, i_type='count', description="To what extent have you applied knowledge from Coaching and Mentoring sessions for the upcoming CFLGA in your work over the past six months?", period='endline', target = None, visual = False)
    d_10_2.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    d_10_2.add_var_order(["5 - To a very great extent",
                           "4 - To a great extent",
                           "3 - To some extent",
                           "2 - To a small extent",
                           "1 - Not at all"])
    indicators.append(d_10_2)
    
    d_12_2 = bd.Indicator(df, "Module_D_12_2", 0, ['D_12-2'], i_cal=None, i_type='count', description="Since the training on child-friendly local governance/DRR, has your LGU integrated gender priorities into its plans or budget?", period='endline', target = None, visual = False)
    d_12_2.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    d_12_2.add_var_order(["Yes",
                         "No",
                         "Unsure"])
    indicators.append(d_12_2)
    
    d_13a = bd.Indicator(df, "Module_D_13a", 0, ['D_13a'], i_cal=None, i_type='count', description="To what extent does your LGU currently consider the following groups in its plans and budget?: Boys", period='endline', target = None, visual = False)
    d_13a.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    d_13a.add_var_order(["Not at all",
                         "Rarely",
                         "Sometimes",
                         "Often",
                         "Almost always"])
    indicators.append(d_13a)
    
    d_13b = bd.Indicator(df, "Module_D_13b", 0, ['D_13b'], i_cal=None, i_type='count', description="To what extent does your LGU currently consider the following groups in its plans and budget?: Girls", period='endline', target = None, visual = False)
    d_13b.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    d_13b.add_var_order(["Not at all",
                         "Rarely",
                         "Sometimes",
                         "Often",
                         "Almost always"])
    indicators.append(d_13b)
    
    d_13c = bd.Indicator(df, "Module_D_13c", 0, ['D_13c'], i_cal=None, i_type='count', description="To what extent does your LGU currently consider the following groups in its plans and budget?: Adolescents", period='endline', target = None, visual = False)
    d_13c.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    d_13c.add_var_order(["Not at all",
                         "Rarely",
                         "Sometimes",
                         "Often",
                         "Almost always"])
    indicators.append(d_13c)
    
    d_13d = bd.Indicator(df, "Module_D_13d", 0, ['D_13d'], i_cal=None, i_type='count', description="To what extent does your LGU currently consider the following groups in its plans and budget?: Women (Adult)", period='endline', target = None, visual = False)
    d_13d.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    d_13d.add_var_order(["Not at all",
                         "Rarely",
                         "Sometimes",
                         "Often",
                         "Almost always"])
    indicators.append(d_13d)
    
    d_13e = bd.Indicator(df, "Module_D_13e", 0, ['D_13e'], i_cal=None, i_type='count', description="To what extent does your LGU currently consider the following groups in its plans and budget?: Men (Adult)", period='endline', target = None, visual = False)
    d_13e.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    d_13e.add_var_order(["Not at all",
                         "Rarely",
                         "Sometimes",
                         "Often",
                         "Almost always"])
    indicators.append(d_13e)
    
    d_13f = bd.Indicator(df, "Module_D_13f", 0, ['D_13f'], i_cal=None, i_type='count', description="To what extent does your LGU currently consider the following groups in its plans and budget?: Persons with disabilities", period='endline', target = None, visual = False)
    d_13f.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    d_13f.add_var_order(["Not at all",
                         "Rarely",
                         "Sometimes",
                         "Often",
                         "Almost always"])
    indicators.append(d_13f)
    
    d_13g = bd.Indicator(df, "Module_D_13g", 0, ['D_13g'], i_cal=None, i_type='count', description="To what extent does your LGU currently consider the following groups in its plans and budget?: Internally displaced persons (IDPs)", period='endline', target = None, visual = False)
    d_13g.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    d_13g.add_var_order(["Not at all",
                         "Rarely",
                         "Sometimes",
                         "Often",
                         "Almost always"])
    indicators.append(d_13g)
    
    d_13h = bd.Indicator(df, "Module_D_13h", 0, ['D_13h'], i_cal=None, i_type='count', description="To what extent does your LGU currently consider the following groups in its plans and budget?: Refugees", period='endline', target = None, visual = False)
    d_13h.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    d_13h.add_var_order(["Not at all",
                         "Rarely",
                         "Sometimes",
                         "Often",
                         "Almost always"])
    indicators.append(d_13h)
    
    d_14 = bd.Indicator(df, "Module_D_14", 0, ['D_14'], i_cal=None, i_type='count', description="Overall, to what extent has your capacity in child-friendly local governance (CFLG) or DRR management and planning improved through UNICEF", period='endline', target = None, visual = False)
    d_14.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    d_14.add_var_order(["5 - To a very great extent",
                           "4 - To a great extent",
                           "3 - To some extent",
                           "2 - To a small extent",
                           "1 - Not at all"])
    indicators.append(d_14)
    
    # Module E
    
    e_9_1 = bd.Indicator(df, "Module_E_9_1", 0, ['E_9-1'], i_cal=None, i_type='count', description="Which training or activities supported by UNICEF have you participated in?: Emergency Preparedness and Response (EPR) Training?", period='endline', target = None, visual = False)
    e_9_1.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    e_9_1.add_var_order(["Yes",
                         "No"])
    indicators.append(e_9_1)
    
    e_10_1 = bd.Indicator(df, "Module_E_10_1", 0, ['E_10-1 '], i_cal=None, i_type='count', description="To what extent have you applied knowledge from Emergency Preparedness and Response (EPR) Training in your work over the past six months?", period='endline', target = None, visual = False)
    e_10_1.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    e_10_1.add_var_order(["5 - To a very great extent",
                           "4 - To a great extent",
                           "3 - To some extent",
                           "2 - To a small extent",
                           "1 - Not at all"])
    indicators.append(e_10_1)
    
    e_12_1 = bd.Indicator(df, "Module_E_12_1", 0, ['E_12-1'], i_cal=None, i_type='count', description="Did Emergency Preparedness and Response (EPR) Training include a component on integrating gender equality into your work?", period='endline', target = None, visual = False)
    e_12_1.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    e_12_1.add_var_order(["Yes",
                         "No",
                         "Unsure"])
    indicators.append(e_12_1)
    
    e_13_1 = bd.Indicator(df, "Module_E_13_1", 0, ['E_13-1'], i_cal=None, i_type='count', description="To what extent do you try to apply gender equality in your work? (from Emergency Preparedness and Response (EPR) Training)", period='endline', target = None, visual = False)
    e_13_1.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    e_13_1.add_var_order([1,
                           2,
                           3,
                           4,
                           5])
    indicators.append(e_13_1)
    
    e_9_2 = bd.Indicator(df, "Module_E_9_2", 0, ['E_9-2'], i_cal=None, i_type='count', description="Have you participated in Training of Trainers (ToT) on Child Protection in Emergencies and Emergency Preparedness and Response?", period='endline', target = None, visual = False)
    e_9_2.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    e_9_2.add_var_order(["Yes",
                         "No"])
    indicators.append(e_9_2)
    
    e_10_2 = bd.Indicator(df, "Module_E_10_2", 0, ['E_10-2'], i_cal=None, i_type='count', description="To what extent have you applied the knowledge gained from ToT on Child Protection in Emergencies and Emergency Preparedness and Response in child protection during emergency situations, over the past six months?", period='endline', target = None, visual = False)
    e_10_2.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    e_10_2.add_var_order(["5 - To a very great extent",
                           "4 - To a great extent",
                           "3 - To some extent",
                           "2 - To a small extent",
                           "1 - Not at all"])
    indicators.append(e_10_2)
    
    e_12_2 = bd.Indicator(df, "Module_E_12_2", 0, ['E_12-2'], i_cal=None, i_type='count', description="Did ToT on Child Protection in Emergencies and Emergency Preparedness and Response include a component on integrating gender equality into your work?", period='endline', target = None, visual = False)
    e_12_2.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    e_12_2.add_var_order(["Yes",
                         "No"])
    indicators.append(e_12_2)
    
    e_13_2 = bd.Indicator(df, "Module_E_13_2", 0, ['E_13-2'], i_cal=None, i_type='count', description="To what extent do you try to apply gender equality in your work? (from Emergency Preparedness and Response (EPR) Training)", period='endline', target = None, visual = False)
    e_13_2.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    e_13_2.add_var_order([1,
                           2,
                           3,
                           4,
                           5])
    indicators.append(e_13_2)
    
    e_9_3 = bd.Indicator(df, "Module_E_9_3", 0, ['E_9-3'], i_cal=None, i_type='count', description="Have you participated in Emergency Preparedness and Response Training?", period='endline', target = None, visual = False)
    e_9_3.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    e_9_3.add_var_order(["Yes",
                         "No"])
    indicators.append(e_9_3)
    
    e_10_3 = bd.Indicator(df, "Module_E_10_3", 0, ['E_10-3'], i_cal=None, i_type='count', description="To what extent have you applied knowledge from Emergency Preparedness and Response Training in your work over the past six months?", period='endline', target = None, visual = False)
    e_10_3.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    e_10_3.add_var_order(["5 - To a very great extent",
                           "4 - To a great extent",
                           "3 - To some extent",
                           "2 - To a small extent",
                           "1 - Not at all"])
    indicators.append(e_10_3)
    
    e_14 = bd.Indicator(df, "Module_E_14", 0, ['E_14'], i_cal=None, i_type='count', description="Since the training on child-friendly local governance/DRR, has your LGU integrated gender priorities into its plans or budget?", period='endline', target = None, visual = False)
    e_14.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    e_14.add_var_order(["Yes",
                         "No",
                         "Unsure"])
    indicators.append(e_14)
    
    e_15 = bd.Indicator(df, "Module_E_15", 0, ['E_15a', 'E_15b', 'E_15c', 'E_15d', 'E_15e', 'E_15f', 'E_15g', 'E_15h'], i_cal=None, i_type='count', description=" To what extent does your LGU currently consider the following groups in its plans and budget?", period='endline', target = None, visual = False)
    e_15.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    e_15.add_var_change({1: "Yes", 0: "No"})
    e_15.add_var_order([1, 0])
    e_15.add_label(["Boys",
                    "Girls",
                    "Adolescents",
                    "Women (Adult)",
                    "Men (Adult)",
                    "Persons with disabilities",
                    "Internally displaced persons (IDPs)",
                    "Refugees"])
    indicators.append(e_15)
    
    e_16 = bd.Indicator(df, "Module_E_16", 0, ['E_16'], i_cal=None, i_type='count', description="Overall, to what extent has your capacity in child-friendly local governance (CFLG) or DRR management and planning improved through UNICEF", period='endline', target = None, visual = False)
    e_16.add_breakdown({'Module':'Module','1':'Gender', 'Age Group':'Age Group', 'Disability' : 'Disability'})
    e_16.add_var_order(["5 - To a very great extent",
                           "4 - To a great extent",
                           "3 - To some extent",
                           "2 - To a small extent",
                           "1 - Not at all"])
    indicators.append(e_16)
    
    
       
    return indicators
    
# Create indicators for several statistical tests such as OLS, ANOVA, T-test and Chi2
def statistical_indicators(df, indicators):
    
    return indicators



# Create the PMF class ('Project Title', 'Evaluation')
banaba = pmf.PerformanceManagementFramework('Banaba', 'Evaluation')

#Overall
indicators = []
indicators = statistics(df, indicators)
indicators = statistical_indicators(df, indicators)
banaba.add_indicators(indicators)

file_path1 = 'data/Banaba Statistics.xlsx' # File path to save the statistics (including breakdown data)
file_path2 = 'data/Banaba Test Results.xlsx'  # File path to save the chi2 test results
folder = 'visuals/' # File path for saving visuals

banaba.PMF_generation(file_path1, file_path2, folder) # Run the PMF


