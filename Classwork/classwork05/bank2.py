###
# filename: bank2.py
# purpose: use bank.py class
# author: Dr. Johnson
# date: 2025-01-31
###

import bank    # must import using the file name

class MyBank:

   accountList = []
   MAX_ACCOUNTS = 5
   totalAssets = 0.0

   def __init__( self ):
      print( "\n\n" )
      for i in range( self.MAX_ACCOUNTS ):
         number  = input( "   Account number: " )
         owner   = input( "   Name on account: " )
         balance = input( "   Starting balance: " )
         self.accountList.append( bank.CheckingAccount( number, owner, balance ) )
         print( "\n" )

   def toString( self ):
      for i in range( self.MAX_ACCOUNTS ):
         self.accountList[i].toString()

   def totalBank( self ):
      for i in range( self.MAX_ACCOUNTS ):
         self.totalAssets += float( self.accountList[i].acctBal )
      print( "\n\n   Total assets of the bank: ", self.totalAssets )

def test():
   mb1 = MyBank()
   mb1.toString()
   mb1.totalBank()

test()
