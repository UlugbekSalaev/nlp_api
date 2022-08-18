# https://www.tutlinks.com/create-and-deploy-fastapi-app-to-heroku/
# from UzTransliterator import UzTransliterator
from fastapi import FastAPI

app = FastAPI()

from UzTransliterator import UzTransliterator

obj1 = UzTransliterator.UzTransliterator()
# print(obj.transliterate("маткаб", from_="cyr", to="lat"))

@app.get("/translit")
def translit(text: str, from_: str, to: str):
    return obj1.transliterate(text, from_, to)


@app.post("/translit")
def translit(text: str, from_: str, to: str):
    return obj1.transliterate(text, from_, to)


## -----------------------------------
from UzMorphAnalyser import UzMorphAnalyser

obj2 = UzMorphAnalyser.UzMorphAnalyser()

@app.get("/stem")
def stem(word: str):
    return obj2.stem(word)


@app.get("/lemmatize")
def lemmatize(word: str, pos: str = None):
    return obj2.lemmatize(word, pos)


@app.get("/analyze")
def analyze(word: str, pos: str = None):
    return obj2.analyze(word, pos)


## -----------------------------------
from uztagger import Tagger

obj3 = Tagger()

@app.get("/postagging")
def postagging(text: str):
    return obj3.pos_tag(text)