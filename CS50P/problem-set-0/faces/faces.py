sentence = input("Write sentence with (':(' or ':)') in it: ")

sentence = sentence.replace(":)", "🙂")
sentence = sentence.replace(":(", "🙁")

print(sentence)