from flask import render_template, url_for
import pandas as pd
import json
import plotly
import plotly.express as px
from application import app


@app.route("/")
def index():
    # Graph One
    df = px.data.medals_wide()
    fig1 = px.bar(
        df, x="nation", y=["gold", "silver", "bronze"], title="Wide=FormInput"
    )
    # Convert the Graph One to JSON
    graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph Two
    df = px.data.iris()
    fig2 = px.scatter_3d(
        df,
        x="sepal_length",
        y="sepal_width",
        z="petal_width",
        color="species",
        title="Iris Dataset",
    )
    # Convert the Graph Two to JSON
    graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph Three
    df = px.data.gapminder().query("continent=='Oceania'")
    fig3 = px.line(df, x="year", y="lifeExp", color="country", title="Life Expectancy")
    # Convert the Graph Three to JSON
    graph3JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template(
        "index.html",
        title="Home",
        graph1JSON=graph1JSON,
        graph2JSON=graph2JSON,
        graph3JSON=graph3JSON,
    )
