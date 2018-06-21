def getcall(calltype = 'shout'):
    def shout(word = "Yes"):
        return word.upper() + '!!!'
    def whisper(word = "yes"):
        return word.lower() + '!!!'
    if calltype == 'shout':
        return shout
    else :
        return whisper
print(getcall())
print(getcall()())
