import argparse

if __name__ == '__main__':
    # create argument parser
    parser = argparse.ArgumentParser()
    # add command line arguments; required=True means that the corresponding argument is not optional
    parser.add_argument('-update', action="store_true" ,help='To create a Pull Request to update the specified dependency')
    parser.add_argument('--i', type=argparse.FileType('r'), help="Pass in the relative path of the csv file", required=True)
    parser.add_argument('--d', type=str, help="Specify dependency", required=True)

    # parsing the arguments
    args = parser.parse_args()
    # print(args.update)
    # print(args.i)
    # print(args.d)