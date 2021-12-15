# About fstabGenerator

This Script generates /etc/fstab configuration file form YAML file.

# Requirements:
- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). 
- [python](https://www.python.org/downloads/). 

# How to run: 
- Clone the project:

      `git clone https://www.python.org/downloads/ `
- Run the script:

      `cd fstab-generator`
      `./fstabGenerator.py <YAML_FILE_PATH> --output /etc/fstab`

# Examples:

- Print the configurations to stdout without safe it to a file.

    `./fstabGenerator.py <YAML_FILE_PATH>`

- Print help message.

    `./fstabGenerator.py --help`