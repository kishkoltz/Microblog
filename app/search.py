from whoosh.index import create_in
import whoosh.index as index
from whoosh.fields import *
from whoosh.qparser import QueryParser

ix = index.open_dir("index")


def add_to_index(model):
    #body = __searchable__
    #payload = {}
    #for field in model.__searchable__:
    #    payload[field] = getattr(model, field)
    writer = ix.writer()
    writer.add_document(id=str(model.id), body=model.body)
    writer.commit()
    
def query_index(query, page, per_page):
    q = QueryParser('body', ix.schema).parse(query)
    with ix.searcher() as searcher:
        results = searcher.search_page(q, page, pagelen=per_page)
        
        #ids = [int(hit['_id']) for hit in search['hits']['hits']]
    #return ids, search['hits']['total']
        ids = [int(result['id']) for result in results[:]]
        return ids, len(results)
        #for result in results[:]:
        #    print(result['id'])
        #print(results[:], len(results))
    
'''    
>>> from app.search import *
>>> for post in Post.query.all():
...     add_to_index(post)
... 
>>> query_index("hello", 1, 5)
[<Hit {'id': '3'}>, <Hit {'id': '4'}>] 2   
'''    
#https://whoosh.readthedocs.io/en/latest/searching.html
