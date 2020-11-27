import random

def f():
    return fish[random.randint(0, len(fishSet) - 1)]


fish = ["karp", "losos", "shyka", "goldfish", "guppy", "bluetang", "swordfish", "megalodon", "bluegill", "clownfish", "shark", "garfish", "angler", "beluga", "oscar"]
fishSet = set(fish)

fisher1 = {f(), f(), f()}
fisher2 = {f(), f(), f()}
fisher3 = {f(), f(), f()}
print("First fisher caught", fisher1)
print("Second fisher caught", fisher2)
print("Third finisher caught", fisher3)

print("Not caught fish:")
print(fishSet.difference(fisher1, fisher2, fisher3))