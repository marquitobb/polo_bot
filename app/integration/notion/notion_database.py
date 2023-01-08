import os
from notion_client import Client
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN_ID_NOTION")
page_id = os.getenv("PAGE_ID")

notion = Client(auth=token)
# children = notion.blocks.children.list(block_id=page_id)
# children = notion.blocks.children.parent()
# results = notion.search(query='')
# print(results)

parent = {
    "database_id": page_id
}

class NotionDatabase:
    @classmethod
    def save_costs(cls, name: str, cost: str):
        try:
            pages = notion.pages.create(parent=parent, properties=cls.create_schema(name, cost))
            return pages
        except Exception as e:
            print(e)
            return None


    @classmethod
    def create_schema(cls, name: str, cost: str) -> dict:
        try:
            page_tags = {
                "Name": {
                    "title":[
                        {
                            "text": {
                                "content": name,
                            }
                        }
                    ]
                },
                "Cost":{
                    "rich_text":[
                        {
                            "text": {
                                "content": cost,
                            }
                        }
                    ]
                }
            }
            return page_tags
        except Exception as e:
            print(e)
            return {
                "Name": {
                    "title":[
                        {
                            "text": {
                                "content": None,
                            }
                        }
                    ]
                },
                "Cost":{
                    "rich_text":[
                        {
                            "text": {
                                "content": None,
                            }
                        }
                    ]
                }
            }

