from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

gpt_4o = ChatOpenAI(model="gpt-4o", temperature=0)
gpt_4o_mini = ChatOpenAI(model="gpt-4o-mini", temperature=0)