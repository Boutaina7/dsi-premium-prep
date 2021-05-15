# Statistical counting
* Factorial
* Permutations
* Combinations


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Factorial: $n!$
*  Can be thought of as the cardinality, or number of ways, that $n$ items can be arranged.
    * Ex: $9!=9 \times 8 \times 7 \times 6 \times 5 \times 4 \times 3 \times 2 \times 1=362880$
    * Note: $0!=1$, as there is only one way to arrange zero items.


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Factorial and selecting without replacement
Consider selecting 3 numbered balls from an urn, without replacement:
* In the first selection, there are 3 choices
* In the second selection, there are 2 choices
* In the thrid selection, there is 1 choice

Possible Sequences:

| Selection One | Selection Two | Selection Three|
|---------------|---------------|----------------|
|  <center>1</center> | <center>2</center> | <center>3</center>|
|  <center>1</center> | <center>3</center> | <center>2</center>|
|  <center>2</center> | <center>1</center> | <center>3</center>|
|  <center>2</center> | <center>3</center> | <center>1</center>|
|  <center>3</center> | <center>1</center> | <center>2</center>|
|  <center>3</center> | <center>2</center> | <center>1</center>|


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (3 minutes) code `factorial()`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT Solution

```python
def factorial(num):
    prod = 1
    for n in range(2, num+1):
        prod *= n
    return prod
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (3 minutes)

There are ten people standing in a line for beignets at the world famous cafe du monde in New Orleans. How many different ways could the ten people be arranged in the queue?


Given that the line was formed organically (i.e, people got into line as they arrived without any organization or coordination), what is the probability that they are standing in the queue in alphabetical order. Assume everyone has a different last name?


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT Solution

There are ten people standing in a line for beignets at the world famous cafe du monde in New Orleans. How many different ways could the ten people be arranged in the queue?
* Solution: $10! = 10 \times 9 \times 8 \times 7 \times 6 \times 5 \times 4 \times 3 \times 2 \times 1 = 3628800$


Given that the line was formed organically (i.e, people got into line as they arrived without any organization or coordination), what is the probability that they are standing in the queue in alphabetical order. Assume everyone has a different last name?
* Solution: $\frac{1}{3628800} \approx .0000003$





<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Permutations: $nPk = \frac{n!}{(n-k)!}$
* A **permutation** can be thought of as an arrangement of a number of items
* $nPk$
    * where $n$ is the number of possible items
    * $k$ is how many of those items to arrange
* Note: **ORDER MATTERS**


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Permutations: Discovery by Counting
$nPk = \frac{n!}{(n-k)!}$

If we consider $n$ to be the base of a counting system, then we can determine all permutations $k$ by a counting/reduction approach.

1. Count in base $n$ system
* ex: $n=3$

000 010 020 100 110 120 200 210 220
001 011 021 101 111 121 201 211 221
002 012 022 102 112 122 202 212 222
                            
2. **Reduce** counts that have duplicate items

000 010 020 100 110 **120** 200 **210** 220
001 011 **021** 101 111 121 **201** 211 221
002 **012** 022 **102** 112 122 202 212 222

3. Consider $k$ items

ex: $k=3$

|012 | 021 | 102 | 120 | 201 | 210| 
|----|-----|-----|-----|-----|-----|

ex: $k=2$
| 12 | 21 | 02 | 20| 01|  10|
|-----|-----|-----|-----|-----|-----|

ex: $k=1$ 
| 2 | 1 | 0 |
|-----|-----|-----|


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (3 minutes)
Code the `permutations(n,k)` function


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT Solution
Code the `permutations(n,k)` function

```python
def permutations(n, k):
    return int(factorial(n) / factorial(n-k))
```

Slightly more optimized:

```python
def permutations(n, k):
    perm = 1
    for i in range(n, n-k, -1):
        perm *= i
    return perm
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (2 minutes)
$nPk = \frac{n!}{(n-k)!}$

