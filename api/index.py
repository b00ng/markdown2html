from flask import Flask, request, render_template
import markdown2

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  converted_html = ""
  markdown_text = ""
  if request.method == 'POST':
      markdown_text = request.form['markdown']
      converted_html = markdown2.markdown(markdown_text)
  return render_template('index.html', converted_html=converted_html, markdown_text=markdown_text)

if __name__ == '__main__':
  app.run(debug=True)

# Created/Modified files during execution:
print("api/index.py")
