from typing import List
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import APIKeyHeader
from pydantic import BaseModel
from langchain_ibm import WatsonxLLM
from dotenv import load_dotenv
import json
import os

load_dotenv()
app = FastAPI(openapi_tags=[{
    "name": "pmo",
    "description": "pmo"
}])

# Initialize WatsonxLLM
watsonx_llm = WatsonxLLM(
    model_id = "mistralai/mixtral-8x7b-instruct-v01",
    project_id = os.environ["WATSONX_PROJECT_ID"],
    params = {
        "max_new_tokens": 1000
    }
)

class UserStory(BaseModel):
    title: str
    description: str

API_KEY = os.environ["API_KEY"]
api_key_header = APIKeyHeader(name="X-API-Key")

@app.get("/health", tags=["pmo"])
def health_check():
    return {"status": "ok"}

@app.post("/user-stories/generate", tags=["pmo"])
def generate_user_stories(query: str, api_key: str = Depends(api_key_header)) -> List[UserStory]:
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
    res = watsonx_llm.generate(["""
<s> [INST]
Generate as many user stories as needed to fulfill the given requirement, with an emphasis on improving user experience, access management, functionality, usability, and overall system performance, ensuring that all features are user-centric and aligned with business goals.
Each user story should have a concise title that summarizes the story and a detailed description with specific information.
Make sure the user stories are logically sequenced, break down the requirement into smaller tasks, and account for various user roles (e.g., Customer, Admin, Supplier).
The output should be in JSON format.

Here is an example for reference:
Input: Create user stories for an inventory management system.

Output:
[
    {
        "title": "Add New Item to Inventory",
        "description": "As a warehouse manager, I want to add new items to the inventory so that I can keep track of all the products available in the warehouse."
    },
    {
        "title": "Update Item Quantity",
        "description": "As a warehouse manager, I want to update the quantity of an item in the inventory so that I can reflect the current stock levels accurately."
    },
    {
        "title": "Search for Items",
        "description": "As a warehouse manager, I want to search for items in the inventory by name, SU, or category so that I can quickly find specific products."
    },
    {
        "title": "Generate Inventory Report",
        "description": "As a warehouse manager, I want to generate a report of the current inventory so that I can review the stock levels and make informed decisions."
    },
    {
        "title": "Track Low Stock Items",
        "description": "As a warehouse manager, I want to receive notifications for items that are low in stock so that I can reorder them in a timely manner."
    },
    {
        "title": "Delete Obsolete Items",
        "description": "As a warehouse manager, I want to delete obsolete items from the inventory so that the system only contains relevant and current products."
    },
    {
        "title": "View Item History",
        "description": "As a warehouse manager, I want to view the history of an item, including additions and removals, so that I can track its movement over time."
    },
    {
        "title": "Set Reorder Levels",
        "description": "As a warehouse manager, I want to set reorder levels for items so that the system can automatically notify me when stock falls below a certain threshold."
    },
    {
        "title": "Manage Suppliers",
        "description": "As a warehouse manager, I want to manage a list of suppliers so that I can easily contact them for reordering items."
    },
    {
        "title": "Export Inventory Data",
        "description": "As a warehouse manager, I want to export inventory data to a CSV or Excel file so that I can share it with other departments or use it for further analysis."
    }
]
End of example.

Use the format mentioned in example to create comprehensive and logically sequenced user stories for any given requirement.

Input: """ + query + """

[/INST]

Output:
                                 """])
    return json.loads(res.generations[0][0].text)

