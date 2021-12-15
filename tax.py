#!/usr/bin/env python3
# Created by: Billy Terimpundu 
# Created on: December 2021
# This program asks the user for the subtotal of the
# purchase. It then calculates and displays the total cost
# of the purchase with Alberta's HST (15%)
import constants


def main():
  # input
  subtotal = float(input("Enter the subtotal of the purchase :"))

  # process
  tax = constants.HST * subtotal
  total = subtotal + tax

  # output
  print("")
  print("The total cost is = ${:.2f}".format(total))


if __name__ == "__main__":
   main()