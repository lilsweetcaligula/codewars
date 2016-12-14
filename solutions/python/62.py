def vowel_indices(word):
	return [index + 1 for index, char in enumerate(word) if char.lower() in 'aeouiy']