from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain.schema import SystemMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

from app.workflow.agent_system_prompt import INSTRUCTION
from app.workflow.tools import tools

load_dotenv()
gpt_4o = ChatOpenAI(model="gpt-4o", temperature=0)
memory = MemorySaver()
MovieAgent = create_react_agent(
    gpt_4o,
    tools=tools,
    state_modifier=SystemMessage(content=INSTRUCTION),
    checkpointer=memory
)
