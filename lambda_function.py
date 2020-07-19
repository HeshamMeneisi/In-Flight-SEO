import re
from fetch_html import fetch_html
from transform_state import transform_state
from rules import rules
from helpers import structure_headers

def lambda_handler(event, context):
    request = event["Records"][0]["cf"]["request"]
    
    if re.match("\.(js|css|jpg|png|svg)$", request["uri"]):
        return request
        
    for rule in rules: 
        if not re.match(rule["pattern"], request["uri"]):
            continue
        state = fetch_html("YOUR_BUCKET_NAME_HERE")
        state['request'] = request
        state["response_headers"] = {"content-type": "text/html"}
        status = state["status"]
        if status>= 200 and status < 400:
            transform_state(state, rule)
        return {
            "status": state["status"],
            "body": state["html"],
            "headers": structure_headers(state["response_headers"])
        }
        
    return request
