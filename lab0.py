# This is the file you'll use to submit most of Lab 0.

# Certain problems may ask you to modify other files to accomplish a certain
# task. There are also various other files that make the problem set work, and
# generally you will _not_ be expected to modify or even understand this code.
# Don't get bogged down with unnecessary work.


# Section 1: Problem set logistics ___________________________________________

# This is a multiple choice question. You answer by replacing
# the symbol 'fill-me-in' with a number, corresponding to your answer.

# You get to check multiple choice answers using the tester before you
# submit them! So there's no reason to worry about getting them wrong.
# Often, multiple-choice questions will be intended to make sure you have the
# right ideas going into the problem set. Run the tester right after you
# answer them, so that you can make sure you have the right answers.

# What version of Python do we *recommend* (not "require") for this course?
#   1. Python v2.3
#   2. Python v2.5 or Python v2.6
#   3. Python v3.0
# Fill in your answer in the next line of code ("1", "2", or "3"):

ANSWER_1 = "2"


# Section 2: Programming warmup _____________________________________________

# Problem 2.1: Warm-Up Stretch

def cube(x):
    if isinstance(x,int) or isinstance(x,float):
       return x*x*x;
    raise NotImplementedError

def factorial(x):
    if(x>=0) and isinstance(x,int):
        fac=1;
        if x==0 or x==1:
             fac=1;
        else:
           for  i in range(1,x+1):
                fac=fac*i;
        return fac        
   
    raise NotImplementedError

def count_pattern(pattern, lst):
    if isinstance(lst,list):
       lst = ''.join(str(x) for x in lst)
       pattern = ''.join(str(x) for x in pattern)
       c = start = 0
       while True:
           start = lst.find(pattern, start) +1
           if start > 0:
              c+=1
           else:
              return c
    raise NotImplementedError


# Problem 2.2: Expression depth

def depth(expr):
    if isinstance(expr, list):
        return max(map(depth, expr))+1
    # this says: return the maximum depth of any sub-expression + 1
    return 0


# Problem 2.3: Tree indexing

def tree_ref(tree, index):
    for i in range(len(index)):
              t=tree[index[i]]
              tree=t;       
    return t
#raise NotImplementedError


# Section 3: Symbolic algebra

# Your solution to this problem doesn't go in this file.
# Instead, you need to modify 'algebra.py' to complete the distributer.

from algebra import Sum, Product, simplify_if_possible
from algebra_utils import distribution, encode_sumprod, decode_sumprod



