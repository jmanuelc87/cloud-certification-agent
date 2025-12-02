import os

from dotenv import load_dotenv
from google.adk.agents.llm_agent import Agent
from cloud_certification_agent.common.load_prompts import load_agent_config


load_dotenv()


LLM_AGENT = os.getenv("LLM_AGENT")

if not LLM_AGENT:
    raise ValueError("The LLM_AGENT environment variable is not set.")


agent_config = load_agent_config("simulator_exam")


root_agent = Agent(
    name="simulator_exam_agent",
    model=LLM_AGENT,
    description=agent_config["description"],
    instruction=agent_config["instruction"],
    tools=[],
)
