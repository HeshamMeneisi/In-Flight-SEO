def structure_headers(headers):
    for key, value in headers.items():
       headers[key] = [{"key": key, "value": value}]
    return headers


def get_pattern(rule):
    if "exact" in rule and rule["exact"]:
        return rule["pattern"] + "$"
    if "strict" in rule and rule["strict"]:
        return rule["pattern"] + "(/*$|/*\?[^/]+)"
    
    return rule["pattern"]
