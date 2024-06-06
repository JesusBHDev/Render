from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    Mi nombre es Jesus Ivan Bautista Hernandez<br>
    Soy de 9º cuatrimestre del grupo<br>
    De la universidad UTHH
    """

if __name__ == '__main__':
    app.run(debug=True)
