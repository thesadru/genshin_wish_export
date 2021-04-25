import argparse
import csv
import genshinstats as gs

parser = argparse.ArgumentParser()
parser.add_argument('-o','--output',default='export.csv',help="output file")
parser.add_argument('--lang',default='en',help="output language")
parser.add_argument('--authkey',help="authkey for authentication")

args = parser.parse_args()

with open(args.output,'w',newline='',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['time','name','type','rarity','banner'])
    
    print('getting data from genshin...')
    for i,pull in enumerate(gs.get_entire_gacha_log(lang=args.lang,authkey=args.authkey)):
        print(f'fetched {i} pulls',end='\r')
        writer.writerow([pull['time'],pull['name'],pull['type'],pull['rarity'],pull['gacha_name']])
