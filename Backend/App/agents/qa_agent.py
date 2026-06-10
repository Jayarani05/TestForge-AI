from app.mcp_tools.requirement_analyzer import (
    RequirementAnalyzer
)

from app.orchestrator.multi_llm_orchestrator import (
    MultiLLMOrchestrator
)

from app.agents.judge_agent import (
    JudgeAgent
)

from app.mcp_tools.test_generator import (
    TestGeneratorTool
)

from app.mcp_tools.test_classifier import (
    TestClassifier
)

from app.agents.output_agent import (
    OutputAgent
)

from app.agents.project_context_agent import (
    ProjectContextAgent
)

from app.agents.test_data_agent import (
    TestDataAgent
)

from app.agents.requirement_agent import (
    analyze_requirement
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


        self.output_agent = (
            OutputAgent()
        )


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




        # ==================================
        # COMBINE REPO + USER STORY
        # ==================================


        enhanced_prompt = f"""

You are TestForge AI,
an Agentic QA Automation Engineer.


Your task:

Analyze the existing software repository
and generate accurate QA test cases.


====================================
PROJECT / REPOSITORY CONTEXT
====================================

{project_context}



====================================
USER STORY / REQUIREMENT
====================================

{story}



Generate test cases considering:

1. Existing code structure
2. Framework and technology stack
3. APIs and components
4. Database behaviour
5. Positive scenarios
6. Negative scenarios
7. Edge cases
8. Security validations


Return professional QA test cases.

"""





        # ==================================
        # REQUIREMENT INTELLIGENCE AGENT
        # ==================================


        requirement_intelligence = (

            analyze_requirement(

                enhanced_prompt

            )

        )






        # ==================================
        # MCP REQUIREMENT ANALYZER
        # ==================================


        requirement_analysis = (

            self.requirement_tool

            .analyze(

                enhanced_prompt

            )

        )








        # ==================================
        # MULTI LLM ORCHESTRATOR
        # Gemini + Llama + DeepSeek
        # ==================================


        llm_outputs = (

            self.llm_orchestrator

            .generate_all(

                enhanced_prompt

            )

        )








        # ==================================
        # JUDGE AGENT
        # ==================================


        judge_result = (

            self.judge

            .evaluate(

                llm_outputs

            )

        )








        # ==================================
        # TEST CLASSIFIER
        # ==================================


        classified_tests = (

            self.test_classifier

            .classify(

                judge_result[

                    "optimized_tests"

                ]

            )

        )








        # ==================================
        # PROJECT CONTEXT AGENT
        # ==================================


        context_result = (

            self.context_agent

            .process(

                project_context

            )

        )









        # ==================================
        # TEST DATA AGENT
        # ==================================


        test_data = (

            self.test_data_agent

            .generate(

                story,


                classified_tests

            )

        )









        # ==================================
        # OUTPUT FORMATTER AGENT
        # ==================================


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

                final_output,



            "test_data":

                test_data



        }