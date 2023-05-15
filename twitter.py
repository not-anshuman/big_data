import tweepy
import json
import os
import csv
from dotenv import load_dotenv

load_dotenv()

bearer_token = os.environ.get("BEARER_TOKEN")
if bearer_token is None:
    raise ValueError(
        "No bearer token found in environment variable BEARER_TOKEN")


class CustomStreamingClient(tweepy.StreamingClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.csv_file = open('tweets.csv', 'a', newline='', encoding='utf-8')
        self.csv_writer = csv.writer(self.csv_file)
        self.csv_writer.writerow(
            ['id', 'screen_name', 'created_at', 'text'])  # Write header

    def on_tweet(self, tweet):
        print(json.dumps(tweet.data))
        if 'id' in tweet and 'text' in tweet:
            id = tweet['id']
            text = tweet['text']
            screen_name = tweet['user']['screen_name'] if 'user' in tweet and 'screen_name' in tweet['user'] else ''
            created_at = tweet['created_at'] if 'created_at' in tweet else ''
            self.csv_writer.writerow(
                [id, screen_name, created_at, text])  # Write row
        else:
            print("Tweet does not contain necessary fields.")

    def on_error(self, errors):
        print(f"Error: {errors}")

    def disconnect(self):
        super().disconnect()
        self.csv_file.close()  # Close the CSV file


streaming_client = CustomStreamingClient(bearer_token)
location_bbox = [-74.05, 40.63, -73.85, 40.88]  # Coordinates here

rule = f"bounding_box:[{location_bbox[0]} {location_bbox[1]} {location_bbox[2]} {location_bbox[3]}]"
stream_rule = tweepy.StreamRule(value=rule)
# print(streaming_client.add_rules([stream_rule]))
print(streaming_client.get_rules())

try:
    print("Starting the stream...")
    streaming_client.filter()
except KeyboardInterrupt:
    print("Stopped.")
finally:
    streaming_client.disconnect()
