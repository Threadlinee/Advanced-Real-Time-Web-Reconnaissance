from flask import Flask, request, jsonify
from analyzer import analyze_entry
import json, os

app = Flask(__name__)
entries = []

@app.route('/collect', methods=['POST'])
def collect():
    data = request.get_json()
    analyzed = analyze_entry(data)
    entries.append(analyzed)
    return jsonify({"status": "received"})

@app.route('/export', methods=['GET'])
def export():
    with open("output/results.json", "w") as f:
        json.dump(entries, f, indent=2)
    return jsonify({"status": "exported", "count": len(entries)})

if __name__ == "__main__":
    os.makedirs("output", exist_ok=True)
    app.run(port=5000)




