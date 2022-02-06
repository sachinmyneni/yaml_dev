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

if 'conditionals' in job:
    for cond in job['conditionals']: # [{'license':{'a'=='a'=21,'a'!='c'=22}},'h3d':{'a'=='a'=14,'a'!='c'=22}]
        print(cond) #{'license': {'mdl == mdl': 'RDFLX=21', 'mdl != mdl': 'RDFLX=22'}}
        for var in cond: 
            print(var) #license
            print(cond[var])
            for chks in list(cond[var].items()):
                if eval(chks[0]):
                    print(f"{var} = {chks[1]}")

            # for key in list(job['conditionals'][cond][items].keys()):
            #     print(key) # l i c e n s e 
