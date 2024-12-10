from wolframalpha import Client
import settings
from functools import lru_cache

@lru_cache
def stem_answers(question):
    app_id=settings.wolframalpha_id
    client=Client(app_id)
    try:
      res=client.query(question)
      res = next(res.results).text
      return res
    except:
      print("Error; The Database is Not Functioning Properly. Please Check your Internet Connection!")
      return None