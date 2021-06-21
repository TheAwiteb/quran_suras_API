from typing import Optional
import uvicorn
from fastapi import FastAPI, Query
from quran_suras import QuranSuras

app = FastAPI()
API = QuranSuras()
HOST = "127.0.0.1"
PORT = 8000
# run this command in terminal : python app.py

print(f"http://{HOST}:{PORT}/docs")

@app.get("/")
def read_root():
    return {
        "Methods":
            [
                'get_sura_by_number', 'get_sura_by_name',
                    'get_sura_name', 'get_sura_number',
                        'get_page', 'get_radios'
                ]
            }


# get_sura_by_number
@app.get("/get_sura_by_number/")
def get_sura_by_number(sura_number: int, amount: Optional[int] = Query(10, description="Amount of suras")):
    try:
        suras_result = API.get_sura_by_number(sura_number=sura_number,
                                                amount=amount)
        suras_result.update({'ok':True})
        return suras_result
    except Exception as err:
        return {"ok":False, "error":str(err)}

# get_sura_by_name
@app.get("/get_sura_by_name/")
def get_sura_by_name(sura_name:str, amount: Optional[int] = Query(10, description="Amount of suras")):
    try:
        suras_result = API.get_sura_by_name(sura_name=sura_name,
                                                amount=amount)
        suras_result.update({'ok':True})
        return suras_result
    except Exception as err:
        return {"ok":False, "error":str(err)}

# get_sura_name
@app.get("/get_sura_name/")
def get_sura_name(sura_number: int):
    try:
        sura_name = {'name':API.get_sura_name(sura_number=sura_number)}
        sura_name.update({'ok':True})
        return sura_name
    except Exception as err:
        return {"ok":False, "error":str(err)}

# get_sura_number
@app.get("/get_sura_number/")
def get_sura_number(sura_name: str):
    try:
        sura_number = {'number':API.get_sura_number(sura_name=sura_name)}
        sura_number.update({'ok':True})
        return sura_number
    except Exception as err:
        return {"ok":False, "error":str(err)}

# get_page
@app.get("/get_page/")
def get_page(page_number: int):
    try:
        page_url = {'page_url':API.get_page(page_number=page_number)}
        page_url.update({'ok':True})
        return page_url
    except Exception as err:
        return {"ok":False, "error":str(err)}

# get_radios
@app.get("/get_radios/")
def get_radios(language: str, amount: Optional[int] = Query(3, description="Amount of radios")):
    try:
        radios = API.get_radios(language=language, amount=amount)
        radios.update({'ok':True})
        return radios
    except Exception as err:
        return {"ok":False, "error":str(err)}

if __name__== "__main__":
    uvicorn.run("app:app",host=HOST, port=PORT, reload=True, debug=True, workers=3)