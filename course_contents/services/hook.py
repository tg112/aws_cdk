import urllib3
import json
http = urllib3.PoolManager()

def handler(event, context):
    print('calling stack!!')
    url = "https://hooks.slack.com/triggers/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"

    msg = {
        "channel": "#webhook",
        "text": event["Records"][0]["Sns"]["Message"],
    }

    encoded_msg = json.dumps(msg).encode("utf-8")
    resp = http.request('POST', url, headers={'Content-Type': 'application/json'}, body=encoded_msg)
    print({
        "message": event["Records"][0]["Sns"]["Message"],
        "status_code": resp.status,
        "response": resp.data
    })