from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    table_html = ""

    if request.method == "POST":
        number = int(request.form["number"])

        table_html += f"<h2>Multiplication Table of {number}</h2>"

        for i in range(1, 11):
            table_html += f"{number} × {i} = {number * i}<br>"

    return f"""
    <html>
    <body>
        <h1>Multiplication Table Generator</h1>

        <form method="POST">
            <label>Enter a number:</label>
            <input type="number" name="number" required>
            <button type="submit">Generate Table</button>
        </form>

        <br>

        {table_html}

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)