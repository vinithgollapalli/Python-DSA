set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
union_method = set_a.union(set_b)
union_operator = set_a | set_b
print(f"Union: {union_method}")
intersection_method = set_a.intersection(set_b)
intersection_operator = set_a & set_b
print(f"Intersection: {intersection_method}")
difference_method = set_a.difference(set_b)
difference_operator = set_a - set_b
print(f"Difference (A - B): {difference_method}")
sym_diff_method = set_a.symmetric_difference(set_b)
sym_diff_operator = set_a ^ set_b
print(f"Symmetric Difference: {sym_diff_method}")
set_copy = set_a.copy()
set_copy.update(set_b)
set_copy = set_a.copy()
set_copy.intersection_update(set_b)
set_copy = set_a.copy()
set_copy.difference_update(set_b)  
set_copy = set_a.copy()
set_copy.symmetric_difference_update(set_b) 
subset_x = {1, 2}
subset_y = {1, 2, 3}
is_subset_method = subset_x.issubset(subset_y)
is_subset_operator = subset_x <= subset_y 
is_proper_subset = subset_x < subset_y 
is_superset_method = subset_y.issuperset(subset_x)
is_superset_operator = subset_y >= subset_x  
is_proper_superset = subset_y > subset_x
is_disjoint = set_a.isdisjoint({10, 11, 12})
has_element = 3 in set_a 
set_a.add(9)
set_a.remove(9)
set_a.discard(99)
popped_element = set_a.pop()
set_copy.clear()
