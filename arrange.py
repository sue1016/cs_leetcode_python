import os
import shutil
tag = input("input the tag:")
indexs = input("input the indexs:")
indexs = indexs.split()
path = os.getcwd()
tagPath = path + "/" + tag
questionsPath = path + "/all"
if not os.path.exists(tagPath):
    os.mkdir(tagPath)
questionNames = filter(lambda name: "_" in name,os.listdir(questionsPath))
foundQuestionsNames = filter(lambda question:question.split("_")[0] in indexs,questionNames)
for foundName in foundQuestionsNames:
    if not os.path.exists(tagPath+"/"+foundName):
        shutil.copy(questionsPath+"/"+foundName,tagPath)
