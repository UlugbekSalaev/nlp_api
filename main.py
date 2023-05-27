from fastapi import FastAPI, HTTPException
from uztagger import Tagger
from UzTransliterator import UzTransliterator
from UzMorphAnalyser import UzMorphAnalyser
from fastapi.middleware.cors import CORSMiddleware
from UzSyllable import syllables, count, line_break

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

#  ---------------UzTransliterator---------------
obj1 = UzTransliterator.UzTransliterator()


@app.post("/translit")
async def translit(text: str, from_: str, to: str):
    return str(obj1.transliterate(text, from_, to)).replace('"', '')


#  ---------------UzMorphAnalyser---------------
obj2 = UzMorphAnalyser()


@app.post("/stem")
async def stem(word: str):
    return obj2.stem(word)


@app.post("/lemmatize")
async def lemmatize(word: str, pos: str = None):
    return obj2.lemmatize(word, pos)


@app.post("/analyze")
async def analyze(word: str, pos: str = None):
    return obj2.analyze(word, pos)


# ---------------uztagger---------------
obj3 = Tagger()


@app.post("/postagging")
async def postagging(text: str):
    return obj3.pos_tag(text)


# ----------------UzSyllable----------------


@app.post("/syllables")
async def stem(word: str):
    return syllables(word)

@app.post("/count-syllables")
async def stem(word: str):
    return count(word)


@app.post("/line-break-syllables")
async def stem(word: str):
    return line_break(word)
