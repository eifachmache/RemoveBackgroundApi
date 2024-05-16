from fastapi import FastAPI, File, UploadFile

from fastapi.responses import StreamingResponse
from rembg import remove
from io import BytesIO

# Start your server using:
# fastapi dev .\src\app.py
# uvicorn your_script_name:app --reload
app = FastAPI()


@app.post("/remove-bg/")
async def remove_background(file: UploadFile = File(...)):
    input_image = await file.read()
    output_image = remove(input_image)
    output_io = BytesIO(output_image)
    output_io.seek(0)
    return StreamingResponse(output_io, media_type="image/png")


@app.get("/")
async def root():
    return {"message": "Hello World"}
