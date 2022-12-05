"""
Usage: python3 findTestsInAllFiles.py
Goes through all the files in NIFI COMMONS and find all the files that end with TEST.JAVA. This script will make use of 'findTests.py'
"""
import os
import constants

def is_test_file(path):
    return (path.endswith(".java") and path.startswith("Test"))

def find_all_tests_path():
    res = []
    directory = constants.HIVE_COMMONS_PATH
    print(directory)
    for root, dirs, files in os.walk(directory):
        for filename in files:
            # print(filename)
            if is_test_file(filename):
                res.append(os.path.join(root, filename))

    with open(constants.ALL_TESTS_PATH, 'w') as fp:
        for item in res:
            # write each path on a new line
            fp.write("%s\n" % item)
    
if __name__ == "__main__":
    find_all_tests_path()
    print(1)
    test = open(constants.ALL_TESTS_PATH, 'r')

    print(2)
    Lines = test.readlines()

    print(3)
    for i, line in enumerate(Lines):
        # remove line breaks

        print(4)
        line = line.strip()
        command = "python3 findTests.py --t "+ line
        os.system(command)
