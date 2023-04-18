from flask import Flask, request, jsonify
import pandas as pd
import plotly.express as px
from main import process1, process2
from typing import List
import ast
app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Welcome'})

# TODO: Create a flask app with two routes, one for each function.
# The route should get the data from the request, call the function, and return the result.

@app.route('/process1',methods=['POST'])
def process1route():
    x = request.get_data()
    return jsonify(process1(x))

@app.route('/process2',methods=['POST'])
def process2route():
    x = request.get_data()
    return jsonify(process2(x))

@app.route('/done',methods=['POST'])
def done():
    def pro(data: List[int]) -> List[int]:
        return data;
    fig=request.json

    print(fig) 
    df = pd.DataFrame(fig,columns=['process','run_mean','run_std'])
    fig = px.bar(df,x="process", y= "run_mean", error_y="run_std", opacity=0.6)
    fig.write_image( "makespan.png" )
    return fig
if __name__ == "__main__":
    app.run(host="0.0.0.0")
