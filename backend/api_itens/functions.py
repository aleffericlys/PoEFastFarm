import requests



class Essences:
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

		filtro = {}
		for i in data:
			if "Shrieking" in i['name'] or "Deafening" in i['name']:
				filtro[i['name']] = {'chaosValue': i['chaosValue'], 'divineValue': i['divineValue']}
		
		bases = ['Contempt', 'Wrath', 'Anger', 'Hatred', 'Loathing', 'Envy', 'Spite', 'Rage', 'Zeal', 'Fear', 'Greed', 'Scorn', 'Dread', 'Sorrow', 'Torment', 'Woe', 'Anguish', 'Doubt', 'Misery', 'Suffering']

		canUP= []
		for i in bases:
			if filtro[f'Deafening Essence of {i}']['chaosValue']/3 >= filtro[f'Shrieking Essence of {i}']['chaosValue']:
				canUP.append(f'Shrieking Essence of {i}')




		for i in data:
			if 'Whispering' in i['name']:
				filterEssences['Whispering'].append({'name': i['name'], 'tier': 7,'icon': i['icon'], 'chaosValue': i['chaosValue'], 'exaltedValue': i['exaltedValue'], 'divineValue': i['divineValue'], "canUP": 1 if i['name'] in canUP else 0})
			elif 'Muttering' in i['name']:
				filterEssences['Muttering'].append({'name': i['name'], 'tier': 6,'icon': i['icon'], 'chaosValue': i['chaosValue'], 'exaltedValue': i['exaltedValue'], 'divineValue': i['divineValue'], "canUP": 1 if i['name'] in canUP else 0})
			elif 'Weeping' in i['name']:
				filterEssences['Weeping'].append({'name': i['name'], 'tier': 5,'icon': i['icon'], 'chaosValue': i['chaosValue'], 'exaltedValue': i['exaltedValue'], 'divineValue': i['divineValue'], "canUP": 1 if i['name'] in canUP else 0})
			elif 'Wailing' in i['name']:
				filterEssences['Wailing'].append({'name': i['name'], 'tier': 4,'icon': i['icon'], 'chaosValue': i['chaosValue'], 'exaltedValue': i['exaltedValue'], 'divineValue': i['divineValue'], "canUP": 1 if i['name'] in canUP else 0})
			elif 'Screaming' in i['name']:
				filterEssences['Screaming'].append({'name': i['name'], 'tier': 3,'icon': i['icon'], 'chaosValue': i['chaosValue'], 'exaltedValue': i['exaltedValue'], 'divineValue': i['divineValue'], "canUP": 1 if i['name'] in canUP else 0})
			elif 'Shrieking' in i['name']:
				filterEssences['Shrieking'].append({'name': i['name'], 'tier': 2,'icon': i['icon'], 'chaosValue': i['chaosValue'], 'exaltedValue': i['exaltedValue'], 'divineValue': i['divineValue'], "canUP": 1 if i['name'] in canUP else 0})
			elif 'Deafening' in i['name']:
				filterEssences['Deafening'].append({'name': i['name'], 'tier': 1,'icon': i['icon'], 'chaosValue': i['chaosValue'], 'exaltedValue': i['exaltedValue'], 'divineValue': i['divineValue'], "canUP": 1 if i['name'] in canUP else 0})
			elif 'Corruption' in i['name']:
				pass
			else :
				filterEssences['Special'].append({'name': i['name'], 'tier': 0,'icon': i['icon'], 'chaosValue': i['chaosValue'], 'exaltedValue': i['exaltedValue'], 'divineValue': i['divineValue'], "canUP": 1 if i['name'] in canUP else 0})
		
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
	essence = Essences()

	essenceItens = essence.filter_essence_type()

	return essenceItens


class Oils:
	def __init__(self) -> None:
		pass


	def get_oils_info(self):
		url = "https://poe.ninja/api/data/itemoverview?league=Necropolis&type=Oil"

		response = requests.get(url)

		return response.json()['lines']
	
	def update_oils(self):
		oils = self.get_oils_info()[::-1]
		for oil in oils:
			if oil['name'] == "Reflective Oil" or oil['name'] == "Tainted Oil" :
				oils.remove(oil)

		fst7 = ["Clear Oil", "Sepia Oil", "Amber Oil", "Verdant Oil", "Teal Oil", "Azure Oil", "Indigo Oil", "Violet Oil", "Crimson Oil", "Black Oil", "Opalescent Oil", "Silver Oil", "Golden Oil"]

		oils = sorted(oils, key=lambda x:fst7.index(x['name']))	

		canUP = []
		for i in range(0, len(oils)):
			if oils[i] != oils[-1]:
				if oils[i]['chaosValue']*3 <= oils[i+1]['chaosValue']:
					canUP.append(oils[i]['name'])
		
		return oils, canUP

	def filter_oils(self):
		fst7 = ["Clear Oil", "Sepia Oil", "Amber Oil", "Verdant Oil", "Teal Oil", "Azure Oil", "Indigo Oil"]
		lasts = ["Violet Oil", "Crimson Oil", "Black Oil", "Opalescent Oil", "Silver Oil", "Golden Oil"]
		filtered_oils = {}
		filtered_oils['top'] = []
		filtered_oils['bot'] = []
		oils, canUP = self.update_oils()
		for oil in oils:
			if oil['name'] in fst7:
				filtered_oils['top'].append({'name': oil['name'],'icon': oil['icon'], 'chaosValue': oil['chaosValue'], 'exaltedValue': oil['exaltedValue'], 'divineValue': oil['divineValue'], "canUP": 1 if oil['name'] in canUP else 0})
			else:
				filtered_oils['bot'].append({'name': oil['name'],'icon': oil['icon'], 'chaosValue': oil['chaosValue'], 'exaltedValue': oil['exaltedValue'], 'divineValue': oil['divineValue'], "canUP": 1 if oil['name'] in canUP else 0})
		
		filtered_oils['top'] = sorted(filtered_oils['top'], key=lambda x:fst7.index(x['name']))
		filtered_oils['bot'] = sorted(filtered_oils['bot'], key=lambda x:lasts.index(x['name']))
		return filtered_oils



def oil():
	oil = Oils()

	oilItens = oil.filter_oils()

	return oilItens