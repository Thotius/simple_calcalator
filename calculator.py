#

from math import *
import sys
import time
import argparse

#I will use this library in the future

parser = argparse.ArgumentParser()
parser.parse_args()
print()

print("""
	       ##################
	      ###            ###
	     ### CALCULATOR ###
	    ### Created by ###
	   ###   Th1460   ###
	  ###    2018    ###
	 ###            ###
	##################
		""")
		
time.sleep(2)
print()
print("	Loading Program... Please wait...\n")
time.sleep(2)

print("""
	[+] Select the option [+]
	
	[1] - ADD -
	[2] - SUB -
	[3] - MUL -
	[4] - DIV -
	[5] - SQRT -
		""")

while True:
	print()
	option = input("   Enter the option, '0' for exit: ")
	print()
	
	if option == '0':
		time.sleep(2)
		print("   [!] System exit. See you soon...\n")
		sys.exit()
	
	f_number = float(input("\n    Enter a number, in 'sqrt' enter 0 for 2nd number: "))
	s_number = float(input("\n    Enter a number: "))
	
	print()
	
	if option == '1':
		summ = (f_number) + (s_number)
		print("  [*] The sum is %0.1f" %summ)
		
	elif option == '2':
		sub = (f_number) - (s_number)
		print("  [*] The sub is %0.1f" %sub)
		
	elif option =='3':
		mul = (f_number) * (s_number)
		print("  [*] The mul is %0.1f" % mul)
		
	elif option == '4':
		div = (f_number) / (s_number)
		print("  [*] The div is %0.1f" %div)
		
	elif option == '5':
		sqart = (sqrt(f_number))
		print("  [*] The sqrt is %0.3f" %sqart)
		
	else:
		print("  [*] - Invalid Option")
		
