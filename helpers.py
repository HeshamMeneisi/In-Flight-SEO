def structure_headers(headers):
    for key, value in headers.items():
       headers[key] = [{"key": key, "value": value}]
    return headers
