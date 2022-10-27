import constants
import argparse
import os

def find_test(input_path):

    test_names = []
    find = False
    with open(input_path, 'r') as test_file:
        className = False
        for line in test_file:
            if 'public class' in line:
                test_class = line.split(" ")
                test_names.append(test_class[2] + "\n")
                test_names.append(input_path + "\n")
                className = True
            if '@Test' in line:
                if not className:
                    className = True
                    input_file_parse = input_path.split("/")[-1].replace(".java","")
                    test_names.append(input_file_parse + "\n")
                    test_names.append(input_path + "\n")

                test_name_line = next(test_file).split(" ")
                for word in test_name_line:
                    if word[-2:] == ("()"):
                        test_names.append(word.replace("()", "\n"))
                        break
    if len(test_names) == 0:
        return
    test_names[-1]= test_names[-1].replace("\n", "")
    with open("test/" + test_names[0].replace("\n", "")+".txt", 'a') as output_file:
        print("test/" + test_names[0].replace("\n", "")+".txt")
        output_file.writelines(test_names)

    print("Finished!" + "Total test number is " + str(len(test_names) - 2))
    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Input Test file and output file name')
    parser.add_argument('--TEST_FILE', '--t', type=str, required = True, help='The path of Test file')
    args = parser.parse_args()
    find_test(args.TEST_FILE)
