# Sets

# what does this do?
set("able was i ere I saw elba")

# we can create a set like so:
my_set = set([1,2,3,4,'dog'])

# but what about this?
my_set = set([1, 2, 3, 4, 'dog', {'thebest':'hotdogs'}])

# or this?
my_set = set([1, 2, 3, 4, 'dog', [7, 8, 9])
             
# or this?
my_set = set([1, 2, 3, 4, 'dog', (7, 8, 9))
             
# sets are super useful for making things unique, e.g.:
list1 = [
'locus-1', 
'locus-2', 
'locus-3',
'locus-3',
'locus-4',
'locus-5',
'locus-5',
'locus-6',
'locus-6',
'locus-6'
]

# sets have lots of methods that align with set theory:
set1 = set([
'locus-1', 
'locus-2', 
'locus-3',
'locus-4',
'locus-5',
'locus-6'
])

set2 = set([
'locus-4',
'locus-5',
'locus-6'
])

set3 = set([
'locus-10',
'locus-11',
'locus-12'
])

# we can test for membership:
'locus-1' in set1

# do sets share common elements:
set1.isdisjoint(set2)
set1.isdisjoint(set3)

# is set on the left a subset of set on the right:
set1.issubset(set2)
set2.issubset(set1)

# is set on the left a superset of set on the right:
set1.issuperset(set2)
set2.issuperset(set1)

# create a new set with all unique elements of others:
set2.union(set3)

# create a new set with only overlapping elements of others:
set1.intersection(set2)

# create a new set with non-overlapping elements of others:
set1.difference(set2)

# sets are mutable, frozensets are not:
set1 = frozenset([1,2,3])
set1.add(4)