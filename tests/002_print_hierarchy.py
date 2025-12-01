import os
import argparse
import pathlib
import xml.etree.ElementTree as ET

from setting import setting

DOC_PATH = setting.DATASETS_PATH / pathlib.Path("documentation/categories-july30.xml")

def load_tree():
    return ET.parse(DOC_PATH)

def get_categories(root):
    ns = {'ns': 'http://www.w3schools.com'}
    return root.findall('ns:category', ns)

def text(elem, tag, ns):
    t = elem.find(f'ns:{tag}', ns)
    return t.text.strip() if t is not None and t.text else ''

def print_hierarchy(filter_term=None):
    tree = load_tree()
    root = tree.getroot()
    ns = {'ns': 'http://www.w3schools.com'}
    for cat in get_categories(root):
        name = text(cat, 'name', ns)
        if filter_term and filter_term.lower() not in name.lower():
            continue
        print(name)
        attrs = cat.find('ns:attributes', ns)
        if attrs is None:
            continue
        for attr in attrs.findall('ns:attribute', ns):
            aname = text(attr, 'name', ns)
            opt = attr.get('optional', 'false')
            default = attr.get('default')
            status = 'optional' if opt == 'true' else 'required'
            line = f"  - {aname} ({status}"
            if default:
                line += f", default={default}"
            line += ")"
            print(line)
            values = attr.find('ns:values', ns)
            if values is not None:
                for v in values.findall('ns:value', ns):
                    vname = text(v, 'name', ns)
                    print(f"    * {vname}")


print_hierarchy()
