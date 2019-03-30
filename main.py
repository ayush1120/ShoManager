import os, time



os.system('cls')
print('Hello')
print('\n os.path : ' , os.path)
print('\n Type of os.path.dirname ' , type(os.path.dirname))
print('\n Current Working Dir : ' , os.getcwd())

pwd = os.getcwd()

print('\n Type of __file__ : ' , type(__file__))

print('\n Current File Name : ' , __file__)

print('\n Putting pwd in os.path.dirname : ' , os.path.dirname(pwd))


file_list = os.listdir(pwd)

print('\n File List In pwd : ' ,file_list)





class Show(object):

    name = 'Unknown'
    path = ''
    num_episodes = 0
    subs = 'false'
    extension = 'default'

    def __init__(self,name = 'Unknown', path = '', num_episodes = 0, subs = 'false', extension = 'default'):
        self.name = name
        self.path = path
        self.num_episodes = num_episodes
        self.subs = subs
        self.extension = extension

    def __str__(self):
        return self.name

    
    def findvideos(self):
        file_list = os.listdir(self.path)
        for fil in file_list:
            fil = str(fil)
            

file_list = os.listdir(r'F:\\TV Shows\\The Bride of Habaek')


print('File List : ', file_list)

s = "F:\TV Shows\The Bride of Habaek"

print('\n\nsafkhasb : ',s+'\\'+file_list[0])

old = file_list[0]

os.rename(s+'\\'+file_list[0],s+'\\'+'new.mp4')




os.rename(s+'\\'+'new.mp4',s+'\\'+file_list[0])


class File(object):

    dir = ''
    name = ''
    file_path = ''
    extension = ''