#!/usr/bin/env python3
"""Return the list of schools"""

def schools_by_topic(mongo_collection, topic):
    """Return a list of schools with a specific topic."""
    schools = mongo_collection.find({"topics": topic})
    return list(schools)
