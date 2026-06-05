class RequirementAnalyzer:


    def analyze(self, user_story: str):

        analysis = {
            "actor": self.extract_actor(
                user_story
            ),

            "requirement": user_story,

            "test_focus": [
                "functional testing",
                "negative testing",
                "edge case testing"
            ],

            "status": "analyzed"
        }

        return analysis


    def extract_actor(
        self,
        story
    ):

        if "As a" in story:

            return (
                story
                .split("As a")[1]
                .split("I want")[0]
                .strip()
            )

        return "Unknown"