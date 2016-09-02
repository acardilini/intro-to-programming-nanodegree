import os
import string

def rename_files():
    files = os.listdir("/Users/jess/adam/ipnd-starter-code-master/stage_3/lesson_3.2_using_functions/secret_message/prank")
    saved_path = os.getcwd()
    print("Current Working Directory is "+saved_path)
    os.chdir("/Users/jess/adam/ipnd-starter-code-master/stage_3/lesson_3.2_using_functions/secret_message/prank")
    for filename in files:
        print("Old filename is "+filename)
        print("New filename is "+filename.translate(None, digits))
        os.rename(filename, filename.translate(None, digits))
    os.chdir(saved_path)

rename_files()
