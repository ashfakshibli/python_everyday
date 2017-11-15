"""

Most Python code is either a module to be imported, or a script that does something. 
However, sometimes it is useful to make a file that can be both imported as a module and run as a script. 
To do this, place script code inside if __name__ == "__main__". 
This ensures that it won't be run if the file is imported.

"""


import main

main.function()