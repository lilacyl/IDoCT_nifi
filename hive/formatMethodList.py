import constants
import os
import json

res = []

def format_method_to_list(filename):
    testFileName = filename[:-4] # remove the ".txt" at the end of the filename

    with open(os.path.join(constants.INDIVIDUAL_TEST_INFO_FOLDER, filename), 'r') as f:
        lines = f.readlines()

        for i, line in enumerate(lines):
            if i == 0 or i == 1:
                continue
            else:
                cur = testFileName + "#" + line.strip()
                res.append(cur)
    
if __name__ == "__main__":
    for filename in os.listdir(constants.INDIVIDUAL_TEST_INFO_FOLDER):
        print(filename)
        format_method_to_list(filename)
    
    json.dump(res, open(constants.FORMATTED_TEST_METHOD_LIST_PATH, "w"), indent=2)