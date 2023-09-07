#!/usr/bin/env python3
"""Log stats for Nginx logs in MongoDB."""

from pymongo import MongoClient

if __name__ == "__main__":

    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    #total logs
    n_logs = nginx_collection.count_documents({})
    
    #methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: nginx_collection.count_documents({"method": method}) for method in methods}

    #status checks
    status_check = nginx_collection.count_documents({"method": "GET", "path": "/status"})

    #stats
    print(f"Collection nginx with {n_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tMethod {method}: {count} logs")
    print(f"Status checks: {status_check} logs")
