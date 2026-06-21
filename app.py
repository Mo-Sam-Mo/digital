from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import uvicorn
import uuid

class MyModelInput(BaseModel):
    name: str
    image: UploadFile

app = FastAPI()

@app.post("/predict/")
async def model(inputs: UploadFile = File(...)):
    allowed_extensions = ["jpg", "jpeg", "png"]
    if inputs.filename.split(".")[-1] not in allowed_extensions:
        return {"error": "Invalid file type. Only jpg, jpeg, and png are allowed."}
    input_image = await inputs.read()
    with open(f"{uuid.uuid4()}.jpg", "wb") as f:
        f.write(input_image)

    # preprocess

    #prediction

    return {"prediction": inputs.filename}
    

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)