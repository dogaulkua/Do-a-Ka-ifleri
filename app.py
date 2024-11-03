from flask import Flask, request, jsonify
from fuzzy_logic import suggest_task

app = Flask(__name__)

@app.route('/suggest_task', methods=['POST'])
def suggest_task_api():
    try:
        data = request.get_json()
        interest_level_value = data.get('interestLevel', 0.5)
        task = suggest_task(interest_level_value)
        return jsonify({"suggestedTask": task}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
