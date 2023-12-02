from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Playlist(Base):
    __tablename__ = 'playlist'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class PlaylistTrack(Base):
    __tablename__ = 'playlist_track'
    id = Column(Integer, primary_key=True)
    playlist_id = Column(Integer, ForeignKey('playlist.id'))
    track_id = Column(Integer, ForeignKey('track.id'))

class Track(Base):
    __tablename__ = 'track'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    artist = Column(String)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

engine = create_engine('sqlite:///mydatabase.db')
Session = sessionmaker(bind=engine)
