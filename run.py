"""
run.py

Used during development for running the given application.
"""
import subprocess
import sys
import yaml
from constants import constants
from constants import DEVELOPMENT_MODE, PRODUCTION_MODE, TESTING_MODE, DOCUMENTATION_MODE, BUILD_MODE

class ApplicationRunner:
    def __init__(self, run_code):
        """
        ApplicationRunner

        Responsible for running the application in a given Run Mode, specified by run_code.

        Parameters:
        -----------
        - run_code (str): Value representing 1 of 5 run modes:
            - Development Mode (Expected: 0, dev)
            - Production Mode (Expected: 1, prod)
            - Testing Mode (Expected: 2, test)
            - Documentation Mode (Expected: 3, docs)
            - Build Mode (Expected: 4, build)
        """
        _mode_constants = None
        _mode: str = ''

        # Determine Run Mode
        if run_code == '0' or run_code == 'dev': _mode = '0'
        elif run_code == '1' or run_code == 'prod': _mode = '1'
        elif run_code == '2' or run_code == 'test': _mode = '2'
        elif run_code == '3' or run_code == 'docs': _mode = '3'
        elif run_code == '4' or run_code == 'build': _mode = '4'
        else: 
            raise AttributeError("\nSelect run mode:\n\t0=Development\n\t1=Production\n\t2=Testing\n\t3=Generate Documentation\n\t4=Build Mode\n")
        
        _mode_constants = constants(_mode)
        _path_to_application = _mode_constants.PATH_TO_APPLICATION

        """
        DEVELOPMENT, PRODUCTION, TESTING Modes

        All parameters for development, production, and testing modes are set via
        their respective dataclasses in constants.py.

        DOCUMENTATION Mode

        Configuration (yaml) file is built using data from the corresponding 
        dataclass in constants.py. Static documentation is generated using mkdocs
        tool.

        BUILD Mode

        The build mode is meant to be used to generate executable files. All 
        parameters should be built into the respective dataclass in constants.py.
        """
        if _mode in [DEVELOPMENT_MODE, PRODUCTION_MODE, TESTING_MODE]:
            print("You are running in", _mode_constants.RUN_MODE, "Mode.")
            cmd = ["python", _path_to_application]
            subprocess.run(cmd)
        
        elif _mode in [DOCUMENTATION_MODE]:
            print("You are running in", _mode_constants.RUN_MODE, "Mode.")
            doc_config = {
                'site_name': _mode_constants.PROJECT_NAME,
                'site_author': _mode_constants.PROJECT_AUTHOR,
                'theme': _mode_constants.THEME,
                'plugins': _mode_constants.PLUGINS,
                'use_directory_urls': _mode_constants.USE_DIRECTORY_URLS,
                'dev_addr': _mode_constants.DOCUMENTATION_LOCAL_IP,
                'markdown_extensions': _mode_constants.EXTENSIONS
            }

            yaml_output = yaml.dump(doc_config, sort_keys=False)
            with open("mkdocs.yaml",'w') as fd:
                fd.write(yaml_output)
                fd.close()
            
            cmd = ["mkdocs", "build"]
            subprocess.run(cmd)
        
        elif _mode in [BUILD_MODE]:
            print("Build Mode Not Supported yet")

        else:
            print(f"Mode {_mode} not yet supported")


        


#####################
#  RUN APPLICATION  #
#####################
if len(sys.argv) == 1:
    ApplicationRunner(DEVELOPMENT_MODE)     # Default mode = Development
elif len(sys.argv) == 2:
    ApplicationRunner(sys.argv[1])          # Read desired Run Mode
else:
    raise AttributeError("Too many arguments. Select run mode:\n\t0=Development\n\t1=Production\n\t2=Testing\n\t3=Generate Documentation\n\t4=Build Mode\n")
