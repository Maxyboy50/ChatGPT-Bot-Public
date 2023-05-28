# Boto3 Documentation https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html
import time

def register_user(userID, table):
    table.put_item(Item={"userID": userID, "messages": []})


def fetch_message_history(userID, table):
    for i in range(5):
        try:
            message_history = table.get_item(Key={"userID": userID})
            message_list = message_history["Item"]["messages"]
            return message_list
        except KeyError as e:
            if "Item" not in message_history:
                register_user(userID=userID, table=table)
                continue
            else:
                break
        finally:
            time.sleep(2**i)


def update_user_message(userID, input, table):
    table.update_item(
        Key={"userID": userID},
        UpdateExpression=f"SET #messages = list_append(#messages, :value)",
        ExpressionAttributeNames={"#messages": "messages"},
        ExpressionAttributeValues={":value": [input]},
    )


def update_assistant_message(userID, response, table):
    proper_formatting = dict(response)
    table.update_item(
        Key={"userID": userID},
        UpdateExpression=f"SET #messages = list_append(#messages, :value)",
        ExpressionAttributeNames={"#messages": "messages"},
        ExpressionAttributeValues={":value": [proper_formatting]},
    )
