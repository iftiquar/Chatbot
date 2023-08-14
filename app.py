from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def chatbot():
    if request.method == 'POST':
        user_message = request.form['user_message']
        # Add your chatbot logic here
        response = "Hello, I'm a chatbot! Please tell me your age, gender, and ethnicity."
        return render_template('index.html', user_message=user_message, bot_message=response)
    return render_template('index.html', user_message='', bot_message='')

if __name__ == '__main__':
    app.run(debug=True)