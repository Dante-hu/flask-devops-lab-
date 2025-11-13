import random
from flask import Flask


app = Flask(__name__)

# random DevOps quotes
DEVOPS_QUOTES = [
    "Keep pushing forward, DevOps is the way!",
    "Automate everything, sleep better.",
    "Infrastructure as code – because copy-paste is not a strategy.",
    "Fail fast, learn faster.",
    "CI/CD: Continuous Improvement, Continuous Delivery.",
    "Your pipeline is only as strong as its weakest test.",
    "Ship it, monitor it, improve it.",
]


@app.route("/")
def hello():
    return "Hello, DevOps World!"


@app.route("/motivator")
def motivator():
    return random.choice(DEVOPS_QUOTES)


if __name__ == "__main__":
    app.run()
