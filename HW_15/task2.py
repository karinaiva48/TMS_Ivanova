from peewee import *

db = SqliteDatabase('chinook.db')

class BaseModel(Model):
    class Meta:
        database = db

class Albums(BaseModel):
    title = CharField(column_name='Title')
    album_id = AutoField(column_name='AlbumId')

    class Meta:
        table_name = 'albums'

class Track(BaseModel):
    name = CharField(column_name='Name')
    album_id = AutoField(column_name='AlbumId')

    class Meta:
        table_name = 'tracks'


def get(album_name_from_input):
    with db:
        tracks = Track.select().where(Track.album_id == Albums.select().where(Albums.title == album_name_from_input))
        print(tracks)
    return tracks

tracks_list = input('Введите название альбома:')
print([track.name for track in list(get(tracks_list))])

