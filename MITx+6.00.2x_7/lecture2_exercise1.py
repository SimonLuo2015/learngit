# generate all combinations of N items.
"""
Hi, I can try to help. Let's look at your scenario in which N=7. Or, N==7, if you want to be more Pythonic.
We know there are 2**7 or 128 options. If we represent these options in binary, then 0000000 corresponds to empty bag,
1111111 corresponds to bag with all seven items, and 0001111 corresponds to bag only containing the first four items.

Now to the program. We have some i , which, for the sake of example we let be 101 (1100101 in binary).
So the next pieces of code must generate what the 101st (actually 102nd, because of the possibility of i==0)
combo is and yield it.

Looking at the binary of 101, bit-by-bit, we know that this combo contains the first, third, sixth, and seventh items.
We want the program to do the same.

We need to look at the right number of bits, and there are N of these, hence the line for j in range(N):

Now we need to single out the bit we're looking for.
Let's say we're looking at the 6th bit from the right, the penultimate bit from the left.
This would mean our value of j would be five.
According to the Python Wiki page linked above, (i >> j) returns i with the bits shifted to the right by j places.
So (101 >> 5) would turn 101's binary, 1100101 into 11 (00101 is removed).
Then the modular operator singles out the last bit from the right,
meaning (i >> j) % 2 == 1 returns True and allows the jth item to be added to the combo if and
only if the jth bit of i is 1.

The section of code you highlighted will look at the binary of an integer i,
literally bit-by-bit, and if a bit is equal to one, it adds the item corresponding
to that bit to the combo corresponding to the integer i.

Let me know if I was able to help!
"""


def powerSet(items):
    N = len(items)
    # enumerate the 2**n possible combinations.
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                # print '---', items[j]
                combo.append(items[j])
        yield combo


#A simple test
def __test__():
    s = [1, 2, 3, 4]
    for e in powerSet(s):
        print '+++', e
    # print powerSet(s)

__test__()

def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as
      a list of which item(s) are in each bag.
    """
