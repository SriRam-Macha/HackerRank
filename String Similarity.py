def stringSimilarity(s): 
	n = len(s) 
	z = [0]*n
	l, r, k = 0, 0, 0
	for i in range(1, n): 
		if i > r: 
			l, r = i, i 
			while r < n and s[r - l] == s[r]: 
				r += 1
			z[i] = r - l 
			r -= 1
		else: 
			k = i - l 
			if z[k] < r - i + 1: 
				z[i] = z[k] 
			else: 
				l = i 
				while r < n and s[r - l] == s[r]: 
					r += 1
				z[i] = r - l 
				r -= 1
	return (n + sum(z)) 

print(stringSimilarity('aa'))

