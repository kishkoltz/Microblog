from whoosh.index import create_in
import whoosh.index as index
from whoosh.fields import *
from whoosh.qparser import QueryParser

ix = index.open_dir("index")


def add_to_index(model):
    writer = ix.writer()
    writer.add_document(id=str(model.id), body=model.body)
    writer.commit()
    
def query_index(query, page, per_page):
    q = QueryParser('body', ix.schema).parse(query)
    with ix.searcher() as searcher:
        results = searcher.search_page(q, page, pagelen=per_page)
        ids = [int(result['id']) for result in results[:]]
        return ids, len(results)
