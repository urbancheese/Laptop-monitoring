import urllib.request
import json
import datetime
import os

WEBHOOK_URL = 'YOUR_WEBHOOK_URL_HERE'
HEADERS = {
    'Content-Type': 'application/json', 
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def send_notification():
    if not WEBHOOK_URL or WEBHOOK_URL.startswith('YOUR_WEBHOOK'):
        return

    try:
        now = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
        user = os.getlogin()
        pc_name = os.environ.get('COMPUTERNAME', 'Unknown PC')

        data = {
            "username": "System Monitor",
            "embeds": [{
                "title": "💻 System Started",
                "description": f"**{pc_name}** (User: {user}) has come online.",
                "color": 3447003,
                "fields": [
                    {"name": "Date & Time", "value": now, "inline": True}
                ],
                "footer": {"text": "Automated Startup Alert"}
            }]
        }

        req = urllib.request.Request(
            WEBHOOK_URL, 
            data=json.dumps(data).encode('utf-8'), 
            headers=HEADERS
        )
        
        try:
            urllib.request.urlopen(req, timeout=5)
        except Exception:
            pass
            
    except Exception as e:
        error_data = {
            "username": "System Monitor",
            "embeds": [{
                "title": "⚠️ Execution Error",
                "description": f"Failed to run startup script on **{os.environ.get('COMPUTERNAME', 'Unknown PC')}**.",
                "color": 16711680,
                "fields": [
                    {"name": "Traceback", "value": f"```python\n{str(e)}\n```", "inline": False}
                ]
            }]
        }
        
        try:
            req = urllib.request.Request(
                WEBHOOK_URL, 
                data=json.dumps(error_data).encode('utf-8'), 
                headers=HEADERS
            )
            urllib.request.urlopen(req, timeout=5)
        except Exception:
            pass

if __name__ == "__main__":
    send_notification()
