from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch([{'host': 'guest', 'port': 9200}])

index_name = "status"
doc_type = "application_status"

def calculate_overall_status():
    try:
        # Query Elasticsearch to retrieve the statuses of all documents
        result = es.search(index=index_name, doc_type=doc_type, size=1000)  # Adjust size as needed

        # Extract the 'service_status' field from each document
        statuses = [doc['_source']['service_status'] for doc in result['hits']['hits']]

        # Calculate the overall status based on the statuses
        overall_status = "UP" if "DOWN" not in statuses else "DOWN"

        return overall_status

    except Exception as e:
        return str(e)

def get_service_status(service_name):
    try:
        # Query Elasticsearch to retrieve the status of the specific service
        query = {
            "query": {
                "term": {
                    "service_name": service_name
                }
            }
        }
        result = es.search(index=index_name, doc_type=doc_type, body=query, size=1)

        # Extract the 'service_status' field from the document
        if result['hits']['total']['value'] > 0:
            service_status = result['hits']['hits'][0]['_source']['service_status']
            return service_status
        else:
            return f"Service {service_name} not found in Elasticsearch"

    except Exception as e:
        return str(e)


@app.route('/add', methods=['POST'])
def add_status_to_elasticsearch():
    try:
        data = request.get_json()
        es.index(index="status", doc_type="application_status", body=data)
        return "Status added to Elasticsearch", 201
    except Exception as e:
        return str(e), 500

@app.route('/healthcheck', methods=['GET'])
def get_overall_health():
    try:
        overall_status = calculate_overall_status()
        return "Overall Application Status: {overall_status}", overall_status
    except Exception as e:
        return str(e), 500

@app.route('/healthcheck/<service_name>', methods=['GET'])
def get_service_health(service_name):
    try:
        service_status = get_service_status(service_name)
        return f"Service {service_name} Status: {service_status}", {service_status}
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run()
