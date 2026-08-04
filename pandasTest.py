# Notes
    # Pandas is a Python library.
    # Pandas is used to analyze data
    # Pandas is a Python library used for working with data sets.
    # It has functions for analyzing, cleaning, exploring, and manipulating data.

# What is a Series?
# A Pandas Series is like a column in a table.
# It is a one-dimensional array holding data of any type.

# DataFrames
# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
# Series is like a column, a DataFrame is the whole table.
# A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

# Read CSV Files
# A simple way to store big data sets is to use CSV files (comma separated files).
# CSV files contains plain text and is a well know format that can be read by everyone including Pandas.
# In our examples we will be using a CSV file called 'data.csv'.

# Read JSON
# Big data sets are often stored, or extracted as JSON.
# JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.
# In our examples we will be using a JSON file called 'data.json'.


# Viewing the Data
# One of the most used method for getting a quick overview of the DataFrame, is the head() method.
# The head() method returns the headers and a specified number of rows, starting from the top.












# -------------------------------------------------------------------
# Install pandas library -  pip install pandas
#Importing Pandas Libray - import pandas as pd


# import pandas as pd

# my_dataset_dict={'cars':["TATA", "MARUTI", "HONDA"], 'passing':[3,4,5]}

# df=pd.DataFrame(my_dataset_dict)

# print(df)
# print()

# Series======================

# a=[1,5,9]
# x=pd.Series(a)
# print(x)
# print(type(x))

# With the index argument, you can name your own labels.

# a=[1,5,9]
# x=pd.Series(a, index=["x", "y", "z"])
# print(x)

# print(x["y"])   #indexed value

# # You can also use a key/value object, like a dictionary, when creating a Series.
# calories = {"day1": 420, "day2": 380, "day3": 390}
# # Note: The keys of the dictionary become the labels.

# s1=pd.Series(calories)
# print(s1)

# print()
# # To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Series.
# s2=pd.Series(calories, index=["day2", "day3"])

# print(s2)


# DataFrames=============================
# A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# df1=pd.DataFrame(data)
# print(df1)

# Pandas use the loc attribute to return one or more specified row(s)
# print(df1.loc[0])

# print(df1.loc[[0,1]])
# print()
# print(df1.loc[[1]])
# print()
# print(df1.loc[[1,2]])
# print()

# # With the index argument, you can name your own indexes.
# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# df1=pd.DataFrame(data, index=["x","y","z"])
# print(df1)
# print(df1.loc["x"])

# print(df1.loc[["y", "z"]])

# Load Files Into a DataFrame
# df=pd.read_csv("E:\Programming Code\Ptyhon Course\pythonapp\data.csv")

# use to_string() to print the entire DataFrame.
# print(df.to_string())

# You can check your system's maximum rows with the pd.options.display.max_rows statement.
# print(df)
# print(pd.options.display.max_rows)
# n my system the number is 60, which means that if the DataFrame contains more than 60 rows, the print(df) statement will return only the headers and the first and last 5 rows.

# You can change the maximum rows number with the same statement.
# pd.options.display.max_rows=100
# print(pd.options.display.max_rows)
# print(df)
# print()
# print(df.to_string())

# Read JSON===========================
import pandas as pd

# df =pd.read_json("https://www.w3schools.com/python/pandas/data.js")

# df=pd.read_json("E:\Programming Code\Ptyhon Course\pythonapp\data.js")
# print(df.to_string())

# JSON = Python Dictionary
# JSON objects have the same format as Python dictionaries.

# data = {
#   "Duration":{
#     "0":60,
#     "1":60,
#     "2":60,
#     "3":45,
#     "4":45,
#     "5":60
#   },
#   "Pulse":{
#     "0":110,
#     "1":117,
#     "2":103,
#     "3":109,
#     "4":117,
#     "5":102
#   },
#   "Maxpulse":{
#     "0":130,
#     "1":145,
#     "2":135,
#     "3":175,
#     "4":148,
#     "5":127
#   },
#   "Calories":{
#     "0":409,
#     "1":479,
#     "2":340,
#     "3":282,
#     "4":406,
#     "5":300
#   }
# }

# df=pd.DataFrame(data)
# print(df)

# Viewing the Data ======================

# import pandas as pd

# df =pd.read_csv("E:\Programming Code\Ptyhon Course\pythonapp\data.csv")

# print(df.head(10))  #Get a quick overview by printing the first 10 rows of the DataFrame:
# # Note: if the number of rows is not specified, the head() method will return the top 5 rows.

# # There is also a tail() method for viewing the last rows of the DataFrame.
# # The tail() method returns the headers and a specified number of rows, starting from the bottom.

# print(df.tail())    #Print the last 5 rows of the DataFrame:


