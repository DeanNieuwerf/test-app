from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def display_template():
    with open('templates/template.html', 'r') as file:
        html_content = file.read()
    return html_content

if __name__ == '__main__':
    app.run(debug=True)