You have 10 students and you are conducting a science fair where 4 students will win 1st, 2nd, 3rd, 4th. How many different arrangements of those 4 winners is possible?



<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION (3 minutes)
You have 10 students and you are conducting a science fair where 4 students will win 1st, 2nd, 3rd, 4th. How many different arrangements of those 4 winners is possible?

$$
nPk = \frac{n!}{(n-k)!}
$$

$$
10P4 = \frac{10!}{(10-4)!}
$$

$$
10P4 = \frac{10 \times 9 \times 8 \times 7 \times 6 \times 5 \times 4 \times 3 \times 2 \times 1}{(6 \times 5 \times 4 \times 3 \times 2 \times 1)}
$$

$$
10P4 = \frac{10 \times 9 \times 8 \times 7 \times \cancel{6 \times 5 \times 4 \times 3 \times 2 \times 1}}{\cancel{(6 \times 5 \times 4 \times 3 \times 2 \times 1)}}
$$

$$
10P4 = 10 \times 9 \times 8 \times 7 = 5040
$$

There are 5040 different possible ways for the 10 students to win the 1st, 2nd, 3rd, and 4th prizes.


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Permutations Intuition (Reductive Approach)
1. Count in Base $n$ system
2. Reduce space by removing outcomes with duplicate items

Five pets and 5 beds. What are all the ways that you can
arrange those 5 pets in 5 beds?

```python
base_5 = ['bat', 'cat', 'frog', 'eel', 'hamster']

animals_counting = []

for an1 in base_5:
    for an2 in base_5:
        for an3 in base_5:
            for an4 in base_5:
                for an5 in base_5:
                    animals_counting.append([an1, an2, an3, an4, an5])

# for an_number in animals_counting:
#     print(an_number)

animal_perms = []

for an_number in animals_counting:
    perm = True

    for an in an_number:
        if an_number.count(an) > 1:
            perm = False
            break
    if perm == True:
        animal_perms.append(an_number)

# for an_number in animal_perms:
#     print(an_number)
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# [Heap's Algorithm](https://en.wikipedia.org/wiki/Heap%27s_algorithm): A better way to get Permutations
* Relies on swapping

Non-Recursive Algorithm from [Wikipedia](https://en.wikipedia.org/wiki/Heap%27s_algorithm):

```
procedure generate(n : integer, A : array of any):
    //c is an encoding of the stack state. 
    //c[k] encodes the for-loop counter for when generate(k - 1, A) is called
    c : array of int

    for i := 0; i < n; i += 1 do
        c[i] := 0
    end for

    output(A)
    
    //i acts similarly to the stack pointer
    i := 0;
    while i < n do
        if  c[i] < i then
            if i is even then
                swap(A[0], A[i])
            else
                swap(A[c[i]], A[i])
            end if
            output(A)
            //Swap has occurred ending the for-loop. Simulate the increment of the for-loop counter
            c[i] += 1
            //Simulate recursive call reaching the base case by bringing the pointer to the base case analog in the array
            i := 0
        else
            //Calling generate(i+1, A) has ended as the for-loop terminated. Reset the state and simulate popping the stack by incrementing the pointer.
            c[i] := 0
            i += 1
        end if
    end while
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# [Heap's Algorithm](https://en.wikipedia.org/wiki/Heap%27s_algorithm) in Python
We'll write this version close to the algorithm on wikipedia



