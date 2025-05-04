from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    # Placeholder response from the AI model
    bot_response = "This is a placeholder response."
    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(debug=True)