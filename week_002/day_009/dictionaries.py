# Dictionaries
dict_methods = {
    "clear": "Removes all items from the dictionary.",
    "copy": "Returns a shallow copy of the dictionary.",
    "fromkeys": "Returns a new dictionary with specified keys and a default value.",
    "get": "Returns the value of the specified key. If the key does not exist, returns a default value.",
    "items": "Returns a view of the dictionary's key-value pairs as tuples.",
    "keys": "Returns a view of the dictionary's keys.",
    "values": "Returns a view of the dictionary's values.",
    "pop": "Removes and returns the value of the specified key. Raises an error if the key is not found.",
    "popitem": "Removes and returns a key-value pair from the dictionary. Raises an error if the dictionary is empty.",
    "setdefault": "Returns the value of the specified key or insert the key with a default value if it doesn't exist.",
    "update": "Updates the dictionary with key-value pairs from another dictionary or an iterable of key-value pairs.",
    "__contains__": "Returns True if the dictionary contains the specified key, else False.",
    "__len__": "Returns the number of items in the dictionary.",
    "__iter__": "Returns an iterator over the keys of the dictionary.",
    "__str__": "Returns a string representation of the dictionary.",
    "__repr__": "Returns a string representation of the dictionary suitable for reproduction using eval().",
}

print(dict_methods['items'])
