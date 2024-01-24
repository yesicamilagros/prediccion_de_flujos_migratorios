from flask import Flask , render_template, request
import pickle
app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route("/")
def hello():
    return render_template('forest.html')

@app.route("/predict", methods=['POST'])
def predict():
    rooms = int(request.form['rooms'])
    distance = int(request.form['distance'])
    prediction = model.predict([[rooms, distance]])
    output = round(prediction[0], 2)
    return render_template('forest.html', pred=f'tiene un PBI de {rooms} y un indice de gini de {distance}, el flujo de migracion aproximado es {output}',dash= "https://app.powerbi.com/view?r=eyJrIjoiYzJhYzM5ODctY2M4YS00ODBlLThiNWEtNTZkNDM5OTA3MTk0IiwidCI6IjFmODEwNTkyLTJiMTAtNGQyZi05ZDFkLWNhMzFiMjY5MTVkZSIsImMiOjR9")


if __name__=="__main__":
    app.run()