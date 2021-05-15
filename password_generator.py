from random_password_creator import Password
import argparse


args = argparse.ArgumentParser()
args.add_argument('-c','--charset',required=True)
args.add_argument('-l','--length',default=8)
options = args.parse_args()
password = Password(options.charset,int(options.length))
password.set_char_array()
password.generate_password()
print('Your Random Password is: ',password.get_password())