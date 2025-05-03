from Flask import flask
app = Flask(name)
@app.route('/')
def index():
  return "<h1>Hello Welcome to Flask</h1>"

if name == 'main":
  app.run(host='0.0.0.0' , port='5000')
