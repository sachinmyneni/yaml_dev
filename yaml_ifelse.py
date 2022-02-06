import yaml
import jinja2

YAML_FILE = 'ifelse.yml'
with open(YAML_FILE) as fp:
    dataMap = yaml.safe_load(fp)

env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath='.'))
template = env.get_template(YAML_FILE)
job = yaml.safe_load(template.render(**dataMap))
print(job)
print(job['build']['bcygwin_smp']['command'])