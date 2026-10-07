from insta_utils import format_follower_count

counts = [1500, 2300000, 850]

for c in counts:
    print(c, "->", format_follower_count(c))