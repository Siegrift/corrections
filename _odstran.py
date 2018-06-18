import os, sys

def getXoj(jehoDir):
    files = os.listdir(os.path.join(os.getcwd(), jehoDir))
    for file in files:
        if file.endswith('.xoj'):
            return file
    return -1


dirs = [d for d in os.listdir(os.getcwd()) if not d.startswith('_')]
for d in dirs:
    if getXoj(d) != -1:
        print('rm "%s"' % (os.path.join(d, getXoj(d))))
        os.system('rm "%s"' % (os.path.join(d, getXoj(d))))
