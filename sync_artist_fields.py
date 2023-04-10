import os
from dotenv import load_dotenv
from notion_client import Client

load_dotenv()

# Get the API key and database URL from the .env file
notion_api_key = os.getenv("NOTION_API_KEY")
database_id = os.getenv("DATABASE_ID")

notion = Client(auth=notion_api_key)

def query_database_items(notion, database_id):
    results = []
    has_more = True
    start_cursor = None

    while has_more:
        result_set = notion.databases.query(
            database_id,
            page_size=100,
            start_cursor=start_cursor
        )
        results.extend(result_set["results"])
        start_cursor = result_set.get("next_cursor")
        has_more = start_cursor is not None

    return results


def get_group_field_value(item, initial_field_name):
    return item["properties"][initial_field_name]["select"]["name"]

def sync_fields(items, initial_field_name, derived_field_name):
    for item in items:
        group_field_value = get_group_field_value(item, initial_field_name)
        if not group_field_value:
            continue
        item_id = item["id"]
    # Update the value of the "derived_field_name" property for this item
        item_properties = {
            derived_field_name: {
                "rich_text": [{"type": "text", "text": {"content": group_field_value}}]
            }
        }
        # Update the derived field
        # notion.set_item_property(item["id"], derived_field_name, {"text": derived_field_value})
        notion.pages.update(page_id=item_id, properties=item_properties)

# Retrieve all items in the gallery database
items = query_database_items(notion, database_id)

# Set the initial field name and the derived field name
initial_field_name = "Artist"
derived_field_name = "Artist (Grouping)"


sync_fields(items, initial_field_name, derived_field_name)