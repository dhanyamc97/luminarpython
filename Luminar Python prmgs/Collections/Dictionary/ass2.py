#def nameAndId(num_Tweet):
    #return dict
#def final_value(dict, tweet_max):

test_case = int(input())

dict = {}
dict2 = {}
for x in range(0,test_case):

    num_Tweet = int(input())
    for i in range(num_Tweet):
        name_id = input()
        name_id = name_id.split(" ")
        if (name_id[0] not in dict):
            dict[name_id[0]] = 1
        else:
            dict[name_id[0]] += 1

    tweet = dict.values()
    max_tweet = max(tweet)

    for k, v in sorted(dict.items()):
        if (v == max_tweet):
            if v not in dict2:
                dict2[v] = [k]
            else:
                dict2[v].append(k)
            print(k, v)


#elif (test_case == 2):
'''2
4
sachin tweet_id_1
sehwag tweet_id_2
sachin tweet_id_3
sehwag tweet_id_4
5
dhoni tweet_id_10
dhoni tweet_id_11
kohli tweet_id_12
dhoni tweet_id_13
dhoni tweet_id_14
'''


























