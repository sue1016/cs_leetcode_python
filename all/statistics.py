import os

filenames = os.listdir()
def isLeetcode(filename):
    return "_" in filename
def isLeetcode400(filename):
    return int(filename.split("_")[0]) <= 400

leetcode400s = list(filter(isLeetcode400,filter(isLeetcode,filenames)))
print(len(leetcode400s)/400)

