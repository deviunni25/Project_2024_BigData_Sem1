#importing the neccessary library for data cleaning
import pandas as pd

# reading the csv file into pandas dataframe
df=pd.read_csv("C:/Users/email/Downloads/car_prices.csv")

# Remove rows where age is greater than or equal to 35
df = df.head(250000)
df = df[df['year'] > 2007]

# Checking for null values 
print(df.isna().sum())

# Fill missing values with 'NA' category
df['make'] = df['make'].fillna('NA')
df['model'] = df['model'].fillna('NA')
df['trim'] = df['trim'].fillna('NA')
df['color'] = df['color'].fillna('NA')
df['interior'] = df['interior'].fillna('NA')

# Fill missing values with mode --- most frequently appearing value
df['body'] = df['body'].fillna(df['body'].mode()[0])
df['transmission'] = df['transmission'].fillna(df['transmission'].mode()[0])
df['condition'] = df['condition'].fillna(df['condition'].mode()[0])
df['sellingprice'] = df['sellingprice'].fillna(df['sellingprice'].mode()[0])
df['odometer'] = df['odometer'].fillna(df['odometer'].mode()[0])
df['mmr'] = df['mmr'].fillna(df['mmr'].mode()[0])

# Remove null values
df.dropna(subset = ['vin'], inplace=True)
df.dropna(subset = ['saledate'],inplace=True)
          
# Replace special characters in the 'interior' column with mode value
df['interior'] = df['interior'].str.replace('â€”', str(df['condition'].mode()[0]))


# Rename column 'condition' to 'rating'
df.rename(columns={'condition': 'rating'}, inplace=True)

# Display the DataFrame to verify the changes
print(df.isna().sum())


# Saving the result back to a csv file
df.to_csv("D:/PROJECTS/NOSQL/PandasOutputAfterDataCleaning/car_prices_cleaned.csv",index=False)