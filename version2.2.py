while True:
    sayOrListen = input("say or listen?\n")
    if sayOrListen == "say":
        text = input("what do you want to say?\n").lower()
        text1 = list(text)
        text2 = []
        for number in range(len(text)):
            if text[number] == "a":
                text2.append("z")
            elif text[number] == "b":
                text2.append("y")
            elif text[number] == "c":
                text2.append("x")
            elif text[number] == "d":
                text2.append("w")
            elif text[number] == "e":
                text2.append("v")
            elif text[number] == "f":
                text2.append("u")
            elif text[number] == "g":
                text2.append("t")
            elif text[number] == "h":
                text2.append("s")
            elif text[number] == "i":
                text2.append("r")
            elif text[number] == "j":
                text2.append("q")
            elif text[number] == "k":
                text2.append("p")
            elif text[number] == "l":
                text2.append("o")
            elif text[number] == "m":
                text2.append("n")
            elif text[number] == "n":
                text2.append("m")
            elif text[number] == "o":
                text2.append("l")
            elif text[number] == "p":
                text2.append("k")
            elif text[number] == "q":
                text2.append("j")
            elif text[number] == "r":
                text2.append("i")
            elif text[number] == "s":
                text2.append("h")
            elif text[number] == "t":
                text2.append("g")
            elif text[number] == "u":
                text2.append("f")
            elif text[number] == "v":
                text2.append("e")
            elif text[number] == "w":
                text2.append("d")
            elif text[number] == "x":
                text2.append("c")
            elif text[number] == "y":
                text2.append("b")
            elif text[number] == "z":
                text2.append("a")
            elif text[number] == " ":
                text2.append(" ")
            else:
                text2.append(text[number])
        ok = "".join(text2)
        print(f"your code is:\n{ok}")
    elif sayOrListen == "listen":
        text = input("what do you want to translate?\n").lower()
        text1 = list(text)
        text2 = []
        for number in range(len(text)):
            if text[number] == "z":
                text2.append("a")
            elif text[number] == "y":
                text2.append("b")
            elif text[number] == "x":
                text2.append("c")
            elif text[number] == "w":
                text2.append("d")
            elif text[number] == "v":
                text2.append("e")
            elif text[number] == "u":
                text2.append("f")
            elif text[number] == "t":
                text2.append("g")
            elif text[number] == "s":
                text2.append("h")
            elif text[number] == "r":
                text2.append("i")
            elif text[number] == "q":
                text2.append("j")
            elif text[number] == "p":
                text2.append("k")
            elif text[number] == "o":
                text2.append("l")
            elif text[number] == "n":
                text2.append("m")
            elif text[number] == "m":
                text2.append("n")
            elif text[number] == "l":
                text2.append("o")
            elif text[number] == "k":
                text2.append("p")
            elif text[number] == "j":
                text2.append("q")
            elif text[number] == "i":
                text2.append("r")
            elif text[number] == "h":
                text2.append("s")
            elif text[number] == "g":
                text2.append("t")
            elif text[number] == "f":
                text2.append("u")
            elif text[number] == "e":
                text2.append("v")
            elif text[number] == "d":
                text2.append("w")
            elif text[number] == "c":
                text2.append("x")
            elif text[number] == "b":
                text2.append("y")
            elif text[number] == "a":
                text2.append("z")
            elif text[number] == " ":
                text2.append(" ")
            else:
                text2.append(text[number])
        ok = "".join(text2)
        print(f"your translated text is:\n{ok}")
    else:
        print("choose between say and listen")
    again = input("do you want to continue?\n").lower()
    if again == "no" or again == "nope" or again == "stop":
        break
print("thank you for choosing KingMaster")