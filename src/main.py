import os
from src.Libraries import *

from src.utils import id2details, vector_search, faiss_index, DATAFRAME
import pickle
import uvicorn
from typing import Optional
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles



BASE_DIR = pathlib.Path(__file__).parent
df = pd.read_csv(BASE_DIR/"")


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


### IMPORTANT VARIABLES


df = DATAFRAME(df)
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
index = faiss_index("/notebooks/qqq.ai/src/faiss/index.pkl")



@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})



async def search(query:str, request: Request):
    query = request.query_params.get("query")
    
    ### MAIN SEARCH ENGINE 
    D, I = vector_search([query], model, index, num_results=1000)

    # Fetching Results
    results = id2details(df, I, 'Quote')
    new_results = [str for sublist in results for str in sublist]

    # Create a boolean mask that returns True for rows that match the list
    search_result = list(set(new_results))
    mask = df['Quote'].isin(search_result)
    # Use the mask to index the dataframe and convert the result to a dictionary
    result = df[mask].to_dict()
    # Get the indices from the first value of the dictionary
    indices = list(result.values())[0].keys()
    
    Author = []
    Quotes = []


    for index in indices:
        Author.append(result['Author'][index])
        Quotes.append(result['Quote'][index]) 


    return templates.TemplateResponse("search.html", {"query": query, 
                                                      "request": request, 
                                                      "Author": Author,
                                                      "Quote": Quotes, })