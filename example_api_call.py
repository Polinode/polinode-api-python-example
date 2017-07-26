import requests
import pprint
import json

username = '' #Your Public Key here. Replace with an environment variable before committing or using in production.
password = '' #Your Private Key here. Replace with an environment variable before committing or using in production.

exampleNetworkData = {
	'nodes':[
		{
			'id': 'Joe',
			'attributes':
			{
				'Example Numerical Attribute Name': 24,
				'Example Categorical Attribute Name': 'Value 1',
				'Name': 'Joe'
			}
		},
		{
			'id':'Mary',
			'attributes':
			{
				'Example Numerical Attribute Name':38,
				'Example Categorical Attribute Name':'Value 1',
				'Name':'Mary'
			}
		},
		{
			'id':'Bill',
			'attributes':
			{
				'Example Numerical Attribute Name':65,
				'Example Categorical Attribute Name':'Value 2',
				'Name':'Bill'
			}
		},
		{
			'id':'Grant',
			'attributes':
			{
				'Example Numerical Attribute Name':52,
				'Example Categorical Attribute Name':'Value 2',
				'Name':'Grant'
			}
		}
	],
	'edges':[
		{
			'id':0,
			'source':'Joe',
			'target':'Mary',
			'attributes':
			{
				'Example Numerical Attribute Name':30,
				'Example Categorical Attribute Name':'Value 1'
			}
		},
		{
			'id':1,
			'source':'Grant',
			'target':'Mary',
			'attributes':
			{
				'Example Numerical Attribute Name':34,
				'Example Categorical Attribute Name':'Value 1'
			}
		},
		{
			'id':2,
			'source':'Bill',
			'target':'Joe',
			'attributes':
			{
				'Example Numerical Attribute Name':38,
				'Example Categorical Attribute Name':'Value 2'
			}
		}
	]
}

#Create a network
r = requests.post('https://wwww.polinode.com/api/v2/networks', auth=(username, password), json = {'name': 'My new network', 'networkJSON': exampleNetworkData, 'status': 'Public', 'fileType': 'JSON', 'originalFileType': 'JSON', 'isDirected': 'true', 'description': 'An example network created via the Polinode API'}) #name is required, networkJSON is required, status is optinal and defaults to public, fileType is optional and defaults to JSON, originalFileType is optional and defaults to Excel, isDirected is optional and defaults to true, description is optional and defautls to no description.
network = r.json()
networkId = network['_id']
print('Summary of network created:')
pprint.pprint(network, indent=2)

#Edit the network we just created. We will change the name of the network and change one attribute value
exampleNetworkData['nodes'][0]['attributes']['Example Numerical Attribute Name'] = 25;
r = requests.put('https://wwww.polinode.com/api/v2/networks/' + networkId, auth=(username, password), json = {'name': 'My new network after edits', 'networkJSON': exampleNetworkData})
network = r.json()
print('Summary of updated network:')
pprint.pprint(network, indent=2)

#Example of retrieving a summary of all networks for a user
r = requests.get('https://wwww.polinode.com/api/v2/networks', auth=(username, password))
networks = r.json()
print('Summary of networks')
pprint.pprint(networks, indent=2)

#Example of retrieving a specific network for a user. Authentication is not required for this action if this is a public network.
r = requests.get('https://wwww.polinode.com/api/v2/networks/' + networkId, auth=(username, password))
network = r.json()
print('Summary for a single network')
pprint.pprint(network, indent=2)

#Delete the network that we created. Comment this section out to not delete the created network, i.e. to view it in the application
r = requests.delete('https://wwww.polinode.com/api/v2/networks/' + networkId, auth=(username, password))
network = r.json()
print('Network deleted')
pprint.pprint(network, indent=2)