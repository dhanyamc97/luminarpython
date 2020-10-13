def nameAndId(num_Tweet):
    for i in range(num_Tweet):
        name_id = input()
        name_id = name_id.split(" ")
        if(name_id[0] not in dict):
            dict[name_id[0]] = 1
        else:
            dict[name_id[0]] += 1
    return dict

def final_value(dict,tweet_max):

    for k,v in sorted(dict.items()):
        if(v == tweet_max):
            if v not in dict2:
                dict2[v] = [k]
            else:
                dict2[v].append(k)
            print(k,v)

test_case = int(input())
dict = {}
dict2 = {}

for x in range(0,test_case):

    num_Tweet = int(input())
    res = nameAndId(num_Tweet)
    tweet = dict.values()
    max_tweet = max(tweet)
    res1 = final_value(dict,max_tweet)














    










