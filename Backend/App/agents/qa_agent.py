from app.mcp_tools.requirement_analyzer import (
    RequirementAnalyzer
)


class QAAgent:


    def __init__(self):

        self.requirement_tool = (
            RequirementAnalyzer()
        )


    def process_story(
        self,
        story: str
    ):

        requirement_analysis = (
            self.requirement_tool
            .analyze(story)
        )


        return {

            "agent": "QA Agent",

            "workflow": [
                "Requirement Analysis"
            ],

            "analysis":
                requirement_analysis
        }