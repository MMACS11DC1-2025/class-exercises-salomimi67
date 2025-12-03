file = open("6.2/spotify.csv")
junk = file.readline()

drake_data = []

for line in file:
	items = line.strip().split(",")
	artist = str(items[-1])
	songtitle = str(items[-2])
	danceability = float(items[1])
	
	if artist == "Drake":
		drake_data.append([danceability, songtitle, artist])

for i in range(len(drake_data)):
	small_score = drake_data[i]
	small_index = i

	for j range(i+1, len(drake_data)):
		if drake_data[j] < small_score:
		small_score = drake_data[y]
		small_index = y
	
	drake_data[small_index], drake_data[i] = drake_data[i], drake_data{small_index}

top_five = drake_data[:5]
for item in top_five:
	print(str(item[0]) + "\t\t" + item[1] + " by " + item[2])