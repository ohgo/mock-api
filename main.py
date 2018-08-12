import json
import responsemap

def handle(event, context):
    print("event: {}".format(event))
    return json.loads(responsemap.get(event["httpMethod"], event["path"]))
