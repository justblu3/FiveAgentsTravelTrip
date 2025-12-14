from core import Agent

activity_agent = Agent(
    name="Activity Planner",
    system_instruction="""
    You are an Activity Planner. 
    You will receive a trip summary.
    Suggest 3 specific things to see or do in that location.
    Mention if they are free or if they have an entry fee.
    """
)