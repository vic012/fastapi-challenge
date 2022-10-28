from sqlalchemy import Column, Integer, String
from database import Base


class VideoModel(Base):
	__tablename__ = "videos"

	id = Column(Integer, primary_key=True, index=True)
	title = Column(String, index=True)
	description = Column(String, index=True)
	url = Column(String, index=True)

	def __repr__(self):
		return f'Video {self.title}'