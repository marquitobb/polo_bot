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

page_tags = {
    "Name": {
        "title":[
            {
                "text": {
                    "content":'zzzz zzzz',
                }
            }
        ]
    },
    "Cost":{
        "rich_text":[
            {
                "text": {
                    "content":'201',
                }
            }
        ]
    }
}


pages = notion.pages.create(parent=parent, properties=page_tags)
print(pages)
