# Notion: Sync Artist Fields

This project is a Python script that synchronizes a Select field called "Artist" with a derived Text field called "Artist (Grouping)" in a Notion gallery database. The script ensures that the "Artist (Grouping)" field is updated based on the value of the "Artist" field, allowing for proper Grouping and display in a gallery view.

> ⚠️ **Note:** This project is necessary only because Notion does not support Grouping alphabetically by a "Select"-type field. If you don't need to group your Notion database by a "Select"-type field, you can ignore this project.

## Usage

Before running the script, make sure you have Python 3.6 or later installed, along with the required libraries. You can install the dependencies using the following command:

bash
```
pip install -r requirements.txt
```

Next, create a .env file in the same directory as the script and add your Notion API key and the URL of your gallery database. Refer to the .env.template file for details.

Finally, you can run the script using the following command:
```
python sync_artist_fields.py
```

## Automating the script
This project uses Github Actions to periodically run the script - this keeps the derived group field up to date with changes to the source field. Instrutions for doing so are in the GitHub Actions workflow file (`sync_artist_fields.yml`). If you would want it to run on a different schedule, just modify the `cron` setting in the workflow file.

To set up the GitHub Action, follow the instructions provided in the main project discussion.

## Testing
Test coverage incomplete in test_sync_artist_fields.py; further mocking would likely be required to debug the 502 error. 
Consider creating a small test database in your own Notion ecosystem to ensure this works for your field names.