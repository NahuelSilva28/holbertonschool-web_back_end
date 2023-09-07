#!/usr/bin/env python3
"""
Log stats for Nginx logs in MongoDB.
"""

from pymongo import MongoClient


def log_stats(mongo_collection):
    """_summary_

    Args:
        mongo_collection (_type_): _description_
    """
    #number of logs
    total_logs = mongo_collection.count_documents({})

    #methods
    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: mongo_collection.count_documents({"method": method}) for method in http_methods}

    #logs
    status_check_count = mongo_collection.count_documents({"method": "GET", "path": "/status"})

    #results
    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")
    print(f"{status_check_count} status check")
