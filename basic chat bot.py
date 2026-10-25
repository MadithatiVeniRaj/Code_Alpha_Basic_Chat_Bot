import random
print("Welcome...")
def response(word):
    if (word == "hello" or word == "hi"):
        return "Hi!"
    elif (word == "how are you"):
        return "I am good, Thankyou"
    elif(word=="bye"):
        return "Goodbye!"
    else:
        li = ["Sorry! I can't Understand", "Sorry! Ask something else"]
        return random.choice(li)
def chat():
    while True:
        word = input().lower().strip()
        print(response(word))
        if(word=="bye"):
            break

if __name__ == "__main__":
    chat()
    