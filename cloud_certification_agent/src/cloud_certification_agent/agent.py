import os

from dotenv import load_dotenv
from cloud_certification_agent.common.common import save_to_state
from cloud_certification_agent.mentor_agent import mentor_agent
from cloud_certification_agent.simulator_exam_agent import simulator_exam_agent
from google.adk.tools.function_tool import FunctionTool
from google.adk.tools.agent_tool import AgentTool
from google.adk.agents.llm_agent import Agent

from cloud_certification_agent.common.load_prompts import load_agent_config


load_dotenv()


LLM_AGENT = os.getenv("LLM_AGENT")

if not LLM_AGENT:
    raise ValueError("The LLM_AGENT environment variable is not set.")


agent_config = load_agent_config("orquestrator")


root_agent = Agent(
    name="orquestrator_agent",
    model=LLM_AGENT,
    description=agent_config["description"],
    instruction=agent_config["instruction"],
    tools=[
        AgentTool(mentor_agent),
        AgentTool(simulator_exam_agent),
        FunctionTool(save_to_state),
    ],
)
