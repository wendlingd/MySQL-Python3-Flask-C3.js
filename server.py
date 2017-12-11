from flask import Flask, render_template, jsonify, url_for, redirect, request
from model import *
import pandas as pd

'''
This package shows a bar chart from a database, through a local web server
(localhost). Created for use with MySQL 5.6, Python 3, sqlalchemy, pandas, 
Flask, and for the grouped bar chart, C3.js, which is based on D3.js, 
version 3 (D3.js is now in version 4). You'll need to create the test 
database using mysqlscript.sql. NOT guaranteed to suit your need. 
Contrived from the original; I will test more later.

A few URLs I used:
    https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_csv.html
    http://flask.pocoo.org/docs/0.12/tutorial/views/#tutorial-views
    http://docs.sqlalchemy.org/en/latest/core/engines.html
    https://stackoverflow.com/questions/39881571/best-way-to-transfer-data-from-flask-to-d3
    
    YOUR TEST URL NEEDS TO BE: http://localhost:5000/chartUsage/102
'''


# 
# Good test page: AND Address = 'https://www.nlm.nih.gov/bsd/pmresources.html'


app = Flask(__name__)


# Page the chart will appear on
@app.route("/<int:GroupCode>")
    MicrositeData = getMicrositeData(GroupCode)

    return render_template('index.html', MicrositeData=MicrositeData)


# How the chart data is obtained; called from index.html
@app.route("/chartUsage/<int:GroupCode>")
def chartUsage(GroupCode):
    ChartPVvsSearch = getChartPVvsSearch(GroupCode)
    chartData = ChartPVvsSearch.to_csv(index=False)
    
    return chartData


if __name__ == "__main__":
    app.run(debug=True, port=5000)
