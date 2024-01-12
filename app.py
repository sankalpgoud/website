from flask import Flask,render_template,jsonify

app = Flask(__name__)
hashira=[
  {
  'id': 1,
  'name': 'Rengoku',
  'Breathing style': 'flame',
  'age': 20
  },
  
  {
    'id': 2,
    'name': 'Shinobu Kochu',
    'Breathing style': 'Insect',
    'age': 18
    },
  {
    'id': 3,
    'name': 'Tokito',
    'Breathing style': 'Mist',
    'age': 14
    },
  {
    'id': 4,
    'name': 'Tomioka',
    'Breathing style': 'Water',
    'age': 21
    }
]

@app.route("/")
def helloworld():
  return render_template('p.html',hash=hashira,
                         name='Mitsuri')
@app.route("/api/hashira")
def _list():
  return jsonify(hashira)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
