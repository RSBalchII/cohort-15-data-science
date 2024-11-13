# Select categorical columns from the housing dataset

categorical_cols = housing_df.select_dtypes(include='object')

# Get value counts for the Neighborhood column

categorical_cols['Neighborhood'].value_counts()

# Transpose the categorical columns dataframe

categorical_cols.transpose()

# Print percentage distribution for each categorical column

for col in categorical_cols:
print(f"Value counts for {col}:")
total = len(housing_df)
print(categorical_cols[col].value_counts(dropna=False) / total \* 100)
print("\n")

# Define pairs of columns for joint probability calculation

pairs = ['Street', 'Heating']

# Calculate joint probability for the defined pairs

categorical_cols[pairs].value_counts() / categorical_cols[pairs].value_counts().sum() \* 100

# Define individual columns for conditional probability calculation

A = 'Street'
B = 'Heating'

# Recalculate joint probability using A and B

categorical_cols[[A, B]].value_counts() / categorical_cols[[A, B]].value_counts().sum() \* 100

# Calculate conditional probability of A given B

categorical_cols[[A, B]].value_counts() / (2585 + 12)

# Calculate conditional probability of A given B when B is 'GasA'

categorical_cols[[A, B]].value_counts() / (categorical_cols[B] == 'GasA').sum()

# Get value counts for A and B separately

categorical_cols[[A, B]].value_counts(), categorical_cols[B].value_counts()

# Reset index for both value counts

(categorical_cols[[A, B]].value_counts()).reset_index(), categorical_cols[B].value_counts().reset_index()

# Merge the two dataframes on column B

merged_df = pd.merge(
(categorical_cols[[A, B]].value_counts()).reset_index(),
categorical_cols[B].value_counts().reset_index(),
on=B
)

# Calculate marginal probability

merged_df['marg_prob'] = merged_df['count_x'] / merged_df['count_y'] \* 100

# Redefine A and B for Alley and Street columns

B = ['Street']
A = ['Alley']

# Merge dataframes for Alley and Street columns

merged_df = pd.merge(
categorical_cols[A + B].value_counts(dropna=True).reset_index(),
categorical_cols[B].value_counts(dropna=True).reset_index(),
on=B
)

# Calculate marginal probability for Alley and Street

merged_df['marg_prob'] = merged_df['count_x'] / merged_df['count_y'] \* 100

# Display first few rows of categorical columns

categorical_cols.head()

# Define columns for multi-column analysis

B = ['Street', 'Utilities']
A = ['Alley']
A = A + B

# Count values for A and B

counts_A = categorical_cols[A].value_counts(dropna=False).reset_index()
counts_B = categorical_cols[B].value_counts(dropna=False).reset_index()

# Merge counts for A and B

merged_df = pd.merge(
counts_A,
counts_B,
on=B,
suffixes=('\_A', '\_B')
)

# Calculate marginal probabilities

merged_df['marg_prob'] = merged_df['count_A'] / merged_df['count_B'] \* 100

# Add a new column indicating presence of Alley

categorical_cols['Has_Alley'] = categorical_cols['Alley'].notna()

# Redefine columns for final analysis

A = ['Alley']
B = ['Street', 'Utilities', 'Has_Alley']

# Count values for A and B including Has_Alley

counts_A = categorical_cols[A + B].value_counts(dropna=False).reset_index()
counts_B = categorical_cols[B].value_counts(dropna=False).reset_index()

# Merge counts for A and B including Has_Alley

merged_df = pd.merge(
counts_A,
counts_B,
on=B,
suffixes=('\_A', '\_B')
)

# Calculate marginal probabilities including Has_Alley

merged_df['marg_prob'] = merged_df['count_A'] / merged_df['count_B'] \* 100

## Exploratory Data Analysis
