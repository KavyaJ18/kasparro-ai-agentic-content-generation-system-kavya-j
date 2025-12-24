class DataParserAgent:
    def parse(self, raw_data: dict) -> dict:
        return {
            "name": raw_data["Product Name"],
            "concentration": raw_data["Concentration"],
            "skin_type": raw_data["Skin Type"],
            "ingredients": raw_data["Key Ingredients"],
            "benefits": raw_data["Benefits"],
            "usage": raw_data["How to Use"],
            "side_effects": raw_data["Side Effects"],
            "price": raw_data["Price"]
        }
