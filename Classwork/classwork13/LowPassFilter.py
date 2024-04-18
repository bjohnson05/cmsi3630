###
# filename: LowPassFilter.py
# purpose: demonstrate calculations for low pass filter
# author: Dr. Johnson
# date: 2023-03-28
###

import math
import sys

impedance = 0.0
capacitance = 0.0
inductance = 0.0
cutoff_freq = 0.0
calc = 'a'

def listContains( a, b ):
   b = b.upper()
   for i in (range( len( a ) ) ):
      if a[i] == b:
         return i
   if i == (len( a ) - 1):
     return -1

def getParameters():

   global impedance
   global capacitance
   global inductance
   global cutoff_freq
   global calc

   if( len( sys.argv ) < 7 ):
      print( "\n\n   USAGE:\n" )
      print( "   python lowpassfilter L <value> C <value> F <value> ~OR~" )
      print( "   python lowpassfilter L <value> R <value> F <value> ~OR~" )
      print( "   python lowpassfilter R <value> C <value> F <value> ~OR~" )
      print( "   python lowpassfilter L <value> C <value> R <value> ~OR~" )
      print( "      any combination of three of the four pairs in any order.")
      print( "\n   Please try again!\n\n" )
   else:
      for i in sys.argv:
         i.upper()
      print( "   Entries: ", sys.argv )
      iCap = listContains( sys.argv, "C" ) + 1
      iInd = listContains( sys.argv, "L" ) + 1
      iImp = listContains( sys.argv, "R" ) + 1
      iFrq = listContains( sys.argv, "F" ) + 1
      if( iImp != 0 ):
         impedance = float( sys.argv[iImp] )
      else:
         calc = "R"
      if( iCap != 0 ):
         capacitance = float( sys.argv[iCap] )
      else:
         calc = "C"
      if( iInd != 0 ):
         inductance = float( sys.argv[iInd] )
      else:
         calc = "L"
      if( iFrq != 0 ):
         cutoff_freq = float( sys.argv[iFrq] )
      else:
         calc = "F"
   return

def calcInductance( capacitance, cutoff_freq, impedance ):
   inductance = impedance / (2 * math.pi * cutoff_freq)
   return inductance * 1000

def calcCapacitance( inductance, cutoff_freq, impedance ):
   capacitance = 1 / (math.pi * cutoff_freq * impedance)
   return capacitance * 1000000

def calcImpedance( capacitance, cutoff_freq, inductance ):
   impedance = math.pi * cutoff_freq * inductance
   return impedance

def calcFrequency( capacitance, inductance, impedance ):
   cutoff_freq = 1 / (math.pi * math.sqrt( inductance * capacitance ) )
   return cutoff_freq

def main():

   global impedance
   global capacitance
   global inductance
   global cutoff_freq
   global calc

   getParameters()
   print( "   Calc value: ", calc )
   if( calc == "F" ):
      cutoff_freq = calcFrequency( capacitance, inductance, impedance )
   elif( calc == "R" ):
      impedance = calcImpedance( capacitance, cutoff_freq, inductance )
   elif( calc == "C" ):
      capacitance = calcCapacitance( inductance, cutoff_freq, impedance )
   elif( calc == "I" ):
      inductance = calcInductance( capacitance, cutoff_freq, impedance )
   print( "\n   Resulting filter for a cutoff frequency of {:.3f} Hz".format( cutoff_freq ) )
   print( "   Use an inductor of {:.5f} millihenries, and".format( inductance ) )
   print( "       a capacitor of {:.5f} microfarads, and".format( capacitance ) )
   print( "       it will match an impedence of ", impedance, " ohms." )

main()
