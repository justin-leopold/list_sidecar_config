import requests
import json

sidecars_url = "http://graylogserver.company.org/api/sidecars/all"

sidecars_payload = {}
sidecars_headers = {
    'Authorization': 'Basic key here'
}

sidecars = requests.request(
    "GET", sidecars_url, headers=sidecars_headers, data=sidecars_payload)

sidecars_dict = json.loads(sidecars.text)

print(sidecars_dict['sidecars'][0]['node_name'])
    

nodes = []
count = 0
for key in sidecars_dict['sidecars']:
    node_name = (key['node_name'])
    node_id = (key['node_id'])
    assignments = (key['assignments'])
    filtered_data_info = {
        "Node Name": node_name,
        "Node ID": node_id,
        "Assignments": assignments
    }
    nodes.append(filtered_data_info)


# check the config

for node in nodes:
    try:
        configuration_id = (node['Assignments'][0]['configuration_id'])
    except:
        print(node['Node Name'] + ' has no assignment')
    if configuration_id is None:
        node_name = node['Node Name']
        #print('No collector assigned to ' + node_name)
    elif configuration_id == 0:
        print('invalid value')
    else:
        configuration_url = "http://graylogserver.company.com:80/api/sidecar/configurations/" + configuration_id

        configuration_payload = {}
        configuration_headers = {
            'Authorization': 'Basic key here'
        }

        node_configuration = requests.request(
            "GET", configuration_url, headers=configuration_headers, data=configuration_payload)

        sidecar_config_dict = json.loads(node_configuration.text)
        print(sidecar_config_dict['name'] +
              ' is assigned to ' + node['Node Name'])

print('Run is complete!')
