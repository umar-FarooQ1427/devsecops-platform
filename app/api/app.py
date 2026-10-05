import os
import redis
from flask import Flask, jsonify

app = Flask(__name__)
r = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379)

@app.get("/")
def index():
    return jsonify(message="hello from the platform", visits=r.incr("visits"))

@app.get("/healthz")
def health():
    return "ok"
