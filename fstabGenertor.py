#!/usr/bin/python3

import yaml
import argparse

def convert(args):
    try:
        with open(args.input,'r') as inputFile:
            dict = yaml.load(inputFile, Loader=yaml.FullLoader)
    except:
        print("Can not open the input file")
        parser.print_help()
        exit(1)
    
    try:
        if args.output != "stdout" :
            outputFile = open(str(args.output), "w")
    except:
        print("Can not create the output file")
        parser.print_help()
        exit(1)
    try:    

        for item in dict["fstab"].items():
            device          = item[0]
            mountPoint      = item[1]["mount"]
            fileSystemType  = item[1]["type"]
            options         = ",".join(item[1].get("options",[]))
            dump            = item[1].get("dump",0)
            fsckOrder       = item[1].get("pass",0)

            if args.output != "stdout" :
                outputFile.write("{} {} {} {} {} {}\n".format(device,mountPoint,fileSystemType,options,dump,fsckOrder)) 
            else:
                print("{} {} {} {} {} {}".format(device,mountPoint,fileSystemType,options,dump,fsckOrder))

    except:
        print("Please check the Yaml file strcure it shoud be like:")
        print("fstab:")
        print("  <device>:")
        print("    mount: <mount_path>")
        print("    type: <file_system_type>")
        print("    opetions: # optional")
        print("    - <option>")
        print("    dump: <dump_value> # optional defualt 0")
        print("    pass: <fsck_rder_value> # optional defualt 0")
        parser.print_help()
        exit(1)
    if args.output != "stdout" :
        outputFile.close()




if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='fstabGenerator.py',
                                     usage='%(prog)s [options] <input_YAML_file_path>\nThe input YAML file structre shoul be like this:\nfstab:\n  <device>:\n    mount: <mount_path>\n    type: <file_system_type>\n    options: # optional\n      - <option>\n    dump: <dump_value> # optional defualt 0\n    pass: <fsck_rder_value> # optional defualt 0',
                                     description='Convert YAML to fstab file.',
                                     epilog='Enjoy the program! :)')
    parser.version = 'fstabGenerator.py version 1.0'
    parser.add_argument('input', metavar='input', type=str, help='the path of YAML file')
    parser.add_argument('-o','--output', action='store', type=str, help='write the configurations on the output file',default='stdout')
    parser.add_argument('-v','--version', action='version', help='show program\'s version number')

    # Execute parse_args()
    args = parser.parse_args()
    convert(args)
    
