# About fstabGenerator

This Script generates /etc/fstab configuration file form YAML file.

# Requirements:
- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). 
- [python](https://www.python.org/downloads/).
- [pip.](https://pip.pypa.io/en/stable/)

# How to run: 
- Clone the project:

      git clone https://github.com/ihalloum/fstab-generator.git
- Run the script:

      cd fstab-generator
- Install requirement modules*:

      pip3 install requirements.txt
- Run the script*:

      python3 ./fstabGenerator.py <YAML_FILE_PATH> --output /etc/fstab

# Examples:

- Print the configurations to stdout to check them without save to a file.

      python3 ./fstabGenerator.py <YAML_FILE_PATH>

- Print help message.

      python3 ./fstabGenerator.py --help

* you can use python or pip instead of python3 and pip3. 
