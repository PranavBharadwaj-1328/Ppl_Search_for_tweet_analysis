from elasticsearch import Elasticsearch
def search(S):
    es = Elasticsearch()
    res = es.search(index="ppl_data_index",body={"from":0,"size":10,"query":{"match":{"name":{"query": S,"fuzziness":"AUTO","operator":"or"}}}})
    for hit in res['hits']['hits']:
        print(hit["_source"])

