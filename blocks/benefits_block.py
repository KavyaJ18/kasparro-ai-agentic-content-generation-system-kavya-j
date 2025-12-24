class BenefitsBlock:
    def build(self, benefits: list) -> list:
        return [{"benefit": b} for b in benefits]
