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
r = requests.post('https://www.polinode.com/api/v1/networks', auth=(username, password), data = {'name': 'My new network', 'status': 'Public', 'isDirected': 'true', 'description': 'An example network created via the Polinode API'}) #name is required, status is optinal and defaults to public, isDirected is optional and defaults to true, description is optional and defautls to no description.
network = r.json()
networkId = network['_id']
print('Summary of network created:')
pprint.pprint(network, indent=2)
r = requests.put(network['AWSURL'], data=json.dumps(exampleNetworkData), headers={'Content-Type': 'application/json; charset=UTF-8'})

#Edit the network we just created. We will change the name of the network and change one attribute value
r = requests.put('https://www.polinode.com/api/v1/networks/' + networkId, auth=(username, password), data = {'name': 'My new network after edits'})
network = r.json()
print('Summary of updated network:')
pprint.pprint(network, indent=2)
exampleNetworkData['nodes'][0]['attributes']['Example Numerical Attribute Name'] = 25;
r = requests.put(network['AWSURL'], data=json.dumps(exampleNetworkData), headers={'Content-Type': 'application/json; charset=UTF-8'})

#Example of retrieving a summary of all networks for a user
r = requests.get('https://www.polinode.com/api/v1/networks', auth=(username, password))
networks = r.json()
print('Summary of networks')
pprint.pprint(networks, indent=2)

#Example of retrieving a specific network for a user. Authentication is not required for this action if this is a public network.
r = requests.get('https://www.polinode.com/api/v1/networks/' + networkId, auth=(username, password))
network = r.json()
print('Summary for a single network')
pprint.pprint(network, indent=2)
#Retrieve actual network data
r = requests.get(network['AWSURL'])
networkData = r.json();
print('Actual network data')
pprint.pprint(networkData, indent=2)

#Delete the network that we created. Comment this section out to not delete the created network, i.e. to view it in the application
r = requests.delete('https://www.polinode.com/api/v1/networks/' + networkId, auth=(username, password))
network = r.json()
print('Network deleted')
pprint.pprint(network, indent=2)