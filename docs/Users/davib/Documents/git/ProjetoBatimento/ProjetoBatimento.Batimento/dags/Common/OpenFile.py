
def OpenFile(FileDir):
    with open(FileDir, 'r') as file:
        Arq = file.readlines()
    return Arq
