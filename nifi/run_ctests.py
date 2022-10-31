from run_single_ctest import run_single_test
import json
from tqdm import tqdm
import argparse
import constants

def reverse_map(tp_map):
    reversed_map = {}
    for test, params in tp_map.items():
        for param in params:
            reversed_map[param] = reversed_map.get(param, [])
            reversed_map[param].append(test)
    return reversed_map

def main(args):
    test_param_map = {}
    with open(args.map, 'r') as f:
        test_param_map = json.load(f)
    reversed_map = reverse_map(test_param_map)
    with open(args.input, 'r') as f:
        for line in tqdm(f):
            pairs = line.strip().split(',')
            test_args = []
            params = []
            for param, value in zip(pairs[0::2], pairs[1::2]):
                if param == '':
                    break
                if param not in reversed_map:
                    print('Configuration %s does not exist in test map'%param)
                    continue
                test_args.append("%s=%s"%(param, value))
                params.append(param)
            if len(params) == 0:
                continue
            with open('../../nifi/nifi-commons/nifi-properties/src/test/resources/NiFiProperties/conf/ctest.properties', 'w') as f:
                to_insert = '\n'.join(test_args)
                f.write(to_insert)
            command = constants.CD_NIFI_PATH
            command += constants.MVN_INSTALL_NIFI_COMMONS
            run_single_test(reversed_map[params[0]], command)
            # for test in ]:
            #     run_single_test(test)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default = 'configuration.csv',help='path to configuration csv file')
    parser.add_argument('--map', default = './result/param_map.json',help='path to map')
    parser.add_argument('--output', default = './result/ctest_result.json', help='ctest result file')
    args = parser.parse_args()
    main(args)