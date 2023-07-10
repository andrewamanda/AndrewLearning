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


def format_lyrics(lyrics):
    # Split the entire string into lines
    lyrics_lines = lyrics.replace('\n', ' ').split('...')

    # Normalize each line by trimming spaces at the beginning and end of each line
    lyrics_lines = [line.strip() for line in lyrics_lines]

    # Count the occurrences of "Oh, I keep dancin' with my"
    count = sum(1 for line in lyrics_lines if line.endswith("Oh, I keep dancin' with my"))
    print (count)


    # Combine lines ending with certain phrases with the next line
    eyes_closedbetter = []
    i = 0
    while i < len(lyrics_lines):
        line = lyrics_lines[i]
        if (line.endswith("While my friends are somewhere else") or
            line.endswith("'Cause I'm here alone") or
            line.endswith("So I'll keep dancin' with my") or
            line.endswith("I can't help but missin' you") or
            line.endswith("And life just goes on") or
            (line.endswith("Oh, I keep dancin' with my") and count > 2) or
            line.endswith("But I'm on my own")) and i+1 < len(lyrics_lines):
            if line.endswith("Oh, I keep dancin' with my"):
                count -= 1
            line += '\n'

        eyes_closedbetter.append(line)
        i += 1

    # Print each line
    for line in eyes_closedbetter:
        print(line)


format_lyrics(eyes_closed)
