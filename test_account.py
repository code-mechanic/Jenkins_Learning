import pytest
import account as acc

def test_passwordLen():
    accInfo = acc.account()
    print("Checking possible password")
    pw_list = ["mohanmohan", "iamfromindia", "loneanimal"]

    for each in pw_list:
        print("Checking password "+each+"\n")
        passInfo = accInfo.countLen(each)
        if(passInfo > 8):
            print("ok")
    
