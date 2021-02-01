
def main():
    challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]
    trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]
    nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]


    print(challenge[2][1], challenge[2][0], challenge[-1])

    print(trial[2]["goggles"], trial[2]["eyes"], trial[3])

    print(nightmare[0]["user"]["name"]["first"], nightmare[0]["kumquat"], nightmare[0]["d"])
  
    print("My",challenge[2][1],"! The",challenge[2][0], "do", challenge[-1],"!")

if __name__ == "__main__":
    main()
