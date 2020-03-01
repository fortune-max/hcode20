from collections import defaultdict as d

def best_lib_choice(lib_idxs, days):
    lib_dic = {}
    for lib_idx in lib_idxs:
        avail_books = set(book_lookup[lib_idx]) - processed_books
        (book_total, signup_cost, daily_cpcty) = lib_props[lib_idx]
        lib_days = days - signup_cost
        lib_score = sum(sorted([book_scores[x] for x in avail_books], reverse=True)[:max(0, daily_cpcty * lib_days)])
        lib_dic[lib_idx] = lib_score / (1. * signup_cost)
    return max(lib_dic, key = lambda x : lib_dic[x])

def best_book_choice(lib_idx):
    for book in book_lookup[lib_idx][::-1]:
        book_lookup[lib_idx].pop()
        if book not in processed_books:
            processed_books.add(book)
            return book

B, L, D = map(int, raw_input().split())
book_scores = map(int, raw_input().split())
book_lookup, lib_props = d(set), [0] * L

for lib_idx in xrange(L):
    book_total, signup_cost, daily_cpcty = map(int, raw_input().split())
    lib_props[lib_idx] = (book_total, signup_cost, daily_cpcty)
    lib_books = map(int, raw_input().split())
    book_lookup[lib_idx] = sorted(lib_books, key = lambda x : book_scores[x])

lib_order, processed_books, unprocessed_libs = [], set(), set(book_lookup)
lib_order, lib_ans = [], d(list)

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

# Del libs sending nothing
for lib_idx in lib_order:
    if not lib_ans[lib_idx]:
        del lib_ans[lib_idx]

print len(lib_ans)
for lib_idx in lib_order:
    if lib_idx in lib_ans:
        print lib_idx, len(lib_ans[lib_idx])
        print " ".join(map(str, lib_ans[lib_idx]))
