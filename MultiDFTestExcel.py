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

response = df.chat("Location column values matching Pune and Wakad")

#response = df.chat("Please compare each column in first dataframe with all columns in dataframes and show me percentage match for each column? Show in tabular format with columns of dataframes in order completely ")
print(response)