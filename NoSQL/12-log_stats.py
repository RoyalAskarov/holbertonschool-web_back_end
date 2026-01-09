#!/usr/bin/env python3
""" Module that provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient


def log_stats():
    """ Provides stats about Nginx logs in MongoDB """
    client = MongoClient('mongodb://127.0.0.1:27017')
    # Use the logs database and nginx collection as required
    nginx_collection = client.logs.nginx

    # Get total logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # Get method counts in the specific order required
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        # Note the tab character (\t) before 'method'
        print(f"\tmethod {method}: {count}")

    # Get status check count (method=GET, path=/status)
    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()