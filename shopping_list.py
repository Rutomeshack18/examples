#!/bin/bash
#Searching Items on a shopping cart
shopping_cart = ["bread", "eggs", "tissue", "sugar"]
item_found = False
while not item_found:
	item= input("Enter the item or 'q' to quit: ")
	if item.lower() == "q":
		break
	else
