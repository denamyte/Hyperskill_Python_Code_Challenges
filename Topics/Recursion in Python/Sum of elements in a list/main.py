def list_sum(ls):
    return ls[0] + list_sum(ls[1:]) if len(ls) > 0 else 0
