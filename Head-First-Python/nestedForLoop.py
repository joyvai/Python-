movies = ["The Holy Grail",1975, "Terry Jones & Terry Gilliam", 91,
		["Graham Chapman",["Michael Palin", "John Clesese","Terry Gilliam",
		"Eric Idle","Terry Jones"]]]
# print movies
# print movies[4][1][3]
for each_item in movies:
	if isinstance(each_item, list):
		for nested_item in each_item:
			if isinstance(nested_item,list):
				for item in nested_item:
					print item
	else:
		print each_item


























