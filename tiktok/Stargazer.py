def star_gazer(coords,points):
	x1,y1 = coords[0],coords[1]
	x2,y2 = coords[2],coords[3]
	out_of_bounds = []
	curr_stars = create_area(x1,y1,x2,y2)

	all_dist_res = []
	for point in points:
		px1,py1 = point[:2]
		if((px1,py1) in curr_stars):
			continue
		else:
			close_dist = max((abs(px1-x1),abs(py1-y1)))
			far_dist = max((abs(px1-x2),abs(py1-y2)))
			min_dist = min(close_dist,far_dist)
			all_dist_res.append(min_dist)
			out_of_bounds.append(point)
	if(out_of_bounds == []):
		return 0
	return max(all_dist_res)


def create_area(x1,y1,x2,y2):
	all_coords = set()
	for i in range(x2+1):
		for j in range(y2+1):
			all_coords.add((x1+i,y1+j))

	return all_coords


coordinates = [0,0,4,4]
stars = [[-4,4,1,0],[8,0,-1,0]]
print(star_gazer(coordinates,stars))