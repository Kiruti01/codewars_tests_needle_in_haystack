def find_needle(haystack):
    i = haystack.index("needle")
    return "found the needle at position " + str(i + 1)

print(find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]))
