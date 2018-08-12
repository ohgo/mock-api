import boto3

db = boto3.client('dynamodb')

def get(method, path):
    print("Getting response for {} {}".format(method, path))
    prefix = "duduksini"
    result = db.query(
        TableName = "mock-api-responsemap",
        KeyConditionExpression = "prefix = :prefix",
        ExpressionAttributeValues = {
            ":prefix": {"S": prefix},
        },
    )
    # TODO: match all items' method & path vs our method & path
    matchedResponse = result["Items"][0]["response"]["S"]

    print(matchedResponse)
    return(result["Items"][0]["response"]["S"])
