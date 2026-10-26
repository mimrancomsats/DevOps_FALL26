from flask import Flask, render_template_string, request

app = Flask(__name__)

# Simple HTML template
html = """
<!DOCTYPE html>
<html>
<head>
    <title>Square Calculator</title>
</head>
<body style="font-family: Arial; text-align: center; margin-top: 50px;">
    <h1>Square Calculator</h1>
    <form method="POST">
        <label>Enter a number:</label><br><br>
        <input type="number" name="number" required>
        <input type="submit" value="Calculate"><br><br>
    </form>

    {% if result is not none %}
        <h2>Result: {{ result }}</h2>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        num = float(request.form["number"])
        result = num ** 2
    return render_template_string(html, result=result)

if __name__ == "__main__":
    app.run(debug=True)
