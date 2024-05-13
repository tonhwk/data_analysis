import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# Load the dataset from a CSV file
df = pd.read_csv('marketing_campaign.csv', sep='\t', 
                   index_col='ID', 
                   parse_dates=['Dt_Customer'])

# Display the first few rows of the DataFrame
print(df.head(10))

# Check for missing values in each column
missing_values = df.isnull().sum()
print("Missing values in each column:")
print(missing_values)

df.info()
print(df['Z_Revenue'].value_counts())
print(df['Z_CostContact'].value_counts())

#Two columns that were never mentioned in the dataset
df.drop(columns=['Z_Revenue', 'Z_CostContact'], inplace=True)

#Handling duplicates
df[df.duplicated(keep=False)].sort_values(by='Income')
df[df.duplicated(keep='first')]
df.drop_duplicates(inplace=True)
df.info()

#Lets plot something :D
plt.figure(figsize=(24, 6))
plt.title('Customers yearly household income distribution')
ax = sns.displot(df.query('Income < 150000')['Income'], rug=True)

plt.show()

#Finding nulls
print(f'There are {df["Income"].isna().sum()} missing Income values')

#Transforming 2n Cycle and Graduation variables into a more specific and clear variables such as Master and Bachelor.
df['Education'].replace(['2n Cycle', 'Graduation'], 
                          ['Master', 'Bachelor'], inplace=True)

#Plotting corresponding proportions for education in the dataset
PALETTE = sns.color_palette("Set2")
sizes = dict(df['Education'].value_counts())

plt.figure(figsize=(12, 8))
plt.title("Education degrees proportion")
plt.pie(sizes.values(), labels=sizes.keys(), autopct="%.1f%%", pctdistance=0.85, shadow=True, colors=PALETTE)
plt.legend(title="Client's eduation", labels=sizes.keys(), bbox_to_anchor=(1, 1))

# add a circle at the center to transform it in a donut chart
my_circle=plt.Circle( (0,0), 0.7, color='white')
p=plt.gcf()
p.gca().add_artist(my_circle)

plt.show()






# Handle missing values appropriately (e.g., by imputation or removal)
# For example, if you want to fill missing values with the mean of the column:
# df.fillna(df.mean(), inplace=True)

# Or if you want to remove rows with missing values:
# df.dropna(inplace=True)

# You can choose the appropriate method based on your dataset and analysis goals