```python
def swap(lst, idx_1, idx_2):
    lst_ = lst.copy()
    temp = lst_[idx_2]
    lst_[idx_2] = lst_[idx_1]
    lst_[idx_1] = temp
    return lst_


def heaps_non_recursive(lst, k):
    # avoid modifying parameter
    lst_copy = lst.copy()

    # holds stack state
    c = [0] * len(lst)

    # collect permutations, collect initial perm
    perms = [lst_copy[:k]]

    i = 0 # acts like a stack pointer
    while i < len(lst_copy):
        if c[i] < i:
            if i % 2 == 0:
                lst_copy = swap(lst_copy, 0, i)
            else:
                lst_copy = swap(lst_copy, c[i], i)
            
            if lst_copy[:k] not in perms:
                perms.append(lst_copy[:k])

            # incr the counter
            c[i] += 1

            # reset i
            i = 0
        else:
            # reset state of count state at i
            c[i] = 0
            i += 1

    return perms
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Combinations: $nCk = \frac{n!}{((n-k)! k!)}$
**ORDER DOESN'T MATTER**
Combinations can be thought of as a reduction of the Permutations space, as order doesn't matter.

**Cardinal Example of a Combinations Prob**: 
How many different 5 card hands in a game of poker?
It doesn't matter how you arrange the cards in your hand


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (3 minutes)
Code the `combinations Function`

$$
nCk = \frac{n!}{((n-k)! k!)}
$$

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT Solution
Code the `combinations Function`

$$
nCk = \frac{n!}{((n-k)! k!)}
$$

```python
def combinations(n, k):
    return int(factorial(n) / (factorial(n-k) * factorial(k)))

# Slightly more optimal:
def combinations(n, k):
    perm = 1
    for i in range(n, n-k, -1):
        perm *= i
    return int(perm / factorial(k))
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Combinations Intuition
1. Make a counter list, treating the elements as the base in a number system
2. Create a sublist of the counter list that is the Permutations
3. Sort the elements of the sublist
4. Remove any duplicate sublists

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Combinations Intuition
#### An expensive Counting Approach

Ex:

Out of a set of 11 basketball players, only
5 can be on the court at a time. What are all
the combinations possible for that basketball team.

```python
num_combs = combinations(11, 5)

def basketball_combs():
    eleven_nums = range(1, 11+1)

    # every arrangement of 5
    possible_five = []

    for i in eleven_nums:
        for j in eleven_nums:
            for k in eleven_nums:
                for l in eleven_nums:
                    for m in eleven_nums:
                        possible_five.append([i,j,k,l,m])

    # for five in possible_five:
    #     print(five)

    perms = []

    for five in possible_five:
        if len(list(set(five))) == 5:
            perms.append(five)

    # for five in perms:
    #     print(five)

    combs = []

    for five in perms:
        sorted_five = sorted(five)

        if sorted_five not in combs:
            combs.append(sorted_five)
    
    return combs

# for five in basketball_combs():
#     print(five)
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Combinations Intuition
#### An expensive Sampling Approach
We can sample 5 players from our list of 11,
can continue to build combinations until we reach
11C5 combinations

```python
from random import choice

def basketball_combs_samp(team_size=11, num_players=5):
    combs = []

    player_range = range(1, team_size+1)

    while len(combs) < combinations(team_size, num_players):
        player_comb = []

        while len(player_comb) < num_players:
            player_num = choice(player_range)

            if player_num not in player_comb:
                player_comb.append(player_num)

        player_comb = sorted(player_comb)

        if player_comb not in combs:
            print(player_comb)
            combs.append(player_comb)
    return combs


team_size = 11
num_players = 5

print(len(basketball_combs_samp(team_size, num_players)))
print(combinations(team_size, num_players))
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Combinations Algorithm (Better) 
#### Based on `Itertools` implementation
* Notice the `yield` keyword, which allows for the creation of a [generator](https://wiki.python.org/moin/Generators) object. 

```python
def combs_alg_from_itertools(lst, k):
    # get a frozen version of the input, 
    lst_frozen = tuple(lst)
    n = len(lst_frozen)
    
    combs = []

    # fault control
    if k > n:
        return


    indices = list(range(k))
    yield tuple(lst_frozen[i] for i in indices)
    while True:
        for i in reversed(range(k)):
            if indices[i] != i + n - k:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, k):
            indices[j] = indices[j-1] + 1
        yield tuple(lst_frozen[i] for i in indices)
```