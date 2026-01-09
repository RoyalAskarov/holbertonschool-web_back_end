#!/usr/bin/env python3
""" Module that provides a function to find documents by a specific topic """


def schools_by_topic(mongo_collection, topic):
    """ Returns the list of schools having a specific topic """
    return list(mongo_collection.find({"topics": topic}))