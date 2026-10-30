from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route('/blog')
def home():
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url)
    post = response.json()
    return render_template("index.html", all_post=post)

@app.route('/post/<int:num>')
def get_read(num):
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url)
    post = response.json()
    return render_template("post.html", all_post=post, num=num)

if __name__ == "__main__":
    app.run(debug=True)
