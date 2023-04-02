
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

#-------------READING DATA IN PANDAS ---------
#read headers
print(df.columns)
## read an specific columns
print(df['Name'][0:5])  ##top five names
print(df[['Name','HP']]) ##3 different columns
#read each row
print(df.head(4))
print(df.iloc[1]) #for specific row 
# for index,row in df.iterrows():
     #print(index,rows['Name'])
df.loc[df['Attack']== '50']     

print(df.iloc[2:1]) #read a specific location

#---------Sort/Describe Data---------
xxx= df.describe()
print(xxx)
xo= df.sort_values(['Name','Generation'],ascending=False)
print(xo)
