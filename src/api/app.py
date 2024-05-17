from dotenv import load_dotenv

load_dotenv()

from typing import Annotated, Container
from fastapi import Depends, FastAPI, File, HTTPException, Request, UploadFile

from fastapi.responses import StreamingResponse
from rembg import remove
from io import BytesIO

from .dependencies import get_container


def authorize(
    request: Request,
    container: Annotated[Container, Depends(get_container)],
):
    api_key = request.headers.get("Authorization")
    is_authenticated = api_key == f"Bearer {container.config.api_key}"

    if not is_authenticated:
        raise HTTPException(status_code=401, detail="Unauthorized")


# Start your server using:
# fastapi dev .\src\app.py
# uvicorn your_script_name:app --reload
app = FastAPI(dependencies=[Depends(authorize)])


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
