###
# filename: bank.py
# purpose: demo
# author: Dr. Johnson
# date: 2025-01-29
###

class CheckingAccount:

   acctNum = ""
   acctName = ""
   acctBal = 0.0

   def __init__( self, aNum, aName, aBal ):
      self.acctNum = aNum
      self.acctName = aName
      self.acctBal = aBal

   def setNum( self, newNum ):
      self.acctNum = newNum

   def setName( self, newName ):
      self.acctName = newName

   def setBal( self, newBal ):
      self.acctBal = newBal

   def toString( self ):
      print( "\n\n   Account #: ", self.acctNum )
      print( "   Name on account: ", self.acctName )
      print( "   Account balance: ", self.acctBal )
      print( "\n\n" )

def test():
   ac1 = CheckingAccount( "L23B92X", "bozo derimini", 1234.56 )
   ac1.toString()

   ac2 = CheckingAccount( "L23B93X", "lolly gagger", 1000000.00 )
   ac2.toString()

test()
