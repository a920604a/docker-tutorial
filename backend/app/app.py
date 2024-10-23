from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io
from app.algo import detect_faces
from app.models import save_to_db, Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)


origins = [
    "http://localhost:3001",      # 其他可以允許的來源
    "http://frontend:3001",  # 使用服務名稱作為來源
    # "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/upload")
async def upload_image(file: UploadFile = File(...)):
    print('upload_image')
    image = Image.open(io.BytesIO(await file.read()))
    # 進行人臉偵測分析
    analysis, processed_image = detect_faces(image)
    
    # 儲存圖片和分析結果到資料庫
    save_to_db(file.filename, analysis)
    
    # 回傳處理後圖片和分析結果
    return {"processedImage": processed_image, "analysis": analysis}
