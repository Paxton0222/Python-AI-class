import re

list1 = ["", "/", "path/", "/path", "/path/", "//path/", "/path///"]

def getPath(path):
    if path:
        if path[0] != "/":
            path = "/" + path
        if path[-1] != "/":
            path = path + "/"
        path = re.sub(r"/{2,}", "/", path) #代表前一格項目至少出現2次,最多無限次
    else:
        path = "/"
        
    return path

for item in list1:
    item = getPath(item)
    print(item)
