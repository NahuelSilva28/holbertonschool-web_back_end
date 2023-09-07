#!/usr/bin/env python3
"""Change school topics in a MongoDB collection."""

def update_topics(mongo_collection, name, topics):
    """Update the topics of a school document by name."""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
