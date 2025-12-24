class ComparisonTemplateAgent:
    def assemble(self, comparison_data: dict) -> dict:
        return {
            "page_type": "comparison",
            "data": comparison_data
        }
