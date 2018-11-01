import os
import fnmatch
import time

class Finder():

    DIRECTORY_NAME = 'Search_Results'

    def __init__(self, search_area):
        self.search_area = search_area
        self.create_directory()

    def create_directory(self):
        if not os.path.exists(Finder.DIRECTORY_NAME):
            os.makedirs(Finder.DIRECTORY_NAME)

    def write_file(self, fName, list):
        path = os.path.join(Finder.DIRECTORY_NAME,fName)
       # path = Finder.DIRECTORY_NAME + fName
        with open(path, 'w') as f:
            for l in list:
                f.write(l+'\n')

    def get_search(self, thread_name, keyword):
        time.sleep(2)
        list = set()
        print(thread_name + ' is processing...')
        print(keyword)
        #keyword = keyword + "*"
        for dName,sdName,fName in os.walk(self.search_area):
            for file in fName:
                if fnmatch.fnmatch(file, keyword + "*"):
                    list.add(os.path.join(dName,file))

        self.write_file(keyword, list)
