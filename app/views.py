"""
This module has all the Flask views for the web application
"""

from flask import render_template, flash, redirect, jsonify, request
from app import app
from hospital_info_analyzer import Hospital_Data
from hospital_nlg import Hospital_NLG
import zipcode_analyzer as zipcode_analyzer


@app.route('/')
@app.route('/index')
def index():
    "The home page"

    return render_template('index.html', title='Home')


@app.route("/hospitals-near-me")
def search():
    "Return relevant hospitals"
    zip_code = request.args.get('query')
    if zip_code.strip() == "":
        return render_template('index.html', title='Home')
    else:
        zip_code_list = zipcode_analyzer.get_nearest_zips(str(zip_code))
        hospital_obj = Hospital_Data()
        hospitals = hospital_obj.filter_data_by_zipcode(zip_code_list)
        distance = []
        for curr_zip in hospitals['ZIP Code']:
            distance.append(
                zipcode_analyzer.get_distance_between_zips(zip_code, curr_zip))
        hospitals['Distance'] = distance
        nlg_obj = Hospital_NLG(hospitals)
        summary = nlg_obj.get_summary()

        return render_template('hospitals-near-me.html', title='Results', summary=summary)
