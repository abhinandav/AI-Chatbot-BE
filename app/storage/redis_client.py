import redis
import os
import json

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

def add_to_history(session_id: str, question: str, answer: str):
    entry = json.dumps({question: answer})
    r.rpush(session_id, entry)

def get_history(session_id: str):
    raw_items = r.lrange(session_id, 0, -1)
    history = [json.loads(item) for item in raw_items]
    return history

def clear_history(session_id: str):
    r.delete(session_id)
