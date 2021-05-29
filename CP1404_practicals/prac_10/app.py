from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World! :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)


def celsius_to_fahrenheit(celsius):
    """Convert celsius to Fahrenheit"""
    return celsius * 9.0 / 5 + 32


@app.route('/f/<celsius>')
def f(celsius=""):
    fahrenheit = celsius_to_fahrenheit(float(celsius))
    return "<h1>Celsius temperature: {} degrees. Converts to {} Fahrenheit.<h1>".format(str(celsius), str(fahrenheit))


if __name__ == '__main__':
    app.run()
