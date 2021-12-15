#!/usr/bin/python3

import yaml
import argparse

def convert(args):
    try:
        # Open YAML input file to read.
        with open(args.input,'r') as inputFile:
            # Store configuration on dictionary.
            dict = yaml.load(inputFile, Loader=yaml.FullLoader)
    except:
        # Print Error and help message and exit.
        print("Can not open the input file")
        parser.print_help()
        exit(1)
    
    try:
        # Check if the configuration will be written to file and create this file.
        if args.output != "stdout" :
            outputFile = open(str(args.output), "w")
    except:
        # Print Error and help message and exit.
        print("Can not create the output file")
        parser.print_help()
        exit(1)
    try:    
        # Collect the configuration for each device.    
        for item in dict["fstab"].items():
            device          = item[0]
            mountPoint      = item[1]["mount"]
            fileSystemType  = item[1]["type"]
            options         = ",".join(item[1].get("options",[]))
            dump            = item[1].get("dump",0)
            fsckOrder       = item[1].get("pass",0)
            # Write the device configuration to stdout or output file, depending on output argument.
            if args.output != "stdout" :
                outputFile.write("{} {} {} {} {} {}\n".format(device,mountPoint,fileSystemType,options,dump,fsckOrder)) 
            else:
                print("{} {} {} {} {} {}".format(device,mountPoint,fileSystemType,options,dump,fsckOrder))

    except:
        # Print Error and help message and exit.
        print("Please check the YAML file structure it shoud be like:")
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
    # CLose the output file.
    if args.output != "stdout" :
        outputFile.close()




if __name__ == '__main__':
    # Create the parser.
    parser = argparse.ArgumentParser(prog='fstabGenerator.py',
                                     usage='%(prog)s [options] <input_YAML_file_path>\nThe input YAML file structure should be like this:\nfstab:\n  <device>:\n    mount: <mount_path>\n    type: <file_system_type>\n    options: # optional\n      - <option>\n    dump: <dump_value> # optional defualt 0\n    pass: <fsck_rder_value> # optional defualt 0',
                                     description='Generate /etc/fstab configuration file form YAML file.',
                                     epilog='Enjoy the program! :)')
    # Set the version.
    parser.version = 'fstabGenerator.py version 1.0'
    # Add the input file arguments.
    parser.add_argument('input', metavar='input', type=str, help='the path of YAML file')
    # Add the output file arguments.
    parser.add_argument('-o','--output', action='store', type=str, help='write the configurations on the output file',default='stdout')
    # Add the version arguments.
    parser.add_argument('-v','--version', action='version', help='show program\'s version number')

    # Execute parse_args().
    args = parser.parse_args()

    #Call convert function.
    convert(args)
    
