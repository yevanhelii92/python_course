def shall():
    def whisper(word = "yes"):
        return word.lower() + '...'
    print(whisper())
shall()
try:
    print(whisper())
except NameError as err:
    print(err)