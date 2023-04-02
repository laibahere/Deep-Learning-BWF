
import pandas as pd
#to read csv file
df = pd.read_csv('pokemon_data.csv')  #to read csv files

#print(df.head(4)) \\for top four rows
#print(df.tail(3)) \\ for bottom 3 rows

#to read excel file
df_xlsx= pd.read_excel('pokemon_data.xlsx')
#print(df_xlsx.head(3))

#to read txt file
df_txt=pd.read_csv('pokemon_data.txt')
print(df_txt.head(10))
