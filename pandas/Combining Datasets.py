import pandas as pd
df = pd.read_csv('diabets_sample.csv')
df2 = pd.read_csv('diabets_sample2.csv', index_col='PatientID')

data1 = pd.concat([df, df2])
df3 = pd.read_csv('diabets_sample3.csv', index_col='PatientID')
data2 = pd.concat([data1,df3], axis=1)
# combines all the rows in ​both the dataframes. ​It contains the
# BMI and age from the dataframe of df3, ​and the remaining information
# that is pregnancies, ​glucose, diabetes, pedigree function, ​and outcome
# from data 1 dataframe, ​wherein it has no values of BMI, ​age for those patient IDs

df_left = pd.merge(data1, df3, on='PatientID', how='left')
# will result in a dataframe ​containing only 25
# records from left dataframe.
df_right = pd.join(data1, df3, on='PatientID', how='right')
df_outer = pd.merge(data1, df3, on='PatientID', how='outer')
