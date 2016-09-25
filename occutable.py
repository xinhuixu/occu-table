from flask import Flask, render_template
import occupations

app = Flask(__name__)

@app.route("/")
def main():
    d = occupations.buildDict()
    return render_template('occutemp.html', docc = d)

if __name__ == "__main__":
    app.debug = True
    app.run()

