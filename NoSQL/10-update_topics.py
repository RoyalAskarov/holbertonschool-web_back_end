#!/usr/bin/env python3
""" Module that provides a function to update topics in a collection """


def update_topics(mongo_collection, name, topics):
    """ Changes all topics of a school document based on the name """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})