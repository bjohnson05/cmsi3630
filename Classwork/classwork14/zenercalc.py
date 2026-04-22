###
# filename: zenercalc.py
# purpose: calculate the minimum zener diode current
#           of a circuit
# author:   Dr. Johnson
# date:     2023-04-16
###

import sys

def calcRsCurrent( Vin, Vout, Rseries ):
   return (Vin - Vout) / Rseries

def calcMaxLoadCurrent( Vout, Rmin ):
   return Vout / Rmin

def calcMinZenerCurrent( I_Rseries, I_MaxLoadCurrent ):
   return I_Rseries - I_MaxLoadCurrent

def main():
   if( len( sys.argv ) < 5 ):
      print( "\n\n   This program calculates the minimum Zener current" )
      print( "   through a Zener diode.  Enter the power supply voltage," )
      print( "   the zener breakdown voltage, the series resistance, and" )
      print( "   the [minimum] load resistance." )
      Vin, Vout, Rs, Rmin = map( float, input( "      Enter ==> " ).split( " " )[:4] )
   else:
      Vin, Vout, Rs, Rmin = map( float, sys.argv[1:] )
   print( "\n\n   OK, Vin: ", Vin, ", Vzener: ", Vout, end = "" )
   print( ", Rseries: ", Rs, ", and Rmin: ", Rmin )
   print( "\n   Minimum Zener Current: ", \
      calcMinZenerCurrent( calcRsCurrent( Vin, Vout, Rs ), \
      calcMaxLoadCurrent( Vout, Rmin ) ) * 1000.0, " milliamps" )

main()
