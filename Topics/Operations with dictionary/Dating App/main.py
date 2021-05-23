def match(record):
    return record['age'] > 30 and 'art' in record['hobbies'] and record['city'] == 'Berlin'


def select_dates(potential_dates):
    return ', '.join(record['name'] for record in potential_dates if match(record))
