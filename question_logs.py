logs = [
    {"timestamp": "2025-06-06T15:01:23", "user_id": "abc123", "event": "login", "ip": "192.168.1.2"},
    {"timestamp": "2025-06-06T15:20:05", "user_id": "abc123", "event": "login", "ip": "192.168.1.2"},
    {"timestamp": "2025-06-06T16:05:01", "user_id": "abc123", "event": "login", "ip": "192.168.1.3"},
    {"timestamp": "2025-06-06T16:10:20", "user_id": "xyz789", "event": "purchase", "ip": "10.0.0.5"},
    {"timestamp": "2025-06-06T16:30:55", "user_id": "xyz789", "event": "purchase", "ip": "10.0.0.5"},
    {"timestamp": "2025-06-06T17:05:30", "user_id": "abc123", "event": "logout", "ip": "192.168.1.2"},
]

for i in range(0, len(logs)):
    print(logs[i]["timestamp"], end=" ")
    print(logs[i]["user_id"], end=" ")
    print(logs[i]["event"], end=" ")
    print(logs[i]["ip"])