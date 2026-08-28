from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_route():
    title = request.form.get("title")
    size = int(request.form.get("size"))
    # TODO: parse categories out of the form
    # TODO: call generate() from generator.py
    # TODO: call build_pdf() (or a bytes-returning version) from pdf_builder.py
    # TODO: return the file(s) to the browser
    pass

if __name__ == "__main__":
    app.run(debug=True)