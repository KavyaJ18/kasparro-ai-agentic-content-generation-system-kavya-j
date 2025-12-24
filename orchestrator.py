from agents.data_parser_agent import DataParserAgent
from agents.question_agent import QuestionGeneratorAgent
from agents.comparison_agent import ComparisonAgent

from templates.faq_template import FAQTemplateAgent
from templates.product_template import ProductPageTemplateAgent
from templates.comparison_template import ComparisonTemplateAgent


class Orchestrator:
    def run(self, raw_product_data: dict) -> dict:
        # 1. Parse input data
        parsed_product = DataParserAgent().parse(raw_product_data)

        # 2. Generate questions
        questions = QuestionGeneratorAgent().generate(parsed_product)

        # 3. Build pages
        faq_page = FAQTemplateAgent().assemble(questions, parsed_product)
        product_page = ProductPageTemplateAgent().assemble(parsed_product)

        comparison_data = ComparisonAgent().build_comparison(parsed_product)
        comparison_page = ComparisonTemplateAgent().assemble(comparison_data)

        return {
            "faq": faq_page,
            "product_page": product_page,
            "comparison_page": comparison_page
        }
