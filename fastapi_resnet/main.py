import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile
from eval import MyNet


app = FastAPI()
my_net = MyNet()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"AppStatus": "Running"}


@app.post("/predict")
async def create_upload_file(file: UploadFile):
    image = await file.read()
    result = my_net.predict(image)
    return {"prediction": result}
