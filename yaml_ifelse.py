import yaml
import jinja2

def update_from_globals(updates: list) -> None:
    '''
    Update a block from global vals
    Input: List of dicts as input
           [{'license':'RDFLX=21','H3D'='22'}]
    For each key, see if the key exists in % % 
    Replace with the value of that key
    '''
    pass
YAML_FILE = 'ifelse.yml'
with open(YAML_FILE) as fp:
    dataMap = yaml.safe_load(fp)

env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath='.'))
template = env.get_template(YAML_FILE)
job = yaml.safe_load(template.render(**dataMap))
print(job)
print(job['build']['bcygwin_smp']['command'])

global_updates = []
if 'conditionals' in job:
    for cond in job['conditionals']: # [{'license':{'a'=='a'=21,'a'!='c'=22}},'h3d':{'a'=='a'=14,'a'!='c'=22}]
        # print(cond) #{'license': {'mdl == mdl': 'RDFLX=21', 'mdl != mdl': 'RDFLX=22'}}
        for var in cond: 
            # print(var) #license
            # print(cond[var])
            for chks in list(cond[var].items()):
                if eval(chks[0]):
                    global_updates.append({var:chks[1]})
                    # print(f"{var} = {chks[1]}")
print(global_updates)
print(job['build']['bcygwin_smp']['command'])