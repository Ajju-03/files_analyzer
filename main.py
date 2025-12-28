from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import RedirectResponse, JSONResponse
from analyzer import analyze_file
import shutil
import os

app = FastAPI()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())
    try:
        result = analyze_file(file_path)
        return result
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
