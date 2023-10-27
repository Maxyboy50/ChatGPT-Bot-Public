import os
import json
import boto3
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
from discord_interactions import command_handler

PUBLIC_KEY = os.getenv("PUBLIC_KEY")
TABLE_NAME = os.getenv("TABLE_NAME")
dynamo_db = boto3.resource("dynamodb", region_name="us-east-2")
dynamo_db_table = dynamo_db.Table(TABLE_NAME)


def lambda_handler(event, context):
    body = event["body"]
    body_json = json.loads(body)
    signature = event["headers"]["x-signature-ed25519"]
    timestamp = event["headers"]["x-signature-timestamp"]
    verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))
    try:
        verify_key.verify(f"{timestamp}{body}".encode(), bytes.fromhex(signature))
        if body_json["type"] == 1:
            return {"statusCode": 200, "body": json.dumps({"type": 1})}
        elif body_json["type"] != 1:
            interaction_id = body_json["id"]
            interaction_token = body_json["token"]
            application_id = body_json["application_id"]
            userID = body_json["member"]["user"]["id"]

            command_data = body_json["data"]
            command_name = command_data["name"]
            command_value = command_data["options"][0]["value"]
            return command_handler(
                command_name,
                interaction_token,
                userID,
                interaction_id,
                dynamo_db_table,
                application_id,
                command_value,
            )
    except BadSignatureError:
        return {"statusCode": 401, "body": json.dumps("Invalid request signature")}
