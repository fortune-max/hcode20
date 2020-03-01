from collections import defaultdict as d

B, L, D = map(int, raw_input().split())
book_scores = map(int, raw_input().split())
book_lookup, lib_props = d(set), [0] * L

for lib_idx in xrange(L):
    book_total, signup_cost, daily_cpcty = map(int, raw_input().split())
    lib_props[lib_idx] = (book_total, signup_cost, daily_cpcty)
    lib_books = map(int, raw_input().split())
    book_lookup[lib_idx] = sorted(lib_books, key = lambda x : book_scores[x])

# Process answer
lib_count = input()
book_count_total = 0
ans_books_processed = set()
ans_lib_processed = set()
ans_score = 0
for idx in xrange(lib_count):
    (lib_idx, book_count) = map(int, raw_input().split())
    book_count_total += book_count
    books = map(int, raw_input().split())
    ans_books_processed |= set(books)
    ans_lib_processed |= set([lib_idx])

score_arr = sorted([book_scores[x] for x in ans_books_processed])
ans_score = sum(score_arr)
print "Your submission scored %d points" % ans_score
print "The library signup has been completed for {} out of {} libraries ({}%)".format(lib_count, L, lib_count*100./L)
print "A total of {} books have been scanned. {} of which where distinct with an avg score of {}. This is {}% of the {} books available across all libraries. The minimum score of a scanned book was {} and the maximum was {}." .format (book_count_total, len(ans_books_processed), ans_score*1./len(ans_books_processed), len(ans_books_processed)*100./B, B, score_arr[0], score_arr[-1])
