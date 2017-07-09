import json
import os
import random
import string


def generate_token(length=40):
    list_chars = string.ascii_uppercase + string.digits
    letters = [random.choice(list_chars) for _ in range(length)]
    return ''.join(letters)


def force_rm(filename):
    try:
        os.remove(filename)
    except OSError:
        pass


def ordered(obj):
    """
    Deeply sort dictionary
    """
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj


def compare_json_file(f1, f2):
    """
    Return True if they are equal
    """
    with open(f1) as json_f:
        a = json.loads(json_f.read())
    with open(f2) as json_f:
        b = json.loads(json_f.read())
    return ordered(a) == ordered(b)
