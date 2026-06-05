from app.agents.qa_agent import QAAgent


def test_qa_agent_workflow():

    agent = QAAgent()


    result = agent.process_story(
        "As a user I want login"
    )


    assert "judge_result" in result

    assert "optimized_tests" in result["judge_result"]
    