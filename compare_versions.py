from time import sleep
from git import Repo
import os
import shutil
import importlib.resources
import json
import truncate
import compareStrings

def compare_versions(repo_url, dependency, name, updateFlag):
    print("name: " + str(name))
    print("repo: " + str(repo_url))
    # creating a directory which will store the cloned project temporarily
    os.mkdir('test')
    Repo.clone_from(repo_url, 'test')
    # getting dependency name and version as specified by the user
    dependencyArr = truncate.truncate(dependency)
    dependencyName = dependencyArr[0]
    dependencyVersion = dependencyArr[1]
    
    # getting full path of the test directory
    path = os.path.join(os.getcwd(), 'test')
    flag = False
    newData = {}
    # opening package.json file
    with open(path + "/package.json") as f:
        data = json.load(f)
        # stores version of the specified dependency
        version = ""
        symbols = ""
        try:
            string = data['dependencies'][dependencyName]
            for i in range(0, len(string)):
                # Removing any ^, ~ or similar symbols
                if(((ord(string[i])-ord('0')) >= 0 and (ord(string[i])-ord('0')) <= 9) or string[i] == '.'):
                    version += string[i]
                else:
                    symbols += string[i]
            print("version: " +str(version))
            # comparing the version numbers
            flag = compareStrings.compareStrings(version, dependencyVersion)
            print("version_satisfied: " + str(flag))
        except:
            print("version_satisfied: Dependency not found")
    
        # if update flag is not set or flag variable is true (which means the version is compatible with what was specified in command line) then the conditional is executed
        if(updateFlag == False or flag == True):
            # removing directory
            shutil.rmtree(path)
            print()
            return flag
        
        # updating the dependency version to what the user has specified
        data['dependencies'][dependencyName] = symbols+dependencyVersion
        print(str(dependencyName) + ": " + str(data['dependencies'][dependencyName]))
        newData = data
    
    # updating package.json file locally
    with open(path + "/package.json", 'w') as f:
        json.dump(newData, f, indent=4) # indent = 4 beautfies json file
    
    # removing the cloned directory
    print()
    shutil.rmtree(path)
    

