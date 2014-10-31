import sys
import argparse

parser = argparse.ArgumentParser(description="Find consecutive numbers that add up to create the given polite number. This script was created by redrails")
parser.add_argument("-p", "--polite", help="Polite number to process", required=True)
args = vars(parser.parse_args())

if args['polite'] > 0:

	input_var = int(args["polite"])

	if input_var%2 == 0:
		print "Not a polite number. \n"
		quit()

	print("\n")

	print "Using integer: ", input_var

	input_divide = input_var/2
	input_div_1 = str(input_divide)
	input_div_2 = str(input_divide+1)

	print("\n")

	print "The polite number derives from the consecutive numbers: "+ input_div_1 +" and "+ input_div_2

	print("\n")
else:
	print "Number must be greater than 0"
