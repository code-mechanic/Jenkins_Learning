class account:
    def countLen(self, pw):
        if(len(pw) > 8):
            return True
        else:
            return False

if __name__ == "__main__":
    accVerify = account()
    print("The password length is" + str(accVerify.countLen("MOHAN")))
