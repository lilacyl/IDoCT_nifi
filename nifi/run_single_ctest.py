import sys, time
import os
import constants

def main(argv):

    with open('../../nifi/nifi-commons/nifi-properties/src/test/resources/NiFiProperties/conf/ctest.properties', 'w') as f:
        params = '\n'.join(argv[2:])
        f.write(params)

    command = constants.CD_NIFI_PATH
    command += constants.MVN_INSTALL_NIFI_COMMONS
    cur_test_name = argv[1]
    command += 'mvn -pl nifi-commons/nifi-properties/ test -Dtest="'+cur_test_name+'"'
    os.system(command)

if __name__ == "__main__":
    main(sys.argv)  