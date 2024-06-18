from openligadb import Openligadb

api = Openligadb()
result = api.get_match(69351)
print(result.matchDateTime)