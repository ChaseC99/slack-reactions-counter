import json

# From https://slack.com/api/conversations.history?channel=<CHANNEL>
messages = json.load(open('photos.json'))['messages']

parsed_messages = []

for message in messages:
    reactors = set()
    if "reactions" in message:
        for reaction in message["reactions"]:
            reactors.update(set(reaction["users"]))

    parsed_messages.append({"reactors": list(reactors), "num_reactors": len(reactors), "text": message["text"]})

parsed_messages.sort(key=lambda m: m["num_reactors"],reverse=True)

with open('results.txt', 'w') as json_file:
  json.dump(parsed_messages, json_file)