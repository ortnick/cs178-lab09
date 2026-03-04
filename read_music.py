# read_music.py
# Reads all items from the DynamoDB Songs table and prints them.
# Part of Lab 09 — feature/read-dynamo branch

import boto3
from boto3.dynamodb.conditions import Key

# -------------------------------------------------------
# Configuration — update REGION if your table is elsewhere
# -------------------------------------------------------
REGION = "us-east-1"
TABLE_NAME = "Songs"


def get_table():
    """Return a reference to the DynamoDB songs table."""
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)


def print_song(song):
    song = song.get("Song", "Unknown Song")
    artist = song.get("Artist", "Unknown Artist")
    genre = song.get("Genre", "Unknown Genre")
    print(f"  Song  : {song}")
    print(f"  Artist   : {artist}")
    print(f"  Genre: {genre}")
    print()


def print_all_songs():
    """Scan the entire songs table and print each item."""
    table = get_table()
    
    # scan() retrieves ALL items in the table.
    # For large tables you'd use query() instead — but for our small
    # dataset, scan() is fine.
    response = table.scan()
    items = response.get("Items", [])
    
    if not items:
        print("No songs found. Make sure your DynamoDB table has data.")
        return
    
    print(f"Found {len(items)} song(s):\n")
    for song in items:
        print_song(song)


def main():
    print("===== Reading from DynamoDB =====\n")
    print_all_songs()

if __name__ == "__main__":
    main()
