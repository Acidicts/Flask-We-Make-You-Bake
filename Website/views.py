from . import app


@app.route('/')
def home():
    render_template('index.html')
