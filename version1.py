sayOrListen =input("do you want to say something or listen something?").lower()
if sayOrListen == "say":
    sayContent = input("what do you want to say?\n")
    sayReverseContent = sayContent[::-1]
    print(f"you should say this\n{sayReverseContent}")
elif sayOrListen == "listen":
    listenContent = input("what do you want to translate?\n")
    listenReverseContent = listenContent[::-1]
    print(f"your translated content is:\n{listenReverseContent}")
else:
    print("something went wrong.")
print("thank you for choosing Kingmaster")