from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

# load models and tokenizers at the start

# english -> spanish
en_to_es_tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-es")
en_to_es_model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-es")

# spanish -> english
es_to_en_tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-es-en")
es_to_en_model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-es-en")

# english -> french
en_to_fr_tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-fr")
en_to_fr_model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-fr")

# french -> english
fr_to_en_tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-fr-en")
fr_to_en_model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-fr-en")

# french -> spanish
fr_to_es_tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-fr-es")
fr_to_es_model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-fr-es")

# spanish -> french
es_to_fr_tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-es-fr")
es_to_fr_model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-es-fr")


en_to_es_pipeline = pipeline("translation", model=en_to_es_model, tokenizer=en_to_es_tokenizer)
es_to_en_pipeline = pipeline("translation", model=es_to_en_model, tokenizer=es_to_en_tokenizer)

en_to_fr_pipeline = pipeline("translation", model=en_to_fr_model, tokenizer=en_to_fr_tokenizer)
fr_to_en_pipeline = pipeline("translation", model=fr_to_en_model, tokenizer=fr_to_en_tokenizer)

fr_to_es_pipeline = pipeline("translation", model=fr_to_es_model, tokenizer=fr_to_es_tokenizer)
es_to_fr_pipeline = pipeline("translation", model=es_to_fr_model, tokenizer=es_to_fr_tokenizer)

# inference

# english -> spanish
def inf_en_to_es(en_input):
    es_prediction = en_to_es_pipeline(en_input)
    es_prediction = es_prediction[0]['translation_text']
    return es_prediction

# spanish -> english
def inf_es_to_en(es_input):
    en_prediction = es_to_en_pipeline(es_input)
    en_prediction = en_prediction[0]['translation_text']
    return en_prediction

# english -> french
def inf_en_to_fr(es_input):
    fr_prediction = en_to_fr_pipeline(es_input)
    fr_prediction = fr_prediction[0]['translation_text']
    return fr_prediction

# french -> english
def inf_fr_to_en(es_input):
    en_prediction = fr_to_en_pipeline(es_input)
    en_prediction = en_prediction[0]['translation_text']
    return en_prediction

# french -> spanish
def inf_fr_to_es(es_input):
    es_prediction = fr_to_es_pipeline(es_input)
    es_prediction = es_prediction[0]['translation_text']
    return es_prediction

# spanish -> french
def inf_es_to_fr(es_input):
    fr_prediction = es_to_fr_pipeline(es_input)
    fr_prediction = fr_prediction[0]['translation_text']
    return fr_prediction