# # Info About the Data
# # The DataFrames object has a method called info(), that gives you more information about the data set.
# # The info() method also tells us how many Non-Null values there are present in each column, and in our data set it seems like there are 164 of 169 Non-Null values in the "Calories" column.
# # Which means that there are 5 rows with no value at all, in the "Calories" column, for whatever reason.
# # Empty values, or Null values, can be bad when analyzing data, and you should consider removing rows with empty values. This is a step towards what is called cleaning data, and you will learn more about that in the next chapters.

# print(df.info())  #Print information about the data:


# Data Cleaning ===================================
# Data cleaning means fixing bad data in your data set.

# Bad data could be:
    # Empty cells
    # Data in wrong format
    # Wrong data
    # Duplicates


#       Duration          Date  Pulse  Maxpulse  Calories
#   0         60  '2020/12/01'    110       130     409.1
#   1         60  '2020/12/02'    117       145     479.0
#   2         60  '2020/12/03'    103       135     340.0
#   3         45  '2020/12/04'    109       175     282.4
#   4         45  '2020/12/05'    117       148     406.0
#   5         60  '2020/12/06'    102       127     300.0
#   6         60  '2020/12/07'    110       136     374.0
#   7        450  '2020/12/08'    104       134     253.3
#   8         30  '2020/12/09'    109       133     195.1
#   9         60  '2020/12/10'     98       124     269.0
#   10        60  '2020/12/11'    103       147     329.3
#   11        60  '2020/12/12'    100       120     250.7
#   12        60  '2020/12/12'    100       120     250.7
#   13        60  '2020/12/13'    106       128     345.3
#   14        60  '2020/12/14'    104       132     379.3
#   15        60  '2020/12/15'     98       123     275.0
#   16        60  '2020/12/16'     98       120     215.2
#   17        60  '2020/12/17'    100       120     300.0
#   18        45  '2020/12/18'     90       112       NaN
#   19        60  '2020/12/19'    103       123     323.0
#   20        45  '2020/12/20'     97       125     243.0
#   21        60  '2020/12/21'    108       131     364.2
#   22        45           NaN    100       119     282.0
#   23        60  '2020/12/23'    130       101     300.0
#   24        45  '2020/12/24'    105       132     246.0
#   25        60  '2020/12/25'    102       126     334.5
#   26        60    2020/12/26    100       120     250.0
#   27        60  '2020/12/27'     92       118     241.0
#   28        60  '2020/12/28'    103       132       NaN
#   29        60  '2020/12/29'    100       132     280.0
#   30        60  '2020/12/30'    102       129     380.3
#   31        60  '2020/12/31'     92       115     243.0

# The data set contains some empty cells ("Date" in row 22, and "Calories" in row 18 and 28).

# The data set contains wrong format ("Date" in row 26).

# The data set contains wrong data ("Duration" in row 7).

# The data set contains duplicates (row 11 and 12).


# Empty Cells
# Empty cells can potentially give you a wrong result when you analyze data.

# Remove Rows -dropna()
# One way to deal with empty cells is to remove rows that contain empty cells.
# This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.
# Note: By default, the dropna() method returns a new DataFrame, and will not change the original.
# Return a new Data Frame with no empty cells:

# import pandas as pd

# df =pd.read_csv("E:\Programming Code\Ptyhon Course\pythonapp\data.csv")

# print(df)
# print()
# new_df=df.dropna()
# print(new_df)

# If you want to change the original DataFrame, use the inplace = True argument:
# Remove all rows with NULL values:

# new_df=df.dropna(inplace=True)
# print(new_df) #--> none

# print()
# print(df)

# Note: Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.


# Replace Empty Values -fillna()
# Another way of dealing with empty cells is to insert a new value instead.

# This way you do not have to delete entire rows just because of some empty cells.

# The fillna() method allows us to replace empty cells with a value:

# df.fillna(-1, inplace=True)  #Replace NULL values with the number 130:
# print(df.to_string())

# Replace Only For Specified Columns
# The example above replaces all empty cells in the whole Data Frame.

# To only replace empty values for one column, specify the column name for the DataFrame:


# df.fillna({"Calories": -1}, inplace=True)
# print(df.to_string())


# Replace Using Mean, Median, or Mode
# A common way to replace empty cells, is to calculate the mean, median or mode value of the column.

# Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:

# Calculate the MEAN, and replace any empty values with it: 
# Mean = the average value (the sum of all values divided by number of values).
# Median = the value in the middle, after you have sorted all values ascending.
# Mode = the value that appears most frequently.

# x=df["Calories"].mean()
# df.fillna({"Calories": x}, inplace=True)
# print(x)
# print()
# print(df.to_string())
# print()
# x=df["Calories"].median()
# df.fillna({"Calories": x}, inplace=True)
# print(x)
# print()
# print(df.to_string())
# print()
# x=df["Calories"].mode()
# df.fillna({"Calories": x}, inplace=True)
# print(x)
# print()
# print(df.to_string())
# print()


































