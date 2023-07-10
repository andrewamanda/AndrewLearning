eyes_closed = ''' I know it's a bad idea ...But how can I help myself?... Been inside for most this
year...And I thought a...few drinks, they might help...It's been a while, my dear...Dealin' with the cards
life dealt...I'm still...holdin' back these tears...While my friends are somewhere else...I pictured this
year a little bit different when it hit February...I step in the bar, it hit me so hard, oh, how can it be this
heavy?...Every...song reminds me you're gone and I feel the lump form in my throat...'Cause I'm here
alone...Just dancin' with my eyes closed...'Cause everywhere I look, I still see you...And time is movin'
so slow...And I don't know what else that I can do...So I'll keep dancin' with
my...Eye-eye-eye-eyes...Eye-eye-eye-eyes closed...Eye-eye-eye-eyes...So I'll keep dancin' with
my...Delusion is here again...And I think you'll come home soon...A word brings me right back
in...Then it's only me that's in this room...I guess I could just pretend...The colors are more than
blue...But I lost more than my friend...I can't help but missin' you...I pictured this month a little
bit...different, no one is ever ready...And when it unfolds, you get in a hole, oh, how can it be this
heavy?...Everything changes, nothing's the same, except the truth is now you're gone...And life just
goes on...So I'm dancin' with my eyes closed...'Cause everywhere I look, I still see you...And time is
movin' so slow...And I don't know what else that I can do...So I'll keep dancin' with
my...Eye-eye-eye-eyes...Eye-eye-eye-eyes closed...Eye-eye-eye-eyes...So I'll keep dancin' with
my...Eye-eye-eye-eyes...Eye-eye-eye-eyes closed...Eye-eye-eye-eyes...Oh, I keep dancin' with
my...They're shutting the bar, they're cleaning the floor...And everyone is already home...But I'm on my
own...Still dancin' with my eyes closed...'Cause everywhere I look, I still see you...Time is movin' so
slow...And I don't know what else that I can do...So I'll keep dancin' with
my...Eye-eye-eye-eyes...Eye-eye-eye-eyes closed...Eye-eye-eye-eyes...Oh, I keep dancin' with
my...Eye-eye-eye-eyes...Eye-eye-eye-eyes closed...Eye-eye-eye-eyes...Oh, I keep dancin' with my '''

#Great program, you can improve its readbility, make it simpler, remove some unncessary structures like index, list, dictionary, etc

#The below 10 lines can be replaced by one single line: eyes_closedbetter = eyes_closed.replace('\n', ' ').split('...')
eyes_closed = eyes_closed.split("...")
eyes_closedbetter = []
for x in eyes_closed:
    if '\n' in x:
        here = x.replace('\n', ' ')
        here.strip()
        eyes_closedbetter.append(here)
    else:
        x.strip()
        eyes_closedbetter.append(x)

noo = {}
be = 0
for x in eyes_closedbetter:
    noo[be]= x
    be = be + 1

noo[3] = noo[3] + '∂'
noo[4] = noo[4] + '∂'
noo[7] = noo[7] + '∂'
noo[8] = noo[8] + '∂'
noo[12] = noo[12] + '∂'
noo[13] = noo[13] + '∂'

newlist = []
for k,v in noo.items():
    if '∂' in noo[k]:
        if '∂' not in noo[k+1]:
            sue = 0
        elif '∂' in noo[k] and noo[k+1]:
            h=noo[k]+noo[k+1]
            newlist.append(h)
    else:
        newlist.append(v)
#print(newlist)

def stupidassfunction(list_to_check, item_to_find, start, end):
    indices = []
    for idx, x in enumerate(list_to_check[start:end]):
        if x == item_to_find:
            indices.append(idx)
    return(indices)

newlistbetter = []
for x in newlist:
    x = x.replace('∂', " ")
    x = x.strip()
    newlistbetter.append(x)
betterlist = []
for x in newlistbetter:
    if (x == "While my friends are somewhere else" or x == "'Cause I'm here alone" or x =="So I'll keep dancin' with my" or x == "So I'll keep dancin' with my" or x =="I can't help but missin' you" or  x == "And life just goes on" or x == "Oh, I keep dancin' with my" or x == "But I'm on my own"):
        if ( [20] not in stupidassfunction(newlistbetter, x, 19, 25) or  [42] not in newlistbetter.index(x, 30, 44)):
            x = x + "\n"
    betterlist.append(x)


for x in betterlist:
    print(x)
#print(noo)


print(stupidassfunction(newlistbetter, "So I'll keep dancin' with my", 19, 25))
