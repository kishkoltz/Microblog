from whoosh.index import create_in
import whoosh.index as index
from whoosh.fields import *
from whoosh.qparser import QueryParser

ix = index.open_dir("index")
writer = ix.writer()

def add_to_index(model):
    #body = __searchable__
    payload = {}
    for field in model.__searchable__:
        payload[field] = getattr(model, field)
    writer.add_document(id=model.id, body=payload)
    writer.commit()
    
#def query_index():
    #https://whoosh.readthedocs.io/en/latest/searching.html
