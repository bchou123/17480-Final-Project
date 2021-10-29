from musixmatch import Musixmatch
import json

API_KEY = "597150546acd7bbc5f133deb9b22eaec"
RESPONSE = """{
  "message": {
    "header": {
      "status_code": 200,
      "execute_time": 0.093447923660278
    },
    "body": {
      "artist_list": [
        {
          "artist": {
            "artist_id": 13916103,
            "artist_mbid": "",
            "artist_name": "Maroon 5 feat. Wiz Khalifa",
            "artist_alias_list": [

            ],
            "artist_rating": 81,
            "updated_time": "2012-04-17T10:22:35Z"
          }
        },
        {
          "artist": {
            "artist_id": 13639930,
            "artist_mbid": "ec6eaf55-d743-46ce-89b6-014943a2773c",
            "artist_name": "Emma",
            "artist_alias_list": [

            ],
            "artist_rating": 66,
            "updated_time": "2011-06-03T09:43:10Z"
          }
        },
        {
          "artist": {
            "artist_id": 13834953,
            "artist_mbid": "",
            "artist_name": "Gotye feat. Kimbra",
            "artist_alias_list": [

            ],
            "artist_rating": 84,
            "updated_time": "2012-04-07T18:22:16Z"
          }
        }
      ]
    }
  }
 }"""

musixmatch = Musixmatch(API_KEY)

class Artist():
  """Basic Artist class"""

  def __init__(self, id, mbid, name, alias_list, rating, updated_time, country=None, twitter_url=None):
    self._id = id
    self._mbid = mbid
    self._name = name
    self._country = country
    self._alias_list = alias_list
    self._rating = rating
    self._twitter_url = twitter_url
    self._updated_time = updated_time

  def get_id(self):
    return self._id

  def get_name(self):
    return self._name

  def get_mbid(self):
    return self._mbid

  def get_country(self):
    if not self._country:
      _load_all()
    return self._country

  def get_alias_list(self):
    return self._alias_list

  def get_rating(self):
    return self._rating

  def get_twitter_url(self):
    if not self._twitter_url:
      _load_all()
    return self._twitter_url

  def get_updated_time(self):
    return self._updated_time

  def _load_all(self):
    """queries musixmatch to get all the artist information"""
    pass

def get_top_n_us_artists(n):
  """ Returns the top N artists in a List[Artist]"""
  res = []
  # response = RESPONSE
  j = musixmatch.chart_artists(1, n)
  print(j)
  return
  # j = json.loads(response)
  artists = list(j["message"]["body"]["artist_list"])

  for artist_d in artists:
    artist = artist_d["artist"]
    res.append(Artist(id=artist["artist_id"], mbid=artist["artist_mbid"], name=artist["artist_name"],
    alias_list=artist["artist_alias_list"], rating=artist["artist_rating"], updated_time=artist["updated_time"]))

  return res

def main():
  """Gets the top N US artists and sorts by rating"""

  L = get_top_n_us_artists(1)
  # L.sort(key= lambda x: x.get_rating())
  # for elem in L:
  #   print(elem.get_name())
  #   print(elem.get_rating())

if __name__ == '__main__':
  main()

