import more_itertools as mit

from lxml import etree


def find_password(xml_string):
    return search_element(etree.fromstring(xml_string))


def search_element(item: etree.ElementTree) -> str:
    return item.get('password') or mit.first_true((search_element(child) for child in item), None)
