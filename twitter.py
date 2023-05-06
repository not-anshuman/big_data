import tweepy
import json

bearer_token = "ADD TOKEN HERE"

class CustomStreamingClient(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(json.dumps(tweet.data))

    def on_error(self, errors):
        print(f"Error: {errors}")

streaming_client = CustomStreamingClient(bearer_token)
location_bbox = [74.557000, 32.912000, 75.342000, 33.76000]  # Coordinates here

rule = f"bounding_box:[{location_bbox[0]} {location_bbox[1]} {location_bbox[2]} {location_bbox[3]}]"
stream_rule = tweepy.StreamRule(value=rule)
added_rules = streaming_client.add_rules([stream_rule])

# print(added_rules), check if the rule has been added successfully or not

try:
    print("Starting the stream...")
    streaming_client.filter()
except KeyboardInterrupt:
    print("Stopped.")
finally:
    streaming_client.disconnect()