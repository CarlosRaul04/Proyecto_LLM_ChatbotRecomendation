from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain.schema import SystemMessage
from app.workflow.agent_system_prompt import INSTRUCTION
from app.workflow.models import gpt_4o
from app.workflow.tools.db_tools import search_oscars_by_actor
from app.workflow.tools.movie_tools import MovieRecommendation, searchxTitle, apiMovieRecommendations, findMovies_NowPlaying, moviesTopRated 
from app.workflow.tools.tv_tools import apiTVShowsRecommendations, TvTopRated

agentTools = [
    MovieRecommendation,
    searchxTitle,
    apiMovieRecommendations,
    apiTVShowsRecommendations,
    findMovies_NowPlaying,
    moviesTopRated,
    TvTopRated,
    search_oscars_by_actor
]

memory = MemorySaver()
MovieAgent = create_react_agent(
    gpt_4o,
    tools=agentTools,
    state_modifier=SystemMessage(content=INSTRUCTION),
    checkpointer=memory
)

