import argparse
import csv
import pandas as pd
import pull_request
import compare_versions

if __name__ == '__main__':
    # create argument parser
    parser = argparse.ArgumentParser()
    # add command line arguments; required=True means that the corresponding argument is not optional
    parser.add_argument('-update', action="store_true" ,help='To create a Pull Request to update the specified dependency')
    parser.add_argument('--i', type=argparse.FileType('r'), help="Pass in the relative path of the csv file", required=True)
    parser.add_argument('--d', type=str, help="Specify dependency", required=True)

    # print(args.update)
    # print(args.i)
    # print(args.d)

    # parsing the arguments
    args = parser.parse_args()
    # making dataframe 
    df = pd.read_csv(args.i.name)
    # output the dataframe
    # print(df)

    # Checking the update flag to see if just verisons have to be compared or pull request has to be created as well
    if(args.update == True):
        pull_request.pull_request()
    else:
        compare_versions.compare_versions()
    