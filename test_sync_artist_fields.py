import unittest
from unittest.mock import MagicMock
import sync_artist_fields as s

class TestSyncArtistFields(unittest.TestCase):

    def test_get_initial_field_value(self):
        item = {
            "properties": {
                "Artist": {
                    "select": {
                        "name": "John Doe"
                    }
                }
            }
        }
        initial_field_name = "Artist"
        self.assertEqual(s.get_group_field_value(item, initial_field_name), "John Doe")

    def test_update_derived_field_value(self):
        initial_field_name = "Artist"
        self.assertEqual(s.update_derived_field_value("John Doe", initial_field_name), "John Doe")
        self.assertEqual(s.update_derived_field_value(None, initial_field_name), "No Artist")

    def test_sync_fields(self):
        items = [
            {
                "id": "ea0f737af4af4327bb6353b5df9a4bbc",
                "properties": {
                    "Artist": {
                        "select": {
                            "name": "John Doe"
                        }
                    }
                }
            },
            {
                "id": "da0f737a74af4327bb6353b5cf9a4bbc",
                "properties": {
                    "Artist": {
                        "select": {
                            "name": None
                        }
                    }
                }
            }
        ]

        s.notion.set_item_property = MagicMock()

        initial_field_name = "Artist"
        derived_field_name = "Artist (Grouping)"
        s.sync_fields(items, initial_field_name, derived_field_name)

        s.notion.pages.update.assert_called_with(page_id="page_id_1", properties={
            "Artist (Grouping)": {
                "rich_text": [{"type": "text", "text": {"content": "John Doe"}}]
            }
        })
        s.notion.pages.update.assert_called_with(page_id="page_id_2", properties={
            "Artist (Grouping)": {
                "rich_text": [{"type": "text", "text": {"content": "No Artist"}}]
            }
        })

if __name__ == "__main__":
    unittest.main()
