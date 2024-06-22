import requests



class Essence:
	def __init__(self) -> None:
		pass

	def get_essences_info(self):
		url = "https://poe.ninja/api/data/itemoverview?league=Necropolis&type=Essence"

		response = requests.get(url)

		return response.json()['lines']

	def filter_tier(self):
		data = self.get_essences_info()
		filterEssences = {}
		filterEssences['Whispering'] = []
		filterEssences['Muttering'] = []
		filterEssences['Weeping'] = []
		filterEssences['Wailing'] = []
		filterEssences['Screaming'] = []
		filterEssences['Shrieking'] = []
		filterEssences['Deafening'] = []
		filterEssences['Special'] = []
		for i in data:
			if 'Whispering' in i['name']:
				filterEssences['Whispering'].append({'name': i['name'], 'tier': 7,'icon': i['icon'], 'chaosValue': i['chaosValue'], 'exaltedValue': i['exaltedValue'], 'divineValue': i['divineValue']})
			elif 'Muttering' in i['name']:
				filterEssences['Muttering'].append({'name': i['name'], 'tier': 6,'icon': i['icon'], 'chaosValue': i['chaosValue'], 'exaltedValue': i['exaltedValue'], 'divineValue': i['divineValue']})
			elif 'Weeping' in i['name']:
				filterEssences['Weeping'].append({'name': i['name'], 'tier': 5,'icon': i['icon'], 'chaosValue': i['chaosValue'], 'exaltedValue': i['exaltedValue'], 'divineValue': i['divineValue']})
			elif 'Wailing' in i['name']:
				filterEssences['Wailing'].append({'name': i['name'], 'tier': 4,'icon': i['icon'], 'chaosValue': i['chaosValue'], 'exaltedValue': i['exaltedValue'], 'divineValue': i['divineValue']})
			elif 'Screaming' in i['name']:
				filterEssences['Screaming'].append({'name': i['name'], 'tier': 3,'icon': i['icon'], 'chaosValue': i['chaosValue'], 'exaltedValue': i['exaltedValue'], 'divineValue': i['divineValue']})
			elif 'Shrieking' in i['name']:
				filterEssences['Shrieking'].append({'name': i['name'], 'tier': 2,'icon': i['icon'], 'chaosValue': i['chaosValue'], 'exaltedValue': i['exaltedValue'], 'divineValue': i['divineValue']})
			elif 'Deafening' in i['name']:
				filterEssences['Deafening'].append({'name': i['name'], 'tier': 1,'icon': i['icon'], 'chaosValue': i['chaosValue'], 'exaltedValue': i['exaltedValue'], 'divineValue': i['divineValue']})
			elif 'Corruption' in i['name']:
				pass
			else :
				filterEssences['Special'].append({'name': i['name'], 'tier': 0,'icon': i['icon'], 'chaosValue': i['chaosValue'], 'exaltedValue': i['exaltedValue'], 'divineValue': i['divineValue']})
		
		# Lista na ordem desejada
		ordem_desejada = ["Essence of Insanity", "Essence of Horror", "Essence of Delirium", "Essence of Hysteria"]

		# Ordenar a lista de dicionários com base na ordem desejada
		filterEssences['Special'] = sorted(filterEssences['Special'], key=lambda x: ordem_desejada.index(x['name']))
				
		
		return filterEssences


	def filter_essence_type(self):
		filterEssences = self.filter_tier()
		
		essTiers = {}
		essTiers['Greed'] = []
		essTiers['Contempt'] = []
		essTiers['Hatred'] = []
		essTiers['Woe'] = []
		essTiers['Fear'] = []
		essTiers['Anger'] = []
		essTiers['Torment'] = []
		essTiers['Sorrow'] = []
		essTiers['Rage'] = []
		essTiers['Suffering'] = []
		essTiers['Wrath'] = []
		essTiers['Doubt'] = []
		essTiers['Loathing'] = []
		essTiers['Zeal'] = []
		essTiers['Anguish'] = []
		essTiers['Spite'] = []
		essTiers['Scorn'] = []
		essTiers['Envy'] = []
		essTiers['Misery'] = []
		essTiers['Dread'] = []
		essTiers['Special'] = filterEssences['Special']
		for i in essTiers.keys():
			for j in filterEssences.keys():
				for k in filterEssences[j]:
					if i in k['name']:
						essTiers[i].append(k)
		return essTiers
	

def essence():
	essence = Essence()

	essenceItens = essence.filter_essence_type()

	return essenceItens