###
# filename: bank3.py
# purpose: use bank.py class differently
# author: Dr. Johnson
# date: 2025-01-31
###

import bank    # must import using the file name

class AnotherBank:

   accountList = []
   MAX_ACCOUNTS = 5
   totalAssets = 0.0
   promptsList = ["   Account number: ", "   Name on account: ", "   Starting balance: "]
   accountValues = list()

   def __init__( self, count ):
      for j in range( count ):
         for i in range( len( self.promptsList ) ):
            self.accountValues.append( input( self.promptsList[i] ) )
         self.accountList.append( bank.CheckingAccount( self.accountValues[0], self.accountValues[1], self.accountValues[2] ) )
         self.accountValues.clear()

   def toString( self ):
      print( "\n\n   The bank has the following accounts:" )
      for i in range( len( self.accountList ) ):
         self.accountList[i].toString()

   def getTotal( self ):
      for i in range( len( self.accountList ) ):
         self.totalAssets += float( self.accountList[i].acctBal )
      return self.totalAssets

def makeBank():
   a = AnotherBank( AnotherBank.MAX_ACCOUNTS )
#   a = AnotherBank( 2 )
   a.toString()
   print( "\n   The bank has ${} in total assets.".format( a.getTotal() ) )

makeBank()



