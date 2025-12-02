from fastapi import File, UploadFile, APIRouter,Depends
import cloudinary.uploader
from sqlalchemy.orm import Session
from src.shared.services.cloudinary import config

from src.db.session import get_db_service
from src.shared.exceptions import CustomException
from src.shared.services.cloudinary.fileservice import FileService
from src.shared.services.cloudinary.image_model import Image
from src.shared.services.db_service import DatabaseService

irouter = APIRouter()

@irouter.post("/upload")
async def upload_image(file: UploadFile = File(...), db: DatabaseService = Depends(get_db_service)):
    try:
        # upload to cloudinary
        contents = await file.read() # await here because it is async
        result = FileService.upload(contents)
        if result:
            #save to db
            image = Image(url=result["url"],public_id= result["public_id"]) # type: ignore
            await db.create(image)
            return {"id":image.id,"url":image.url,"originalurl": result["url"]} # type: ignore
    except Exception as e:
        raise CustomException(
            dev_message=f"Image failed and  reported as: \n{e}",
            user_message="Failed to upload image",
            status_code= 500,
        )