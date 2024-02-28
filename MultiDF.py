from pandasai import SmartDatalake
import pandas as pd
from pandasai.llm import OpenAI
import pandas as pd
from dotenv import load_dotenv
from pandasai import SmartDataframe
import os


load_dotenv()

employees_data = {
    'EmployeeID': [1, 2, 3, 4, 5],
    'Name': ['John', 'Emma', 'Liam', 'Olivia', 'William'],
    'Department': ['HR', 'Sales', 'IT', 'Marketing', 'Finance']
}

salaries_data = {
    'EmployeeID': [1, 2, 3, 4, 5],
    'Salary': [5000, 6000, 4500, 7000, 5500]
}

employees_df = pd.DataFrame(employees_data)
salaries_df = pd.DataFrame(salaries_data)

llm = OpenAI(api_token=os.getenv("OPENAI_API_KEY"))  # Get API token from https://platform.openai.com/account/api-keys

df = SmartDatalake([employees_df, salaries_df], config={"llm": llm})
response = df.chat("Who gets paid the most?")
print(response)