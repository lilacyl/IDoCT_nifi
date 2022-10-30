"""
usage: python3 genmap.py
Generate mapping after all the test files had been identified.
Generate mapping is the step after the instrumentation of GET and SET.
"""

import constants
import os
import json

res = {}

def params_in_report(report_path):
    params = []
    report = open(report_path, 'r')
    Lines = report.readlines()
    for line in Lines:
        line = line.strip()
        info = line.split(',')
        try:
            params.append(info[constants.PRAM_IDX])
        except:
            return None
    return params



def parse_and_run_test(test_path):
    test = open(test_path, 'r')
    Lines = test.readlines()
    cur_test_file = None
    report_path = None
    pl_name = None
    for i, line in enumerate(Lines):
        # remove line breaks
        line = line.strip()
        if i == 0:
            cur_test_file = line
        elif i == 1:
            report_path = line
            folders = line.split('/')
            # hardcode the path of the module we want to build
            pl_name = folders[3]+'/'+folders[4]+'/'

        else:
            cur_test_name = cur_test_file+"#"+line
            # run the test
            command = constants.CD_NIFI_PATH
            command += "mvn install -pl " + pl_name + " -am -DskipTest;"
            # command += constants.MVN_INSTALL_NIFI_COMMONS
            command += 'mvn -pl '+ pl_name +' test -Dtest="'+cur_test_name+'" DtestFailureIgnore=true'
            # command += 'mvn -pl nifi-commons/nifi-properties/ test -Dtest="'+cur_test_name+'"'
            os.system(command)

            # get params

            params = params_in_report(report_path)
            if params == None:
                continue
            res[cur_test_name] = params.copy()
    
def output_res(output_path):
    json.dump(res, open(output_path, "w"), indent=2)


if __name__ == "__main__":
    for file in os.listdir(constants.TEST_INFO_FOLDER):
        file_path = "test/"+file
        parse_and_run_test(file_path)
    
    output_res(constants.OUTPUT_PATH)
