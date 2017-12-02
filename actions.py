import requests
import json
import csv
from time import gmtime, strftime


app_id = '2c8605ed'
app_key = 'e5702063af55850166b5b750edeeccb1'
language = 'en'


def search(word_id = 'Ace'):



    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

    r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
    # print(r.text)

    r = r.json()['results'][0]['lexicalEntries']

    for i in range(len(r)):
        ii = r[i]
        print('\n\nlexicalCategory ---->>>>>', ii['lexicalCategory'])
        for j in range(len(ii['entries'])):
            jj = ii['entries'][j]
            for k in range(len(jj['senses'])):
                kk = jj['senses'][k]
                print('\n       Def',k,'-->',kk['definitions'][0])
                try:
                    for l in range(len(kk['examples'])):
                        ll = kk['examples'][l]
                        print('             example',l,'-->',ll['text'])
                except:
                    pass

def gettrainset():
    sett = []
    with open("learningdata.csv","r", newline="") as c:
        reader = csv.DictReader(c)
        for row in reader:
            sett.append(row['word'])
    return sett


def save(wordname = 'hh'):

    # writer.writerow([wordname,time,unknowTimes])
    # writer.writeheader()

    if notExitst(wordname):
        c = open("learningdata.csv","a+", newline="")
        fieldnames = ['word', 'first search', 'unknown times']
        writer = csv.DictWriter(c, fieldnames=fieldnames)
        writer.writerow({'word': wordname, 'first search': strftime("%Y-%m-%d %H:%M:%S", gmtime()), 'unknown times': 1})
        c.close()
    else:
        print('it is already exist')
        # add unknown times
        # with open("learningdata.csv","r", newline="") as c:
        #     reader = csv.DictReader(c)
        #     for row in reader:
        #         if row['word'] == wordname:
        #             flag = 1
        pass





def notExitst(wordname):
    flag = 1
    with open("learningdata.csv","r", newline="") as c:
        reader = csv.DictReader(c)
        for row in reader:
            if row['word'] == wordname:
                print(row['first search'])
                flag = 0
    return flag




save()
