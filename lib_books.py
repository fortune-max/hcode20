from collections import defaultdict as d
from sys import stderr
from copy import deepcopy

def best_lib_choice(lib_idxs, days):
    lib_dic = {}
    for lib_idx in lib_idxs:
        avail_books = set(book_lookup[lib_idx]) - processed_books
        (book_total, signup_cost, daily_cpcty) = lib_props[lib_idx]
        lib_days = days - signup_cost
        lib_score = sum(sorted([book_scores[x] for x in avail_books], reverse=True)[:max(0, daily_cpcty * lib_days)])
        lib_dic[lib_idx] = lib_score / (1. * signup_cost)
    return max(lib_dic, key = lambda x : lib_dic[x])

def best_lib_choice_array():
    global lib_order_copy
    ret_val = lib_order_copy[0]
    lib_order_copy = lib_order_copy[1:]
    return ret_val

def best_book_choice(lib_idx):
    for book in book_lookup[lib_idx][::-1]:
        book_lookup[lib_idx].pop()
        if book not in processed_books:
            lib_locations = lib_lookup[book] & set(lib_order) - set([lib_idx])
            for lib_location in lib_locations:
                book_idx = len(book_lookup[lib_location])-book_lookup[lib_location].index(book)
                start_idx = lib_order.index(lib_idx)
                stop_idx = lib_order.index(lib_location)
                sum_to = sum([lib_props[x][1] for x in lib_order[start_idx:stop_idx+1]])
                if (sum_to + book_idx) < D:
                    print >> stderr, ("Found an instance!!!", book, book_idx, D)
                    print >> stderr, ("Not using lib_idx", lib_idx, "for book", book)
                    lib_lookup[book].remove(lib_idx)
                    new_choice = best_book_choice(lib_idx)
                    print >> stderr, ("return instead book", new_choice)
                    return new_choice
            processed_books.add(book)
            return book

B, L, D = map(int, raw_input().split())
book_scores = map(int, raw_input().split())
book_lookup, lib_props, lib_lookup = dict(), [0] * L, d(set)

for lib_idx in xrange(L):
    book_total, signup_cost, daily_cpcty = map(int, raw_input().split())
    lib_props[lib_idx] = (book_total, signup_cost, daily_cpcty)
    lib_books = map(int, raw_input().split())
    for book in lib_books:
        lib_lookup[book].add(lib_idx)
    book_lookup[lib_idx] = sorted(lib_books, key = lambda x : book_scores[x])

processed_books, unprocessed_libs = set(), set(book_lookup)
lib_order, lib_ans = [], d(list)

#copies for second run
D_copy, book_lookup_copy, lib_lookup_copy = D, deepcopy(book_lookup), deepcopy(lib_lookup)
lib_order_new, lib_ans_new = [], d(list)

print >> stderr, "Begin first run"
while D > 0 and B > len(processed_books):
    if unprocessed_libs:
        lib_choice = best_lib_choice(unprocessed_libs, D)
        signup_cost = lib_props[lib_choice][1]
        # Process all up till signup done
        for t in xrange(signup_cost):
            for lib_idx in lib_order:
                book_choice = best_book_choice(lib_idx)
                if book_choice != None:
                    lib_ans[lib_idx].append(book_choice)
            D -= 1
        lib_order.append(lib_choice)
        unprocessed_libs.remove(lib_choice)
    else:
        # Handle no more libraries to pick from
        for lib_idx in lib_order:
            book_choice = best_book_choice(lib_idx)
            if book_choice != None:
                lib_ans[lib_idx].append(book_choice)
        D -= 1
        
# Second run
print >> stderr, "Begin second run"
processed_books, unprocessed_libs, D = set(), set(book_lookup_copy), D_copy
lib_order_new, lib_ans_new, lib_order_copy = [], d(list), lib_order[:]
book_lookup, lib_lookup = deepcopy(book_lookup_copy), lib_lookup_copy

while D > 0 and B > len(processed_books):
    if unprocessed_libs:
        lib_choice = best_lib_choice_array()
        signup_cost = lib_props[lib_choice][1]
        # Process all up till signup done
        for t in xrange(signup_cost):
            for lib_idx in lib_order_new:
                book_choice = best_book_choice(lib_idx)
                if book_choice != None:
                    lib_ans_new[lib_idx].append(book_choice)
            D -= 1
        lib_order_new.append(lib_choice)
        unprocessed_libs.remove(lib_choice)
    else:
        # Handle no more libraries to pick from
        for lib_idx in lib_order_new:
            book_choice = best_book_choice(lib_idx)
            if book_choice != None:
                lib_ans_new[lib_idx].append(book_choice)
        D -= 1

# reset variables
lib_ans, lib_order = lib_ans_new, lib_order_new

# Del libs sending nothing
for lib_idx in lib_order:
    if not lib_ans[lib_idx]:
        del lib_ans[lib_idx]

print len(lib_ans)
for lib_idx in lib_order:
    if lib_idx in lib_ans:
        print lib_idx, len(lib_ans[lib_idx])
        print " ".join(map(str, lib_ans[lib_idx]))
