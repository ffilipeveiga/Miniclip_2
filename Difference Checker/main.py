import os
import sys
import time
import json

def getFileContent(path):
    f = open(path, "r")
    return json.load(f)

# I assume that the json have been validated already at this point!
class DiferenceChecker:
    def __init__(self, campaign, campaign2):
        self.campaign = campaign
        self.campaign2 = campaign2
        self.differences = []
    
    def Checker():
        DiferenceChecker.nameChecker()


    def nameChecker(self):
        if self.campaign["name"] == self.campaign2["name"]:
            self.differences.append(f"The name is diferent.")
    
    def endChecker(self, condition):

        for key in  (self.campaign[condition]):
            if key not in self.campaign2[condition]:
                self.differences.append("The "+ self.campaign["name"] +" has " + key + " in the \"end\" and " + self.campaign2["name"] + " does not.")
                print(key)
            else:
                if key == "date":
                    DiferenceChecker.dateChecker(self, condition)
                if key == "duration":
                    DiferenceChecker.durationChecker(self, condition)
                if key == "event":
                    DiferenceChecker.eventChecker(self, condition)


    def startChecker(self, condition):

        for key in  (self.campaign[condition]):
            if key not in self.campaign2[condition]:
                self.differences.append("The "+ self.campaign["name"] +" has " + key + " in the \"start\" and " + self.campaign2["name"] + " does not.")
                print(key)
            else:
                if key == "date":
                    DiferenceChecker.dateChecker(self, condition)
                if key == "event":
                    DiferenceChecker.eventChecker(self, condition)

    def durationChecker(self, condition):
        if self.campaign[condition]["duration"] == self.campaign2[condition]["duration"]:
            self.differences.append(f"The {condition} duration is diferent.")

    def dateChecker(self, condition):
        if self.campaign[condition]["date"] == self.campaign2[condition]["date"]:
            self.differences.append(f"The {condition} date is diferent.")

    # I assume that the json have been validated at this point soo the event has a source and a identifier!
    def eventChecker(self, condition):
        if self.campaign[condition]["event"]["source"] == self.campaign2[condition]["event"]["source"]:
            self.differences.append(f"The {condition} even source is diferent.")

        if self.campaign[condition]["event"]["identifier"] == self.campaign2[condition]["event"]["identifier"]:
            self.differences.append(f"The {condition} even identifier is diferent.")

    # I assume that the json have been validated so the popup has art and transation and in the rigth format
    def popupChecker(self):
        DiferenceChecker.artChecker(self, "popup")
        DiferenceChecker.transactionChecker(self)
    
    def artChecker(self, condition):
        if self.campaign[condition]["art"] == self.campaign2[condition]["art"]:
            self.differences.append(f"The art {condition} is diferent.")
        
    def transactionChecker(self):
        if self.campaign["popup"]["transaction"]["price"] == self.campaign2["popup"]["transaction"]["price"]:
            self.differences.append(f"The price of the popup transaction is diferent.")
        if self.campaign["popup"]["transaction"]["item"] == self.campaign2["popup"]["transaction"]["item"]:
            self.differences.append(f"The item of the popup transaction is diferent.")    
        if self.campaign["popup"]["transaction"]["amount"] == self.campaign2["popup"]["transaction"]["amount"]:
            self.differences.append(f"The amount of the popup transaction is diferent.")
    
    def accessChecker(self):
        DiferenceChecker.artChecker(self, "access")


def main():
    path=sys.argv[1]
    path2=sys.argv[2]
    if os.path.isdir(path) and os.path.isdir(path2):
        for root, dirs, files in os.walk(path):
            for campaign_path in files:
                json_path=os.path.join(root,campaign_path)
                campaign = getFileContent(json_path)


                # print("!!!!!!!!!!!!!!!!!!!")
                # print(campaign_path)
                # print("!!!!!!!!!!!!!!!!!!!")

    elif os.path.isfile(path) and os.path.isfile(path2):
        campaign = getFileContent(path)
        campaign2 = getFileContent(path2)

        c1= DiferenceChecker(campaign, campaign2)
        c1.differences.append(f"Deferences between {path} and {path2}!")

        c1.nameChecker()
        c1.startChecker("start")
        c1.popupChecker()
        c1.accessChecker()
        c1.endChecker("end")

        diferences_list=c1.differences
        print(diferences_list)

        # print("\n")
        # errors_list= a.errors
        # print(errors_list)
    else:  
        print("The arguments passed must be a two files or two directories!!!" )

if __name__=="__main__":
    main()




  