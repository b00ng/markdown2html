from flask import Flask, request, render_template
import markdown2
import sys

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  try:
      converted_html = ""
      markdown_text = ""
      if request.method == 'POST':
          markdown_text = request.form['markdown']
          converted_html = markdown2.markdown(markdown_text)
      return render_template('index.html', converted_html=converted_html, markdown_text=markdown_text)
  except Exception as e:
      print(f"An error occurred: {str(e)}", file=sys.stderr)
      return f"An error occurred: {str(e)}", 500

@app.route('/_health')
def health_check():
  return "OK", 200

# Created/Modified files during execution:
print("api/index.py")
