from licensing.models import *
from licensing.methods import Key, Helpers
import os ,socket
from tkinter import simpledialog
from datetime import *
    def activateTrial():
        trial_key = Key.create_trial_key("WyIyMTMzNDEiLCJiN1JuRzK3RaOU0yekQxa1hSWTJYN2RsT2VMWDE4UG1Ibk1yQnc5Il0=", 87, Helpers.GetMachineCode())

        if trial_key[0] == None:
            print("An error occurred:dcdc {0}".format(trial_key[1]))
            
        RSAPubKey = "<RSAKeyValue><Modulus>1d1jyuGWHA5f767Iu9EEJN3Uy2D1SgO+5vppD8u9alJggeoJDuDNjL+6o5fMEgfacgD4OweEV+eG6IV5EbFrjJe5L2ay9Hidn6bQUt67hA8z2G112imLnN9h6CkRQFBCC6ew+M73rCSO/Phhfzs/XeYx9YeCv2HSz91HNJG/KDEXbv4bPges5ihIq5nW6Jq5MKyy4F9aN3P/HEQrtsNb+dSslkI3j9aEUufBAMoMgbSo0oUvQ1oQlvqovFqTPqwnEee7LDHUkVgV9BnJJYDw9wQUowlWuyIsokVQVRDtyXKMeBADp9L8KWFTYRELAd+EOFr14eHEDw1oGgkm1e5tkw==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"
        auth = "WyIyMTMzNDEiLCJiN1JuRzK3RaOU0yekQxa1hSWTJYN2RsT2VMWDE4UG1Ibk1yQnc5Il0="
        
        result = Key.activate(token=auth,\
                                 rsa_pub_key=RSAPubKey,\
                                 product_id=87, \
                                 key=trial_key[0],\
                                 machine_code=Helpers.GetMachineCode(),\
                                 friendly_name=socket.gethostname())
        
        if result[0] == None or not Helpers.IsOnRightMachine(result[0]):

            b = False

        else:
            license_key = result[0]
            result = tkinter.messagebox.showinfo('The trial period ends on' , str(license_key.expires))
            root.mainloop()
            b = True
        return b

    def newactivate():
       
        pubKey = "<RSAKeyValue><Modulus>1d1jyuGWHA5f767Iu9EEJN3Uy2D1SgO+5vppD8u9alJggeoJDuDNjL+6o5fMEgfacgD4OweEV+eG6IV5EbFrjJe5L2ay9Hidn6bQUt67hA8z2G112imLnN9h6CkRQFBCC6ew+M73rCSO/Phhfzs/XeYx9YeCv2HSz91HNJG/KDEXbv4bPges5ihIq5nW6Jq5MKyy4F9aN3P/HEQrtsNb+dSslkI3j9aEUufBAMoMgbSo0oUvQ1oQlvqovFqTPqwnEee7LDHUkVgV9BnJJYDw9wQUowlWuyIsokVQVRDtyXKMeBADp9L8KWFTYRELAd+EOFr14eHEDw1oGgkm1e5tkw==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"

        USER_code = simpledialog.askstring("Activate Program" , " Enter the activation code that was sent to you")
        res = Key.activate(token="WyIyMTMzNDEiLCJiN1JuRzRqK3RaOU0yekQxa1hSWTJYN2RsT2VMWDE4UG1Ibk1yQnc5Il0=",\
                                   rsa_pub_key=pubKey,\
                                   product_id=8704, key=USER_code,machine_code=Helpers.GetMachineCode(),friendly_name=socket.gethostname())
        if res[0] == None or not Helpers.IsOnRightMachine(res[0]):
            print("An error occured: {0}".format(res[1]))
            result = tkinter.messagebox.showinfo('Invalid activation code' , str(format(res[1])))
            a = False

        else:
            
            license_key = res[0]
            l = (str(license_key.expires))
            d = (str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            if l < d:
                    
                result = tkinter.messagebox.showinfo('Your license has expired, please renew' , " EXPIRED " +  "\n" + str(license_key.expires))        
                newactivate()
    
            else:         
                result = tkinter.messagebox.showinfo('Your license  expired AT' , str(license_key.expires))
                root.mainloop()
                if res[0] != None:
                # saving license file to local disk
                    with open('resources/licensefile.skm', 'w') as f:
                        f.write(res[0].save_as_string())   
                a = True
            
        return a 
            
    def check():

        file = "resources/licensefile.skm"
        if os.path.isfile(file)==True:
        

            with open('resources/licensefile.skm', 'r') as f:
                pubKey = "<RSAKeyValue><Modulus>1d1jyuGWHA5f767Iu9EEJN3Uy2D1SgO+5vppD8u9alJggeoJDuDNjL+6o5fMEgfacgD4OweEV+eG6IV5EbFrjJe5L2ay9Hidn6bQUt67hA8z2G112imLnN9h6CkRQFBCC6ew+M73rCSO/Phhfzs/XeYx9YeCv2HSz91HNJG/KDEXbv4bPges5ihIq5nW6Jq5MKyy4F9aN3P/HEQrtsNb+dSslkI3j9aEUufBAMoMgbSo0oUvQ1oQlvqovFqTPqwnEee7LDHUkVgV9BnJJYDw9wQUowlWuyIsokVQVRDtyXKMeBADp9L8KWFTYRELAd+EOFr14eHEDw1oGgkm1e5tkw==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"
                license_key = LicenseKey.load_from_string(pubKey, f.read(),30) ## you can add How many days you want before function return NoneType
        
            if not Helpers.IsOnRightMachine(license_key):
                        
                newactivate()
                print("NOTE: This license file does not belong to this machine.")
                
            else: #compare 
                l = (str(license_key.expires))
                d = (str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
                if l < d:
                    
                    result = tkinter.messagebox.showinfo('Your license has expired, please renew' , " " +  "\n" + str(license_key.expires))        
                    newactivate()
    
                else:         
                    result = tkinter.messagebox.showinfo('The license will expire at ' , str(license_key.expires))
                    root.mainloop()
        elif activateTrial()==True: 
            
            pass
            
        elif newactivate()==True: 
            
            pass
            
        else:
            check()
check()
