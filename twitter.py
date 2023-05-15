import tweepy
import json

bearer_token = "AAAAAAAAAAAAAAAAAAAAADFvdAEAAAAAxPnJv7Me0GQYLWsePtBmHPyB1sI%3Dk10HZD9DHLTAazMR8dc2J2H5KlI9SlV1YmkZAyUxhFKn2SrIze"


class CustomStreamingClient(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(json.dumps(tweet.data))

    def on_error(self, errors):
        print(f"Error: {errors}")


streaming_client = CustomStreamingClient(bearer_token)
location_bbox = [74.72000, 32.650000, 74.930000, 32.80000]  # Coordinates here

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
