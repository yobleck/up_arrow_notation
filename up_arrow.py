# Name:        up arrow notation
# Purpose:      see above
# Author:      YOBLECK
# Created:     22/07/2019
# Copyright:   (c) YOBLECK 2019
# Licence:     creative commons or whatever
#-------------------------------------------------------------------------------
import math;


def up_arrow (a,n,b):
	print ("up_arrow");
	if n==1:
		return a**b;
	elif n>=1 and b==0:
		return 1;
	else:
		return up_arrow(a,n-1,up_arrow(a,n,b-1));

#anything above 2 or 3 will f u up
print(up_arrow(2,2,6));
