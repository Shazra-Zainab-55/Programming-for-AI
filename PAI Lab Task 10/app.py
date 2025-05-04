from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple chatbot logic
def get_response(user_input):
    user_input = user_input.lower()
    if "cardiology" in user_input:
        return "Our cardiology department operates from 9am to 5pm with Dr. Ahmed available on weekdays."
    elif "appointment" in user_input:
        return "You can book an appointment by calling 042-1234567 or through our website."
    elif "timing" in user_input or "hours" in user_input:
        return "Our medical center is open from 8am to 8pm, Monday to Saturday."
    elif "emergency" in user_input:
        return "For emergencies, please visit our ER which is open 24/7."
    elif "gynecology" in user_input:
        return "Our gynecology department has Dr. Maria and Dr. Saima available from 10am to 4pm."
    else:
        return "I'm sorry, I couldn't understand that. Please ask about departments, appointments, or timings."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.form["msg"]
    bot_response = get_response(user_input)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
