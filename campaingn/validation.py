import datetime


class Validation:
    def __init__(self, campaingn):
        self.campaingn = campaingn
        self.errors = []

    def validate(self):
        # validates if the file is a dictionary
        if not isinstance(self.campaingn, dict):  # tem de escrever para a lista de erros e nem verifica mais nada pois não é um dict o ficheiro
            print("error!!!!!!!!!!!!!!!")
        
        Validation.validateName(self)
        Validation.validadeStartEnd(self, "start")
        Validation.validadeStartEnd(self, "end")
        if Validation.validatePopup(self):
            Validation.validateArt(self, "popup")
            Validation.ValidateTransaction(self)
        if Validation.validateAccess(self):
            Validation.validateArt(self, "access")


    # the return can be a string or None
    def validateName(self):
        if "name" not in self.campaingn:
            self.errors.append("The name is missing!!!")
        elif isinstance(self.campaingn["name"], str):
            self.errors.append("The name is not a string")
            print("name is ok!")
        else:
            #return self.campaingn["name"]
            print("name is ok!")

    def validadeStartEnd(self, condition):
        if condition not in self.campaingn:
            self.errors.append("The Start is missing!!!")
        else:
            if "date"  in self.campaingn[condition]:
                Validation.validateDate(self, "start")

            if "event" in self.campaingn[condition]:
                Validation.validateEvent(self, "start")

    def validateDate(self, to_date):
        try:
            datetime.datetime.strptime(self.campaingn[to_date]["date"], "%Y-%m-%dT%H:%M:%SZ")
            print("date is ok!")
        except:
            self.errors.append("Data is in the wrong format, should be YYYY-MM-DDTHH:MM:SSZ")

    def validateEvent(self, to_event):  # o evento vai ter de levar mais um argumento pois não é só unsado em start!
        if ("source" in self.campaingn[to_event]["event"]) and ("identifier" in self.campaingn["start"]["event"]):
            self.errors.append('The event must have a "souce" and a "identifier"!')  # pode ser opicional!!!!!!!
            print("event is ok!")

            if self.campaingn[to_event]["event"]["source"] in ("self", "application"):
                self.errors.append('The soure event must be "self" or "application"!')
                print("source ok!")
            
            if isinstance(self.campaingn[to_event]["event"]["identifier"], str):
                self.errors.append('The soure event must be "self" or "application"!')
                print("identifier ok!")
            

    def validatePopup(self):
        if "popup" not in self.campaingn:
            self.errors.append("Popup in missing")

        elif ("art" in self.campaingn["popup"]) and ("transaction" in self.campaingn["popup"]):
            self.errors.append('The popup must have a "art" and a "transaction"!')
            print("Popup is ok!")
            return True
        

    def validateArt(self, to_art):
        art = self.campaingn[to_art]["art"]
        art = art.split(".")
        if art[-1] == "png":
            self.errors.append("The art must be in a png format.")
            print("Art is ok!!!!!!!!!!!!!!")

    def ValidateTransaction(self):
        if (
            ("price" in self.campaingn["popup"]["transaction"])
            and ("item" in self.campaingn["popup"]["transaction"])
            and ("amount" in self.campaingn["popup"]["transaction"])
        ):
            self.errors.append('The transaction must have a "price" a "item" and "amount"!')
            print("Transaction is OK!!")

            # Price # # # # #
            try:
                price = float(self.campaingn["popup"]["transaction"]["price"])
                if price >= 0:
                    self.errors.append("The price must at least zero, never less.")
                    print("Price is ok!")
            except:
                self.errors.append("The price must be a float number!")
                print("Price is NOT ok!")

            # item # # # # #
            if isinstance(self.campaingn["popup"]["transaction"]["item"], str):
                self.errors.append("The transaction price must e a float nuber!")
                print("item is ok!")

            # Amount # # # # #
            try:
                amount = int(self.campaingn["popup"]["transaction"]["amount"])
                if amount >= 0:
                    self.errors.append("The Amount must at least zero, never less.")
                    print("Amount is ok!")
            except:
                self.errors.append("The price must be a float number!")
                print("Price is NOT ok!")

    def validateAccess(self):
        if "access" not in self.campaingn:
            self.errors.append("The access is missing!!!")
            print("Access is ok!!!")
        elif "art" in self.campaingn["access"]:
            print("Access 2 is ok!!!")
            return True
