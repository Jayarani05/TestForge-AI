from app.mcp_tools.requirement_analyzer import RequirementAnalyzer


from app.orchestrator.multi_llm_orchestrator import (
    MultiLLMOrchestrator
)


from app.agents.judge_agent import JudgeAgent


from app.mcp_tools.test_generator import (
    TestGeneratorTool
)


from app.mcp_tools.test_classifier import (
    TestClassifier
)

from app.agents.output_agent import OutputAgent

from app.agents.project_context_agent import (
    ProjectContextAgent
)



class QAAgent:



    def __init__(self):


        self.requirement_tool = (
            RequirementAnalyzer()
        )


        self.llm_orchestrator = (
            MultiLLMOrchestrator()
        )


        self.judge = (
            JudgeAgent()
        )


        self.test_generator = (
            TestGeneratorTool()
        )


        self.test_classifier = (
            TestClassifier()
        )

        self.output_agent = OutputAgent()

        self.context_agent = (
            ProjectContextAgent()
)




    def process_story(
         self,
         story,
         output_type="test_cases",
         language=None,
         framework=None,
         project_context=None


    ):


        # Step 1:
        # Analyze requirement

        analysis = (

            self.requirement_tool
            .analyze(
                story
            )

        )



        # Step 2:
        # Generate using Gemini + Llama + DeepSeek

        llm_outputs = (

            self.llm_orchestrator
            .generate_all(
                story
            )

        )



        # Step 3:
        # Judge best LLM response

        judge_result = (

            self.judge
            .evaluate(
                llm_outputs
            )

        )



        # Step 4:
        # Classify optimized tests

        classified_tests = (

            self.test_classifier
            .classify(

                judge_result[
                    "optimized_tests"
                ]

            )

        )

        context_result = (

            self.context_agent
            .process(

                project_context
            )

        )

        final_output = (

            self.output_agent
            .generate(
                output_type,
                classified_tests,
                language,
                framework,
                context_result



            )

        )



        return {


            "requirement_analysis":
            analysis,



            "llm_outputs":
            llm_outputs,



            "judge_result":
            judge_result,



            "generated_test_cases":
            classified_tests,

            "final_output":
            final_output,

            "project_context":
            context_result,
        }