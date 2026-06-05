from app.mcp_tools.test_generator import (
    TestGeneratorTool
)


def test_case_generation():

    tool = TestGeneratorTool()


    result = tool.generate(
        [
            "Validate login"
        ]
    )


    assert "positive_tests" in result

    assert "negative_tests" in result

    assert "edge_cases" in result