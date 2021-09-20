import pebble_pb2
import numpy as np
import requests

def run_query(q):
    request = requests.post('http://34.146.117.200:8000/subgraphs/name/iotex/pebble-subgraph'
                            '',
                            json={'query': q})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Query failed with return code: {}'.format(request.status_code))