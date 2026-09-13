import pandas as pd


CSV_FILE = "popular_baby_names.csv"


# Load the CSV file into a pandas DataFrame.
df = pd.read_csv(CSV_FILE)


# Required inspection tasks
print("\n1. First 2 rows")
print(df.head(2))

print("\n2. First row")
print(df.iloc[0])

print("\n3. Rows 10-19")
print(df.iloc[10:20])

print("\n4. Column names")
print(df.columns.tolist())

print("\n5. First 10 values from the Gender column")
print(df["Gender"].head(10))

print("\n6. First 10 rows from three columns")
print(df[["Year of Birth", "Gender", "Child's First Name"]].head(10))


# Question 1: How many babies represented in this dataset were named Olivia?
olivia_total = df.loc[
    df["Child's First Name"].str.upper() == "OLIVIA", "Count"
].sum()
print("\nQuestion 1 - Babies named Olivia:", olivia_total)


# Question 2: How many female and male babies are represented in the dataset?
gender_totals = df.groupby("Gender")["Count"].sum()
print("\nQuestion 2 - Babies by gender")
print(gender_totals)


# Question 3: Among babies named Jordan, how many were female and how many were male?
jordan_gender_totals = (
    df.loc[df["Child's First Name"].str.upper() == "JORDAN"]
    .groupby("Gender")["Count"]
    .sum()
)
print("\nQuestion 3 - Babies named Jordan by gender")
print(jordan_gender_totals)
