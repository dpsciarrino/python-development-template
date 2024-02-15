import pathlib
from dataclasses import dataclass

'''
Run Modes
'''
DEVELOPMENT_MODE: str = '0'
PRODUCTION_MODE: str = '1'
TESTING_MODE: str = '2'
DOCUMENTATION_MODE: str = '3'
BUILD_MODE: str = '4'

def constants(mode: str = DEVELOPMENT_MODE):
    """
    Returns the dataclass associated with the desired run mode.
    """
    # Development Mode
    if mode == DEVELOPMENT_MODE:
        return DevelopmentConstants()
    
    # Production Mode
    elif mode == PRODUCTION_MODE:
        return ProductionConstants()
    
    # Testing Mode
    elif mode == TESTING_MODE:
        return TestingConstants()
    
    # Documentation Mode
    elif mode == DOCUMENTATION_MODE:
        return DocumentationConstants()
    
    # Build Mode
    elif mode == BUILD_MODE:
        return BuildConstants()
    
    # Fail
    else:
        raise AttributeError("\nSelect run mode:\n\t0=Development\n\t1=Production\n\t2=Testing\n\t3=Generate Documentation\n\t4=Build Mode\n")


@dataclass(frozen=True)
class BaseConstants:
    '''
    Defines the filname of the main application
    '''
    APPLICATION_FILENAME = "main.py"

    '''
    Defines the absolute file path for running the application
    '''
    PATH_TO_APPLICATION = str(pathlib.Path(f"./src/{APPLICATION_FILENAME}").absolute())

    '''
    General Application folders
    '''
    SRC_DIRECTORY = str(pathlib.Path(f"./src").absolute())

    '''
    Project Name
    '''
    PROJECT_NAME = "Python Project Template"

    '''
    Project Author
    '''
    PROJECT_AUTHOR = "Dominic Sciarrino"
    


@dataclass(frozen=True)
class DevelopmentConstants(BaseConstants):
    RUN_MODE = "Development"

@dataclass(frozen=True)
class ProductionConstants(BaseConstants):
    RUN_MODE = "Production"

@dataclass(frozen=True)
class TestingConstants(BaseConstants):
    RUN_MODE = "Test"

@dataclass(frozen=True)
class DocumentationConstants(BaseConstants):
    RUN_MODE = "Documentation"

    '''
    Path to Documentation Markdown Files
    '''
    DOC_PATH = str(pathlib.Path("./docs").absolute())

    '''
    Navigation Bar Settings

    None = no navigation bar

    Example:
        nav = [
            {
                "Navigation Label": "MarkdownFile.md"
            },
            ...
        ]
    '''
    NAV = None

    '''
    Markdown Theme
    '''
    THEME = {
        'name':'material',
        'locale':'en'
    }
    
    '''
    Markdown Plugins
    '''
    PLUGINS = ['mkdocstrings']

    '''
    Allows for viewing documentation on local disk
    '''
    USE_DIRECTORY_URLS = False

    '''
    IP Address for accessing local documentation.
    '''
    DOCUMENTATION_LOCAL_IP = "127.0.0.1:5000"

    '''
    Markdown Extensions
    '''
    EXTENSIONS = [
        {
            'toc':{
                'toc_depth':'1-1'
            }
        }
    ]



@dataclass(frozen=True)
class BuildConstants(BaseConstants):
    RUN_MODE = "Build"