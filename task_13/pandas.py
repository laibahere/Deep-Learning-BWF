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
