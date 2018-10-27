import os
import yaml
import requests
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def import_variables_from_file():
    my_variables_file=open('variables.yml', 'r')
    my_variables_in_string=my_variables_file.read()
    my_variables_in_yaml=yaml.load(my_variables_in_string)
    my_variables_file.close()
    return my_variables_in_yaml

def get_file(file_name):
    print table
    r=requests.get(url + '/files/helper-files/' + file_name, auth=HTTPBasicAuth(authuser, authpwd), headers={ 'Accept' : 'application/json', 'Content-Type': 'multipart/form-data' }, verify=False)
    print r.content
    return r.status_code

def commit():
    r = requests.post(url + '/configuration', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
    print 'healthbot configuration commited!'
    return r.status_code


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

my_variables_in_yaml=import_variables_from_file()
server = my_variables_in_yaml['server']
authuser = my_variables_in_yaml['authuser']
authpwd = my_variables_in_yaml['authpwd']
url = 'https://'+ server + ':8080/api/v1'
headers = { 'Accept' : 'application/json', 'Content-Type' : 'application/json' }

rules_list=os.listdir('rules')
playbooks_list=os.listdir('playbooks')
tables_and_views_list=os.listdir('tables_and_views')

print '**************** auditing tables and views ************************'

for table in tables_and_views_list: 
    get_file(table)

print '**************** auditing rules ************************'

for rule in rules_list:
    get_file(rule)

print '**************** auditing playbooks ************************'

for playbook in playbooks_list: 
    get_file(playbook)



