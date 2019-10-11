#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)

O(n)
I believe this algorithm will have O(n) time complexity because even though the while loop specifies (n _ n _ n) we iterate a by n _ n every time. So rather than completing the program in n _ n \* n steps, it really only takes more like n steps.

b)

O(nlogn)
This algorithm should have O(nlogn) time complexity because it's outer loop will iterate at least n times. Its inner loop however iterates by j \* 2 every time, so rather than O(n^2), this algorithm will take O(nlogn) steps

c)

O(n)
Even though this function is recursive, we will still iterate through most of bunnies, so O(n)

## Exercise II

n floors
eggs dropped from floor >= f breaks
eggs dropped from floor < f does not break
Minimize broken + dropped eggs

Linear O(n)

1. Start at the bottom floor
2. We have dropped 0 eggs and 0 eggs have broken
3. Drop an egg, and iterate our dropped eggs by 1
4. Check if the egg is broken: if so iterate broken eggs by 1, this is our f, stop dropping eggs
5. If we have reached the top floor, if we can assume every building has an f, we don't need to drop an egg here, exit the loop this is our f. If there is a chance this building does not have an f, we should still drop an egg and continue the loop.
6. Otherwise move up a floor, start at step 3

## Notes

I originally thought binary search would be better, since it's faster, but if our f is the first floor we break more eggs.

1. Start at the middle floor
2. We have dropped 0 eggs and 0 eggs have broken
3. Store something that lets us know if an egg broke on a floor. Probably a dictionary with floors as the key and a boolean for the value
4. Drop an egg, and iterate our dropped eggs by 1
5. Check if the egg is broken: if so, check if we've broken any eggs on the floor prior. If we have, did the egg break? If the egg broke on the floor below this, we need to keep looking for f. Treat this floor as the top floor, and go the the middle floor between this one and the bottom.
6. But if we are on a broken egg floor, and the floor one below this one did not break an egg, this must be our f
7. If the egg did not break, our f must be higher, treat this floor as the bottom floor and move to the middle floor between this one and the top one and repeat these steps from 3
