import os
import sys
import time
import json
from campaingn import validation

def getFileContent(path):
    f = open(path, "r")
    return json.load(f)

def validateCampaingn(campaign):
    c=validation.Validation(campaign)
    return c


def main():
    if len(sys.argv)!=2:
        print("Wrong arguments!")
        return

    path=sys.argv[1]
    if os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for campaign_path in files:
                json_path=os.path.join(root,campaign_path)
                print("!!!!!!!!!!!!!!!!!!!")
                print(campaign_path)
                print("!!!!!!!!!!!!!!!!!!!")
                campaign = getFileContent(json_path)
                validateCampaingn(campaign)
                a=validateCampaingn(campaign)
                a.validate()
    elif os.path.isfile(path):
        campaign = getFileContent(path)
        print("\n")
        a=validateCampaingn(campaign)
        a.validate()
        print("\n")
        errors_list= a.errors
        print(errors_list)
    else:  
        print("The argument passed must be a file or directory!!!" )

if __name__=="__main__":
    main()
