from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain.schema import SystemMessage
from app.workflow.agent_system_prompt import INSTRUCTION
from app.workflow.agent_tools import tools
from app.workflow.models import gpt_4o

memory = MemorySaver()

MovieAgent = create_react_agent(
    gpt_4o,
    tools=tools,
    state_modifier=SystemMessage(content=INSTRUCTION),
    checkpointer=memory
)

