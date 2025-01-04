import datetime
from flask import Flask, request
import time

from translation_inf import *

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/api/translate_eng_to_spa', methods=["POST"])
def translate_en_to_es():
    data = request.json
    en_input = data['input']
    es_translation = inf_en_to_es(en_input)
    return {
        "translation" : es_translation,
        "timestamp" : datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "lang_code" : "spa"
    }
    
@app.route('/api/translate_spa_to_eng', methods=["POST"])
def translate_es_to_en():
    data = request.json
    es_input = data['input']
    en_translation = inf_es_to_en(es_input)
    return {
        "translation" : en_translation,
        "timestamp" : datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "lang_code" : "eng"
    }
    
@app.route('/api/translate_eng_to_fre', methods=["POST"])
def translate_en_to_fr():
    data = request.json
    en_input = data['input']
    fr_translation = inf_en_to_fr(en_input)
    print(fr_translation)
    return {
        "translation" : fr_translation,
        "timestamp" : datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "lang_code" : "fre"
    }
    
@app.route('/api/translate_fre_to_eng', methods=["POST"])
def translate_fr_to_en():
    data = request.json
    fr_input = data['input']
    en_translation = inf_fr_to_en(fr_input)
    return {
        "translation" : en_translation,
        "timestamp" : datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "lang_code" : "eng"
    }
    
@app.route('/api/translate_fre_to_spa', methods=["POST"])
def translate_fr_to_es():
    data = request.json
    fr_input = data['input']
    es_translation = inf_fr_to_en(fr_input)
    return {
        "translation" : es_translation,
        "timestamp" : datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "lang_code" : "spa"
    }
    
@app.route('/api/translate_spa_to_fre', methods=["POST"])
def translate_es_to_fr():
    data = request.json
    es_input = data['input']
    fr_translation = inf_fr_to_en(es_input)
    return {
        "translation" : fr_translation,
        "timestamp" : datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "lang_code" : "fre"
    }