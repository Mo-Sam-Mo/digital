from fastapi import FastAPI, UploadFile, File
from model import predict as model_predict
import uvicorn

app = FastAPI()

@app.get("/")
async def home():
    return {"message": """
            This is our main api, you can call any one of the following endpoints:
            1. /predict/ - This endpoint accepts an image file (jpg, jpeg, png) and returns the prediction result.
            """}

@app.post("/predict/")
async def predict(input_image: UploadFile = File(...)):
    allowed_extensions = ["jpg", "jpeg", "png"]
    if input_image.filename.split(".")[-1] not in allowed_extensions:
        return {"error": "Invalid file type. Only jpg, jpeg, and png are allowed."}
    image_bytes = await input_image.read()

    prediction = model_predict(image_bytes)

    return {"prediction": prediction}

if __name__ == "__main__":
    uvicorn.run("app2:app", host="0.0.0.0", port=8000, reload=True)