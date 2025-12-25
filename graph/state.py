from typing import Dict, List, Optional
from pydantic import BaseModel


class AgentState(BaseModel):
    product_data: Dict
    questions: List[str] = []
    faq: Optional[Dict] = None
    product_page: Optional[Dict] = None
    comparison_page: Optional[Dict] = None
