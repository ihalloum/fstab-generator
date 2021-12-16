#!/usr/bin/python3
import sys
import yaml
import argparse

def convert(args,parser):
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
        if args.output == sys.stdout :
            output_file = sys.stdout
        else:
            output_file = open(str(args.output), "w")
        
    except:
        # Print Error and help message and exit.
        print("Can not create the output file")
        parser.print_help()
        exit(1)
    try:    
        # Collect the configuration for each device.    
        for item in dict["fstab"].items():
            device              = item[0]
            mount_point         = item[1]["mount"]
            file_system_type    = item[1]["type"]
            options             = ",".join(item[1].get("options",[]))
            dump                = item[1].get("dump",0)
            fsck_order          = item[1].get("pass",0)

            # Write the device configuration to stdout or output file, depending on output argument.
            output_file.write("{} {} {} {} {} {}\n".format(device,mount_point,file_system_type,options,dump,fsck_order)) 

    except:
        # Print Error and help message and exit.
        print(yaml_strucutre_hint_message)
        parser.print_help()
        exit(1)
    # CLose the output file.
    if args.output != "stdout" :
        output_file.close()


if __name__ == '__main__':
    # Create the parser.
    yaml_strucutre_hint_message = "The input YAML file structure should be like this:\nfstab:\n  <device>:\n    mount: <mount_path>\n    type: <file_system_type>\n    options: # optional\n      - <option>\n    dump: <dump_value> # optional defualt 0\n    pass: <fsck_rder_value> # optional defualt 0"
    parser = argparse.ArgumentParser(prog='fstabGenerator.py',
                                     usage='%(prog)s [options] <input_YAML_file_path>\n'+ yaml_strucutre_hint_message,
                                     description='Generate /etc/fstab configuration file form YAML file.',
                                     epilog='Enjoy the program! :)')
    # Set the version.
    parser.version = 'fstabGenerator.py version 1.0'
    # Add the input file arguments.
    parser.add_argument('input', metavar='input', type=str, nargs=1, help='the path of YAML file')
    # Add the output file arguments.
    parser.add_argument('-o','--output', action='store', nargs=1, help='write the configurations on the output file', default=sys.stdout)
    # Add the version arguments.
    parser.add_argument('-v','--version', action='version', help='show program\'s version number')

    # Execute parse_args().
    args = parser.parse_args()

    # Call convert function.
    convert(args,parser)
    
