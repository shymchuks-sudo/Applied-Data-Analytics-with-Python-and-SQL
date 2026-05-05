import pandas as pd
data = {'name': ['john', 'jane', 'doe'],\
        'age': [25, 28, 22],\
            'occupation': ['engenieer', 'doctor', 'artist']}

df = pd.DataFrame(data)
print(df)
#    name  age occupation
# 0  john   25  engenieer
# 1  jane   28     doctor
# 2   doe   22     artist
print(df.head())
# first 5 rows
print(df.tail())
# last 5 rows
print(df.shape)
# (3, 3)
print(df.columns)
# Index(['name', 'age', 'occupation'], dtype='str')
print(df.isnull())
#     name    age  occupation
# 0  False  False       False
# 1  False  False       False
# 2  False  False       False
print(df.describe())
#         age
# count   3.0
# mean   25.0
# std     3.0
# min    22.0
# 25%    23.5
# 50%    25.0
# 75%    26.5
# max    28.0
print(df.any()) # returns true if any value if true
# name          True
# age           True
# occupation    True
# dtype: bool
print(df.all()) #returnes true if all values are true
# name          True
# age           True
# occupation    True
# dtype: bool

data2 = {
    'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
    'last_name': ['Miller', 'Jacobson', '.', 'Milner', 'Cooze'],
    'age': [42, 52, 36, 24, 73],
    'preTestScore': [4,24,31,'.','.'],
    'postTestScore': ['25,000', '94,000', 57, 62, 70]
}

df2 = pd.DataFrame(data2)
print(df2)
#   first_name last_name  age preTestScore postTestScore
# 0      Jason    Miller   42            4        25,000
# 1      Molly  Jacobson   52           24        94,000
# 2       Tina         .   36           31            57
# 3       Jake    Milner   24            .            62
# 4        Amy     Cooze   73            .            70

df2.to_csv('example.csv', index=False)
df_read = pd.read_csv('example.csv')
print(df_read)
#   first_name last_name  age preTestScore postTestScore
# 0      Jason    Miller   42            4        25,000
# 1      Molly  Jacobson   52           24        94,000
# 2       Tina         .   36           31            57
# 3       Jake    Milner   24            .            62
# 4        Amy     Cooze   73            .            70

df_no_header = pd.read_csv('example.csv', header=None)
print(df_no_header) # the first row is now part of the data, index 0
# 0  first_name  last_name  age  preTestScore  postTestScore
# 1       Jason     Miller   42             4         25,000
# 2       Molly   Jacobson   52            24         94,000
# 3        Tina          .   36            31             57
# 4        Jake     Milner   24             .             62
# 5         Amy      Cooze   73             .             70

df_custom_index = pd.read_csv('example.csv', index_col=['first_name', 'last_name'])
print(df_custom_index)
#                       age preTestScore postTestScore
# first_name last_name
# Jason      Miller      42            4        25,000
# Molly      Jacobson    52           24        94,000
# Tina       .           36           31            57
# Jake       Milner      24            .            62
# Amy        Cooze       73            .            70

df_first3rows = pd.read_csv('example.csv').head(3)
print(df_first3rows)
#   first_name last_name  age preTestScore postTestScore
# 0      Jason    Miller   42            4        25,000
# 1      Molly  Jacobson   52           24        94,000
# 2       Tina         .   36           31            57

df2['postTestScore'] = df2['postTestScore'].replace({',':''}, regex=True).astype(float)
print(df2)
#   first_name last_name  age preTestScore  postTestScore
# 0      Jason    Miller   42            4        25000.0
# 1      Molly  Jacobson   52           24        94000.0
# 2       Tina         .   36           31           57.0
# 3       Jake    Milner   24            .           62.0
# 4        Amy     Cooze   73            .           70.0
