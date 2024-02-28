import pandas as pd
from dotenv import load_dotenv
from pandasai import SmartDataframe
import os


load_dotenv()

df = pd.DataFrame({
    "country": [
        "United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
    "gdp": [
        19294482071552, 2891615567872, 2411255037952, 3435817336832, 1745433788416, 1181205135360, 1607402389504, 1490967855104, 4380756541440, 14631844184064
    ],
})

# Instantiate a LLM
from pandasai.llm import OpenAI
llm = OpenAI(api_token=os.getenv("OPENAI_API_KEY"))  # Get API token from https://platform.openai.com/account/api-keys

df = SmartDataframe(df, config={"llm": llm})
response = df.chat('Which are the countries with GDP greater than 3000000000000?')
print(response)