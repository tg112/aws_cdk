import json
import os
import uuid

import boto3

table_name = os.environ.get("TABLE_NAME")
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(table_name)

def handler(event, context):
    method = event["httpMethod"]

    if method == "POST":
        item = json.loads(event["body"])
        item['id'] = str(uuid.uuid4())
        table.put_item(Item=item)
        return {
            "statusCode": 200,
            "body": json.dumps({"id": item["id"]}),
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "*",
            },
        }

    if method == "GET":
        employee_id = event['queryStringParameters']['id']
        response = table.get_item(Key={"id": employee_id})
        if "Item" in response:
            return {
                "statusCode": 200,
                "body": json.dumps(response["Item"]),
                "headers": {
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "*",
                },
            }
