import os

#These functions will be used in our program to do things like creating files and accessing the data within the files.
#I used the os module for this.

#This will set each website crawled as a separate folder
def create_folder(directory):
    if not os.path.exists(directory):
        print('Directory being created: '+directory)
        os.makedirs(directory)

#This will create the queue for crawling and define crawled files.
def create_files(project_name,url_link):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, url_link)
    if not os.path.isfile(crawled):
        write_file(crawled,'')

#Create new file
def write_file(path,data):
    f = open(path,'w')
    f.write(data)
    f.close()

#Add data onto existing file
def add_to_file(path,data):
    with open(path,'a') as f:
        f.write(data)

#Delete contents of file
def delete_contents(path):
    with open(path,'w'):
        pass

#This will convert file contents to a set (prevent duplicates)
def file_set(file_name):
    final = set()
    with open (file_name,'rt') as f:
        for line in f:
            final.add(line.strip())
    return final

#Convert the set into a file
def set_file(url,file_name):
    delete_contents(file_name)
    for link in sorted(url):
        add_to_file(file_name,url)




