# Assignment 1: Asking Questions with CSV Data

## Why I Chose This Dataset

I chose the NYC Popular Baby Names dataset because names are familiar and easy to understand, while the data still supports useful comparisons across years, gender categories, and ethnicity categories. I was also interested in seeing how the same name can appear with different frequencies across groups. The dataset is large enough to reveal patterns without being difficult to work with in pandas.

## Dataset

- Source: [NYC Open Data - Popular Baby Names](https://data.cityofnewyork.us/Health/Popular-Baby-Names/25th-nujf/data)
- Downloaded: September 13, 2026
- Rows: 29,685
- Columns: 6
- Columns: `Year of Birth`, `Gender`, `Ethnicity`, `Child's First Name`, `Count`, and `Rank`

Each row represents the ranking and count for a baby name within a particular year, gender category, and ethnicity category. A row is not one individual baby, so the questions below sum the `Count` column rather than simply counting rows.

## Three Data Questions

### 1. How many babies represented in this dataset were named Olivia?

```python
olivia_total = df.loc[
    df["Child's First Name"].str.upper() == "OLIVIA", "Count"
].sum()
print(olivia_total)
```

Output:

```text
7164
```

The table has a column for the child's first name and a numeric `Count` column. Filtering all rows whose name is Olivia and summing their counts gives the number of babies represented by those rows. Converting names to uppercase first makes the comparison work even though capitalization varies in the CSV.

### 2. How many female and male babies are represented in the dataset?

```python
gender_totals = df.groupby("Gender")["Count"].sum()
print(gender_totals)
```

Output:

```text
Gender
FEMALE    435077
MALE      555298
Name: Count, dtype: int64
```

The categorical `Gender` column can divide the rows into groups. Summing the numeric `Count` column within each group produces a total for each gender category in the published dataset.

### 3. Among babies named Jordan, how many were female and how many were male?

```python
jordan_gender_totals = (
    df.loc[df["Child's First Name"].str.upper() == "JORDAN"]
    .groupby("Gender")["Count"]
    .sum()
)
print(jordan_gender_totals)
```

Output:

```text
Gender
FEMALE     123
MALE      2079
Name: Count, dtype: int64
```

The data structure supports this question because the rows can first be filtered using the name column and then divided using the gender column. The numeric `Count` field can then be summed for each gender within that filtered subset.

## What the Data Cannot Answer

I would like to know why some names became more or less popular, but this dataset cannot answer that question. It records years, names, gender categories, ethnicity categories, counts, and ranks, but it does not record parents' reasons for choosing names or influences such as family traditions, religion, celebrities, fictional characters, or current events. It would therefore be misleading to assume that a change in a name's count was caused by any one cultural event merely because the dates appear to line up; the dataset can show a pattern over time, but it cannot establish the cause of that pattern.
