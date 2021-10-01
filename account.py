class account:
    def countLen(self, pw):
        if(len(pw) > 8):
            return True
        else:
            return False

if __name__ == "__main__":
    accVerify = account()
    if (accVerify.countLen("MOHAN")):
        print("The password length is less than expected")
    else:
        print("The password length critera passed")
