import yaml


apis = yaml.load(open("../doc/api-1.yml"))

for api in apis['apis']:
    print "%s %s %s\n" % (api['title'], api['method'], api['url'])
