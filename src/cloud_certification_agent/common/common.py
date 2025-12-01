from google.adk.tools.tool_context import ToolContext


def save_to_state(key: str, value: str, tool_context: ToolContext):
    """Saves an intermediate value to session state.

    Args:
        key (str): the key for the intermediate value
        value (str): the intermediate value
        tool_context (ToolContext): the context tool
    """

    tool_context.state[key] = value
