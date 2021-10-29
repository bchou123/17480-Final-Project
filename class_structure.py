class MusixMatch():
  def __init__(self):
    pass

  def search_artists(self) -> ArtistList:
    pass

  def search_tracks(self) -> TrackList:
    pass

  def get_chart_artists(self):
    pass

  def get_chart_track(self):
    pass

  def get_track(self):
    pass

  def get_artist(self):
    pass

  def get_genres(self):
    pass

  def get_genre_by_name(self, name):
    """additional"""
    pass

[].sort(key= lambda x: x.get_name())

L = search_tracks(...).sort_by(name)
L = search_tracks(...).sort_by(rating)

L.sort(key= lambda x: x.get_rating)





class TrackList():
  def sort_by(self):
    pass

  def filter_by(self):
    pass


class Artist():
  def get_album(self):
    pass

  def get_related_artists(self):
    pass

class Track():
  def __init__(self, lyric_id):
    self.lyrics = Lyric(lyric_id)
  def get_lyrics(self):
    pass

  def get_snippet(self):
    pass

  def get_rich_sync(self):
    pass

  def upload_lyrics(self):
    pass

  def upload_feedback(self):
    pass

  def get_lyrics(self):
    pass

class Album():
  def get_tracks(self):
    pass

class Lyric():
  def __init__(self, id, track_id):
    self.track = track_id
    pass

  def get_mood(self):
    pass

  def get_language(self):
    pass


class Query():
  def sort(self):
    pass

  def filter(self):
    pass

  def to_list()

L1 = list(q.filter().to_iter())