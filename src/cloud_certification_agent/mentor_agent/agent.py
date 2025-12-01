import os

from dotenv import load_dotenv
from pydantic import BaseModel, Field
from google.adk.agents.llm_agent import Agent
from cloud_certification_agent.common.load_prompts import load_agent_config


load_dotenv()


LLM_AGENT = os.getenv("LLM_AGENT")

if not LLM_AGENT:
    raise ValueError("The LLM_AGENT environment variable is not set.")


agent_config = load_agent_config("mentor")


class Subject(BaseModel):
    week: int = Field(description="Week")
    background: str = Field(description="Background required for the topic")
    topic: str = Field(description="Topic for this week")
    reading_pages: str = Field(description="The book and reading pages")
    links: str = Field(description="Links to the resources")
    replication_targets: str = Field(description="Replication target for this week")
    checkpoints: str = Field(description="Checkpoints that should be achieved")
    required_effort: str = Field(description="The amount of effort required")


class StudyPlan(BaseModel):
    subjects: list[Subject] = Field(description="Each week subject")


root_agent = Agent(
    name="mentor_agent",
    model=LLM_AGENT,
    description=agent_config["description"],
    instruction=agent_config["instruction"],
    tools=[],
    output_key="study_plan",
    output_schema=StudyPlan,
)
