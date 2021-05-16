from __future__ import print_function
 
# Variables Used
sharedPrime = 23    # p
sharedBase = 5      # g
 
aliceSecret = 6     # a
bobSecret = 15      # b
 
# Begin
print( "Publicly Shared Variables:")
print( "    Publicly Shared Prime: " , sharedPrime )
print( "    Publicly Shared Base:  " , sharedBase )
 
# Alice Sends Bob A = g^a mod p
A = (sharedBase**aliceSecret) % sharedPrime
print( "\n  Alice Sends Over Public Chanel: " , A )
 
# Bob Sends Alice B = g^b mod p
B = (sharedBase ** bobSecret) % sharedPrime
print( "   Bob Sends Over Public Chanel: ", B )
 
print( "\n------------\n" )
print( "Privately Calculated Shared Secret:" )
# Alice Computes Shared Secret: s = B^a mod p
aliceSharedSecret = (B ** aliceSecret) % sharedPrime
print( "    Alice Shared Secret: ", aliceSharedSecret )
 
# Bob Computes Shared Secret: s = A^b mod p
bobSharedSecret = (A**bobSecret) % sharedPrime
print( "    Bob Shared Secret: ", bobSharedSecret )

#if bobSharedSecret = aliceSharedSecret then success

####################output#######################
Publicly Shared Variables:
    Publicly Shared Prime:  23
    Publicly Shared Base:   5

  Alice Sends Over Public Chanel:  8
   Bob Sends Over Public Chanel:  19

------------

Privately Calculated Shared Secret:
    Alice Shared Secret:  2
    Bob Shared Secret:  2

