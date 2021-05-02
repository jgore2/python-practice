# string concatenation

youtuber = "Kylie Ying" # some string variable

# different ways to do this
#print("subscribe to " + youtuber)
#print("subsrcibe to {}".format(youtuber))
#print(f"subscirbe to {youtuber}")
# f string is apparently the cleanest way to do string concatination

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time \
because I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)