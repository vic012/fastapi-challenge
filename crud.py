from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from fastapi import HTTPException
import models, schemas


# Pegar um video pelo id
def get_video(db: Session, video_id: int):
	video = db.query(models.VideoModel).filter(models.VideoModel.id == video_id).first()
	if not video:
		raise HTTPException(status_code=404, detail=f"video not found for this id: {video_id}")
	return video

# Pegar todos os vídeos
def get_all_video(db: Session):
	return db.query(models.VideoModel).all()

# Criar um vídeo
def create_video(db: Session, video: schemas.VideoBase):
	new_video = models.VideoModel(
		title = video.title,
		description = video.description,
		url = video.url
	)
	db.add(new_video)
	db.commit()
	db.refresh(new_video)
	return new_video

# --Material para pesquisa--
#https://dassum.medium.com/building-rest-apis-using-fastapi-sqlalchemy-uvicorn-8a163ccf3aa1
# Atualizar um vídeo
def update_video(db: Session, video_id: int, video):
	video_stored = db.query(models.VideoModel).filter(models.VideoModel.id == video_id).first()
	if video_stored:
		update_video_encoded = jsonable_encoder(video)
		video_stored.title = update_video_encoded["title"]
		video_stored.description = update_video_encoded["description"]
		video_stored.url = update_video_encoded["url"]
		updated_video = db.merge(video_stored)
		db.commit()
		return updated_video
	raise HTTPException(status_code=404, detail=f"video not found for this id: {video_id}")

# Deletar um vídeo
def delete_video(db: Session, video_id: int):
	video = get_video(db=db, video_id=video_id)
	if video:
		db.delete(video)
		db.commit()
		return {"detail": f"The video: {video} was successfully deleted!"}
