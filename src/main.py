import os
import pathlib

#from src.Libraries import *

#from src.utils import id2details, vector_search, faiss_index, DATAFRAME
import pickle
import uvicorn
from typing import Optional
from fastapi import FastAPI, File, UploadFile, Request
#from fastapi.templating import Jinja2Templates
from starlette.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse



BASE_DIR = pathlib.Path(__file__).parent
#df = pd.read_csv(BASE_DIR/"")


app = FastAPI()

app.mount("/static", StaticFiles(directory=BASE_DIR/"static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR/"templates")


### IMPORTANT VARIABLES


#df = DATAFRAME(df)
#model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
#index = faiss_index("/notebooks/qqq.ai/src/faiss/index.pkl")



@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})




@app.get("/search", response_class=HTMLResponse)
async def search(request: Request,):
    #query = request.query_params.get("query")

    
    Authors = [
    
    '##A pen, a piece of white paper, and an idea can create a new you.', \
    'The principle virtue of anyone who made an important invention is curious persistence.', 
    'To grow the power of an imagination, travel to see the world.', 
    'There were also the Masters of Arcane Knowledge. Everyone begrudged their presence among the gifteds. These were the kids that could break down an engine and build it back again - no diagrams or instructions needed. They understood things in a real, not theoretical, way. They seemed not to care about their grades.', 
    "Knowledgeable [10w] The knowledgeable man inventoried and catalogued everything he doesn't know.", 
    "The Phenomenon of Life {Couplet} The potter's some man of clay who's molding clay,a robot making an automaton;Every day we recreate ourselves from what bricks we're made,how wondrous life's phenomenon!"
    
    ]
    
       
    Quotes = [
    
    'A pen.', 
    'curious.', 
    'To grow ',
    'Oliver Wendell Holmes, Jr.', 
    'Masters',
    "piece of ",
    "white paper", 
    "an idea", 
    "can create", 
    "a new yo",

    ]
    return templates.TemplateResponse("search.html", {
                                                      "request": request, 
                                                      "Authors": Authors,
                                                      "Quotes": Quotes, })