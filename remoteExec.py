#Authors: Nate Glod

import subprocess
import sys

def main(imgURI):
    HOST="laptop.n8.glod"

    COMMAND= 'cd ~/Documents/DeepYeet
    virtualenv --python python3 env
    export GOOGLE_APPLICATION_CREDENTIALS="BrickHack5-9f098798b17b.json"
    python3 identifyCompany.py ' + imgURI

    ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
            shell=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
    result = ssh.stdout.readlines()
    if(result == []){
        return "Error: Something done fucked"
    elif(result == "No logos detected"):
        return 0
    else:
        return result
    

if __name__== "__main__":
  main(imgURI)
