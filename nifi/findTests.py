import constants
import argparse
import os

def find_test(input_path, output_path):

    test_names = []
    find = False
    with open(input_path, 'r') as test_file:
        for line in test_file:
            if 'public class' in line:
                test_class = line.strip('/n').split(" "):
                for word in test_class:
                    if word[-1::] == ("{"):
                        test_names.append(word.replace("{", ""))
                        break
            if '@Test' in line:
                test_name_line = next(test_file)
                test_name_line.strip('/n')
                test_name_line.split(" ")
                for word in test_name_line:
                    if word[-2::] == ("{"):
                        test_names.append(word.replace("()", ""))
                        break
    with open(output_path, 'a') as output_file:
        output_file.writelines(test_names)

    print("Finished!")
    return




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Input Test file and output file name')
    parser.add_argument('--TEST_FILE', '--t', type=str, required = True, help='The path of Test file')
    parser.add_argument('--OUTPUT_PATH', '--o', type=str, required = True, help='The path of Output file')
    args = parser.parse_args()
    find_test(args.TEST_FILE, args.OUTPUT_PATH)
