from app.agents.requirement_agent import analyze_requirement


story = """

As a customer,
I want to reset my password,
so that I can access my account again.

"""


result = analyze_requirement(
    story
)


print(result)