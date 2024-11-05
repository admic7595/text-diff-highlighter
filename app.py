from flask import Flask, render_template, request
import difflib

app = Flask(__name__)

def highlight_diff(text1, text2):
    """文字列を比較して違いをハイライト"""
    result = []
    for i in range(max(len(text1), len(text2))):
        char1 = text1[i] if i < len(text1) else ''
        char2 = text2[i] if i < len(text2) else ''
        is_different = char1 != char2
        result.append({
            'char': char1,
            'different': is_different
        })
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        text1 = request.form['text1']
        text2 = request.form['text2']
        result = {
            'text1': highlight_diff(text1, text2),
            'text2': highlight_diff(text2, text1)
        }
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)