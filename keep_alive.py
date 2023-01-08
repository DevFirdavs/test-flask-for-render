from flask import Flask, render_template
from threading import Thread 
import os 

app = Flask("app")

STATIC_DIR = os.path.abspath('static')

@app.route('/')
def main():
  return "working now

def run():
  app.run("0.0.0.0", port=8080)

def keep_alive():
  server = Thread(target=run)
  server.start()

if __name__ == "__main__":
  keep_alive()
