def dict_structure(json_data):
	'''	
		This function prints the hierachical structure of dictionary
		Just the structure not including the values

		Example:
		data = {
		    'count': 3,
		    'data':{
		        'x': [1,2,3],
		        'y': [4,5,6],
		        'z': [7,8,9]
		    },
		    'source': 'wiki'
		}

		dict_structure(data)

		Printed Result:
		 - count
		 - data
			 - x
			 - y
			 - z
		 - source
	'''

    def scan(data, level):
        if not isinstance(data, dict):
            return
        indent = '\t' * level
        keys = list(data.keys())
        for key in keys:
            print('{} - {}'.format(indent, key))
            scan(data[key], level + 1)