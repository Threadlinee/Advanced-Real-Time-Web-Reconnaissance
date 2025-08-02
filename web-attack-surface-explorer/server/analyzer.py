from urllib.parse import urlparse

def analyze_entry(data):
    parsed = urlparse(data['url'])
    domain = parsed.netloc
    path = parsed.path
    is_js = path.endswith(".js")
    is_api = "/api" in path or data['method'] in ["POST", "PUT", "PATCH"]
    is_websocket = data['type'] == 'websocket'

    return {
        "url": data['url'],
        "domain": domain,
        "is_js": is_js,
        "is_api": is_api,
        "is_websocket": is_websocket,
        "status": data['statusCode']
    }
