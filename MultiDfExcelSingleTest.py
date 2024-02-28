from pandasai import SmartDatalake
import pandas as pd
from pandasai.llm import OpenAI
import pandas as pd
from dotenv import load_dotenv
from pandasai import SmartDataframe
import os


load_dotenv()

df1 = pd.read_excel(r"resources\Data3.xlsx", sheet_name="Sheet1")


llm = OpenAI(api_token=os.getenv("OPENAI_API_KEY"))  # Get API token from https://platform.openai.com/account/api-keys

df = SmartDatalake([df1], config={"llm": llm})
#response = df.chat("Location column values matching Pune and Wakad")
#response = df.chat("Salary greater than 50000")
#response = df.chat("Village Column is Moshi and Wakad or Location column is Pune..show me in tabular format")
response = df.chat("Village Column is Moshi and Wakad and Location column is Pune..show me in tabular format")
print(response)