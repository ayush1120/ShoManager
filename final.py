import os
import re
import time
import logging

ShoManager = logging.getLogger("ShoManager")
file_handler = logging.FileHandler("Changelog.log")
ShoManager.addHandler(logging.FileHandler("Logs.log"))
ShoManager.addHandler(file_handler)
ShoManager.setLevel(logging.INFO)


def logData(path, showname, final_list):
    with open('Changelog.log', 'w'):
        pass

    now = time.asctime(time.localtime(time.time()))

    ShoManager.info('{} : '.format(now))
    ShoManager.info('Path : {}'.format(path))
    ShoManager.info('Show Name : {}'.format(showname))
    ShoManager.info('Changelog : ')
    flag = 0
    for item in final_list:
        if item[0] != item[1]:
            flag = 1
            ShoManager.info('{} -> {}'.format(item[0], item[1]))
    if flag == 0 or final_list.__len__() == 0:
        ShoManager.info('No Changes')
    ShoManager.info('\n')

def rename(path, showname='None'):
    # os.chdir(path)
    pattern = re.compile(r'(ep\s?|e\s?|Episode\s?|^|{}\s?)(\d+)'.format(showname), re.IGNORECASE)
    ext_pattern = re.compile(r'\.(mp4|mkv|srt)$',re.IGNORECASE)

    file_list = os.listdir(path)
    final_list = []
    for file in file_list:
        # old_name = file
        file_ext = 'null'
        # print("File Name : ",file)
        matches = pattern.finditer(file)
        ext_matches = ext_pattern.finditer(file)
        for match in matches:
            # print(match.group(2))
            ep_no = match.group(2)
        for ext_match in ext_matches:
            # print('Extension : ', ext_match.group(0))
            file_ext = ext_match.group(0)

        if file_ext != 'null':
            new_file_name = showname + ' ' + 'Episode ' + ep_no.zfill(2) + file_ext
            temp = [file, new_file_name]
            final_list.append(temp)

    for item in final_list:
        print('Old Name :', item[0], '\nNew Name :', item[1], end='\n\n')



    choice = input('\nDo You Want To Proceed ?(y/n) : ')
    if choice == 'y' or choice == 'Y':
        logData(path, showname, final_list)
        cwd = os.getcwd()
        os.chdir(path)
        for item in final_list:
            os.rename(item[0], item[1])
        os.chdir(cwd)





# r""" def undo_task(task_time):
#     path = ''
#     showname = ''
#     final_list = []
#     with open('Changelog.log', 'r') as logFile:
#         data = logFile.readline()
#         while task_time not in data:
#             data = logFile.readline()
#         while True:
#             if 'Changelog : ' not in data:
#                 if 'Path : ' in data:
#                     path = re.match(r'Path\s:\s(.+)$', data).group(1)
#                 elif 'Show Name : ' in data:
#                     showname = re.match(r'Show\sName\s:\s(.+)$', data).group(1)
#                 data = logFile.readline()
#             else:
#                 data = logFile.readline()
#                 while '->END<-' not in data:
#                     old_name = re.match(r'(.+)\s->\s(.+)$', data).group(1)
#                     new_name = re.match(r'(.+)\s->\s(.+)$', data).group(2)
#                     final_list.append([new_name, old_name])
#                     data = logFile.readline()
#                 break

#     print(final_list)"""


def undo():
    final_list = []
    with open('Changelog.log', 'r') as logFile:
        data = logFile.readline()
        while 'Path' not in data:
            data = logFile.readline()
        path = re.match(r'Path\s:\s(.+)$', data).group(1)
        data = logFile.readline()
        showname = re.match(r'Show\sName\s:\s(.+)$', data).group(1)
        while True:
            if 'Changelog : ' not in data:
                data = logFile.readline()
            else:
                data = logFile.readline()
                while 'No Changes' not in data and data.strip() != '':
                    old_name = re.match(r'(.+)\s->\s(.+)$', data).group(1)
                    new_name = re.match(r'(.+)\s->\s(.+)$', data).group(2)
                    final_list.append([new_name, old_name])
                    data = logFile.readline()
                break
    # print('Path : ', path)
    # print('Showname : ', showname)
    # print(final_list)
    logData(path, showname, final_list)
    cwd = os.getcwd()
    os.chdir(path)
    for item in final_list:
        os.rename(item[0],item[1])
    os.chdir(cwd)



path = input('Enter Path : ')
name = input('Enter Name : ')
# rename('F:\TV Shows\Descendants of the Sun (2016)', 'Descendants of the Sun')
rename(path, name)
# undo()
