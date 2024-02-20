from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def say_welcome():
    """Returns simple welcome greeting."""
    return "welcome"

@app.route('/welcome/<visited>')
def visit_greet(visited):
    """Returns welcome greeting with additional either home or back, respectively,
    when specified in path."""
    if visited == 'home' or visited == 'back':
        return f"welcome {visited}"
    else:
        return "welcome"