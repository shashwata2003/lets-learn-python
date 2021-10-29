# FROG in the Well
# A frog is at the bottom of a X meter well. Each day he summons enough energy for one Y meter leap up the well. Exhausted, he then hangs there for the rest of the day. At night, while he is asleep, he slips Z meters backwards. How many days does it take him to escape from the well? Note: Assume after the first leap that his hind legs are exactly three meters up the well. His hind legs must clear the well for him to escape

# Input

# X

# Y

# Z

# Output

# Number of days required for thr frog  to come out of the well (Exclude the day on which he comes out)
X=int(input())
Y=int(input())
Z=int(input())
a=X-3
b=Y-Z
c=a//b
print(c)