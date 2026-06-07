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

from app.agents.test_data_agent import (
    TestDataAgent
)


from app.agents.requirement_agent import analyze_requirement


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

        self.test_data_agent = (
             TestDataAgent()
        )




    def process_story(
         self,
         story,
         output_type="test_cases",
         language=None,
         framework=None,
         project_context=None


    ):
        

        requirement_intelligence = analyze_requirement(
            user_story
        )


    # existing Gemini llama deepseek code continues here


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


        test_data = (
            self.test_data_agent.generate(
                 story,
                 classified_tests
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


    "requirement_intelligence":

        requirement_intelligence,


    "requirement_analysis":

        requirement_analysis,


    "llm_outputs":

        llm_outputs,


    "judge_result":

        judge_result,


    "generated_test_cases":

        generated_tests,


    "test_data":

        test_data


}