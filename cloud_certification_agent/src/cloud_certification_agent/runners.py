from google.genai import types
from google.adk.sessions.sqlite_session_service import SqliteSessionService
from google.adk.runners import Runner

APP_NAME = "cloud_certification_agent"


async def get_runner(root_agent, user_id, session_id):
    db_url = "sqlite:///./my_agent_data.db"
    session_service = SqliteSessionService(db_path=db_url)

    await session_service.create_session(
        app_name=APP_NAME, user_id=user_id, session_id=session_id
    )

    runner = Runner(
        agent=root_agent, app_name=APP_NAME, session_service=session_service
    )

    return runner


async def call_agent_async(query: str, runner, user_id, session_id):
    content = types.Content(role="user", parts=[types.Part(text=query)])

    agent_event_generator = runner.run_async(
        user_id=user_id, session_id=session_id, new_message=content
    )

    final_response_text = "Agent did not produce a final response."

    async for event in agent_event_generator:
        if event.is_final_response():
            if event.content and event.content.parts:
                final_response_text = event.content.parts[0].text
            elif event.actions and event.actions.escalate:
                final_response_text = (
                    f"Agent escalated: {event.error_message or 'No specific message.'}"
                )
            break

    return final_response_text
