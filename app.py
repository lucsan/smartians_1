from flask import Flask, render_template

# app = Flask(__name__)
app = Flask(__name__, template_folder='templates', static_folder='templates/assets')

@app.route('/')
def hello():
  # return 'Hello, World!'
  return render_template("index.html")

if __name__ == '__main__':
  app.run(debug=True)