from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>平均坪數計算器</title>
    <style>
        body {
            font-family: "Microsoft JhengHei", sans-serif;
            margin: 20px;
            background: #f4f4f9;
        }
        .container {
            max-width: 400px;
            margin: auto;
            background: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        input {
            width: 100%;
            padding: 10px;
            margin: 8px 0;
            border: 1px solid #ccc;
            border-radius: 10px;
            font-size: 16px;
        }
        button {
            width: 100%;
            padding: 12px;
            background-color: #0078d7;
            color: white;
            font-size: 18px;
            border: none;
            border-radius: 10px;
        }
        button:hover {
            background-color: #005fa3;
        }
        .result {
            margin-top: 15px;
            font-size: 20px;
            text-align: center;
            color: #333;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2 style="text-align:center;">🏠 房價平均坪數計算</h2>
        <form method="POST">
            <label>總價（萬元）：</label>
            <input type="number" step="0.01" name="total_price" required>

            <label>車位價格（萬元）：</label>
            <input type="number" step="0.01" name="parking_price" required>

            <label>權狀坪數：</label>
            <input type="number" step="0.01" name="title_area" required>

            <label>車位坪數：</label>
            <input type="number" step="0.01" name="parking_area" required>

            <button type="submit">計算</button>
        </form>

        {% if result is not none %}
        <div class="result">
            💡 平均每坪價格：<b>{{ result }} 萬/坪</b>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        total_price = float(request.form["total_price"])
        parking_price = float(request.form["parking_price"])
        title_area = float(request.form["title_area"])
        parking_area = float(request.form["parking_area"])

        if title_area > parking_area:
            avg = (total_price - parking_price) / (title_area - parking_area)
            result = round(avg, 2)
        else:
            result = "⚠️ 權狀坪數需大於車位坪數！"

    return render_template_string(HTML_PAGE, result=result)

if __name__ == "__main__":
    # 可讓手機連線使用
    app.run(host="0.0.0.0", port=5000, debug=True)
