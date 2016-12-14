const xMarksTheSpot = function (input, target) {
	target = target || 'x';
	var targetRow = -1, targetCol = -1;
	for (var row = 0; row < input.length; ++row) {
		var col = input[row].indexOf(target);
		if (col >= 0) {
			if (targetCol < 0) {
				targetRow = row;
				targetCol = col;
			} else {
				return [];
			}
		}
	}
	return(
    input.length > 0 
      && targetRow >= 0 
      && targetCol >= 0 ? [targetRow, targetCol] : []);
}