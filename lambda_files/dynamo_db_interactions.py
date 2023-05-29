import time
import openai
def register_user(userID: str, table: None):
    table.put_item(Item={"userID": userID, "messages": []})


def fetch_message_history(userID: str, table: None):
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


def update_user_message(userID: str, input: dict, table: None):
    table.update_item(
        Key={"userID": userID},
        UpdateExpression=f"SET #messages = list_append(#messages, :value)",
        ExpressionAttributeNames={"#messages": "messages"},
        ExpressionAttributeValues={":value": [input]},
    )


def update_assistant_message(userID: str, response: None , table: None):
    proper_formatting = dict(response)
    table.update_item(
        Key={"userID": userID},
        UpdateExpression=f"SET #messages = list_append(#messages, :value)",
        ExpressionAttributeNames={"#messages": "messages"},
        ExpressionAttributeValues={":value": [proper_formatting]},
    )
