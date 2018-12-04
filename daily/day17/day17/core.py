def isiterable(obj):
    # TODO: ドキュメンテーションを記述
    return hasattr(obj, "index")

def isiterator(obj):
    # TODO: ドキュメンテーションを記述
    return hasattr(obj, "__next__")

def ishashable(obj):
    # TODO: ドキュメンテーションを記述
    try:
        hash(obj)
        return True
    except TypeError:
        return False
