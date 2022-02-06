import yaml
import jinja2

with open('ifelse.yml') as fp:
    dataMap = yaml.safe_load(fp)

# print(dataMap)
print(dataMap['branch'])