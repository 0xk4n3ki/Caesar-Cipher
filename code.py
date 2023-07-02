def encrypt(f, key, set):
    cipher = ""
    for i in f:
        key = int(key) % len(set)
        index = set.find(i)

        # if the character is not present in the set
        if(index == -1):
            cipher += i
            continue
        diff = len(set)-index-1
        if(key <= diff):
            modifiedIndex = index + key
            cipher += set[modifiedIndex]
        else:
            modifiedIndex = key - diff-1
            cipher += set[modifiedIndex]
    return cipher

def decrypt(f, key, set):
    text = ""
    for i in f:
        key = int(key) % len(set)
        index = set.find(i)

        # if the character is not present in the set
        if(index == -1):
            text += i
            continue
        if(key <= index):
            modifiedIndex = index - key
            text += set[modifiedIndex]
        else:
            modifiedIndex = len(set) - (key - index)
            text += set[modifiedIndex]
    return text

def main():
    a = input("[+] Enrypt or Decypt(e/d)... ")

    # if user give input other than e or d
    if(str(a) != "e" and str(a) != "d"):
        print("[+] Enter e or d :)")
        return 0

    # user input
    f = "[+] Enter the text to "
    if(a=="e"):
        d = "Encrypt : "
    else:
        d = "Decrypt : "
    userInput = input(f + d)
    key = input("[+] Enter the key for shifting : ")

    print("[+] Default set of string is small alphbets.")
    set = input("[+] Enter the set to be used to " + d + "or press [ENTER] to use default : ")

    if(set == ""):
        set = "abcdefghijklmnopqrstuvwxyz"

    if(a=="e"):
        cipher =  encrypt(userInput, key, set)
        print(f"[+] Encrypted cipher : {cipher}")
    else:
        text =  decrypt(userInput, key, set)
        print(f"[+] Decrypted text : {text}")

if __name__ == "__main__":
    main()
