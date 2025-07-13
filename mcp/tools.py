from pydantic import BaseModel, Field
from typing import List

class Tool(BaseModel):
    name: str = Field(..., description="The name of the tool.")
    description: str = Field(..., description="A description of what the tool does.")
    # Add other tool-related fields here as needed

def get_tools() -> List[Tool]:
    # In a real application, you would fetch these from a database or other source.
    return [
        Tool(name="stock_screener", description="Screens for stocks based on various criteria."),
        Tool(name="company_profile", description="Gets the profile of a specific company."),
    ]
