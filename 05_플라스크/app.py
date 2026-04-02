from flask import Flask, render_template    #플라스크 == 백엔드

app = Flask(__name__)

@app.route("/")		
def hello_world():
    return render_template("index.html")  # render_template <---- html로 보여주고 싶을때

@app.route("/hello")
def hello():
    return "만나서 반갑습니다."

@app.route("/user/<userId>")
def profile(userId):
    return f"{userId}\' profile"

if __name__=='__main__':
    app.run(debug=True)