import yaml
import re
from glusterfsrest.api import apilist

TAB = "^\s\s\s\s"
docs = []


for func in apilist:
    lines = func.__doc__.strip().split("\n")
    docs.append(yaml.load("\n".join([re.sub(TAB, "", l) for l in lines])))


def api_template(doc):
    template = """
    <h2>
    """
    return template

for doc in docs:
    print "%s /api/1/%s" % (doc["method"], doc["url"])
