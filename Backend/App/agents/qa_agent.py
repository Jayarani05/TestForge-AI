from app.mcp_tools.requirement_analyzer import RequirementAnalyzer

from app.orchestrator.multi_llm_orchestrator import (
    MultiLLMOrchestrator
)

from app.agents.judge_agent import JudgeAgent



class QAAgent:


    def __init__(self):

        self.requirement_tool = RequirementAnalyzer()

        self.llm_orchestrator = (
            MultiLLMOrchestrator()
        )

        self.judge = JudgeAgent()



    def process_story(
        self,
        story
    ):


        analysis = (
            self.requirement_tool
            .analyze(story)
        )


        llm_outputs = (
            self.llm_orchestrator
            .generate_all(story)
        )


        final_result = (
            self.judge
            .evaluate(llm_outputs)
        )


        return {

            "requirement_analysis":
                analysis,


            "llm_outputs":
                llm_outputs,


            "judge_result":
                final_result
        }