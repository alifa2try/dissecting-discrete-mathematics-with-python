#!/usr/bin/env python

# Given X = { 0, 1, 2 } and Y = { 0, 1 }, 
# Write a program to find the cartesian product of (i.) X and Y (ii.) Y x X.

import itertools
import argparse


def get_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-X", dest='X', help="The first set")
	parser.add_argument("-Y", dest='Y', help="The second set")
	
	option = parser.parse_args()

	if not option.X:
		parser.error("[+] You need to input set X" )
		raise SystemExit

	if not option.X:
		parser.error("[+] You need to input set Y" )
		raise SystemExit

	return option		


def X_x_Y(X, Y):
	
	cartesian_product = itertools.product(X, Y)
	cartesian_list = list(cartesian_product)

	return cartesian_list


def element_list(X):
	
	element_list = []
	element = X.split(',')
	element_list += element

	return element_list



option = get_arguments()

X = element_list(option.X)
Y = element_list(option.Y)


print(f"[+] The cartesian product of the sets X = {X} and Y = {Y} is: X x Y = {X_x_Y(X, Y)}")
print(f"\n\n [+] The cartesian product of the sets Y = {Y} and X = {X} is: Y x X = {X_x_Y(Y, X)}")


