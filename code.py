# --------------
import yaml

data=yaml.safe_load(open(path,'r'))
print(type(data))
#print(data['info'].keys())
#print(data['innings'][1])
print('City is ' + data['info']['city'] + ' and played at '+data['info']['venue'])
print(data['info']['teams'])
print(len(data['info']['teams']))
print('Toss decision was '+ data['info']['toss']['decision']+' and toss winne team was ' + data['info']['toss']['winner'])
lstinnings=data['innings'][0]['1st innings']['deliveries'][0]
print(lstinnings[0.1]['batsman'])
print(lstinnings[0.1]['bowler'])
print(len(data['innings'][0]['1st innings']['deliveries']))
print(len(data['innings'][1]['2nd innings']['deliveries']))
print(data['info']['outcome'])
#print(data['innings']['1st innings']['batsman'])


