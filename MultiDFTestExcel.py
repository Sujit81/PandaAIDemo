from pandasai import SmartDatalake
import pandas as pd
from pandasai.llm import OpenAI
import pandas as pd
from dotenv import load_dotenv
from pandasai import SmartDataframe
import os


load_dotenv()

df1 = pd.read_excel(r"resources\Data1.xlsx", sheet_name="Sheet1")
df2 = pd.read_excel(r"resources\Data3.xlsx", sheet_name="Sheet1")
#df3 = pd.read_excel(r"resources\Data3.xlsx", sheet_name="Sheet1")
#employees_df = pd.DataFrame(employees_data)
#salaries_df = pd.DataFrame(salaries_data)


llm = OpenAI(api_token=os.getenv("OPENAI_API_KEY"))  # Get API token from https://platform.openai.com/account/api-keys

df = SmartDatalake([df2], config={"llm": llm})
#response = df.chat("Please let me EmployeeID and EmployeeIDWithName which is not present in one of the data frames?")
#response = df.chat("EmployeeID and EmployeeIDWithName values which is not present in one of the data frames and their percentage match? ")
#response = df.chat("Please compare EmployeeID in first dataframe with all columns in second dataframe and show me percentage match for each column? ")

#response = df.chat("Please compare each column in first dataframe with all columns in second dataframe and show me percentage match for each column? Show in tabular format ")

# response = df.chat("Please compare each column in df1 dataframe with all columns in df2 dataframe and show me percentage match for each column? Show in tabular format ")
#
# #response = df.chat("Please compare each column in first dataframe with all columns in dataframes and show me percentage match for each column? Show in tabular format with columns of dataframes in order completely ")
# print(response)
# print("\n\n")

#response = df.chat("Location column values matching Pune and Wakad")

response = df.chat("Please compare each column in first dataframe with all columns in dataframes and show me percentage match for each column? Show in tabular format with columns of dataframes in order completely ")
print(response)

#Output -
#  Column1     Column2  Match Percentage
# 0   EmployeeID  EmployeeID        100.000000
# 1   EmployeeID     Salary2          0.000000
# 2   EmployeeID     Village          0.000000
# 3   EmployeeID    Location          0.000000
# 4      Salary2  EmployeeID          0.000000
# 5      Salary2     Salary2        100.000000
# 6      Salary2     Village          0.000000
# 7      Salary2    Location          0.000000
# 8      Village  EmployeeID          0.000000
# 9      Village     Salary2          0.000000
# 10     Village     Village        100.000000
# 11     Village    Location         16.666667
# 12    Location  EmployeeID          0.000000
# 13    Location     Salary2          0.000000
# 14    Location     Village         16.666667
# 15    Location    Location        100.000000
