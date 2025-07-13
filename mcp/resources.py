from pydantic import BaseModel, Field
from typing import List

class Resource(BaseModel):
    name: str = Field(..., description="The name of the resource.")
    description: str = Field(..., description="A description of the resource.")
    # Add other resource-related fields here as needed

def get_resources() -> List[Resource]:
    # In a real application, you would fetch these from a database or other source.
    return [
        Resource(name="market_news", description="Get the latest market news."),
        Resource(name="economic_calendar", description="Get the economic calendar."),
    ]
