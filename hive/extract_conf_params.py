import constants
import os
import json

def extract_conf_param(input_file, output_file):

    with open( input_file, 'r') as inputF:
        lines = inputF.readlines()
        with open( output_file, 'w') as outputF:
            isNewConfVar = False
            for i, line in enumerate(lines):
                
                line = line.strip()
                
                if line.startswith("//"):
                    continue
                if isNewConfVar:
                    
                    quote_idx = line.index('"')
                    quote_idx2 = line[quote_idx + 1:].index('"')
                    isNewConfVar = False
                    confParam = line[quote_idx + 1 :quote_idx2 + 1]
                    outputF.write(confParam + "\n")
        


                # a hardcoded way to check if the line contains a new ConfVar
                if '(' in line and line[0].isupper():
                    if ',' not in line:
                        isNewConfVar = True
                        continue
                    paranthesis_idx = line.index('(')
                    comma_idx = line.index(',')
                    confParam = line[paranthesis_idx +2 :comma_idx - 1]
                    outputF.write(confParam + "\n")
    
if __name__ == "__main__":

    extract_conf_param(constants.HIVE_CONF_PARAM_IN_JAVA_PATH, constants.OUTPUT_CONF_PARAM_PATH)