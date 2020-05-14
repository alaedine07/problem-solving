function destroyer(arr){
	var args = Array.from(arguments);
	args.splice(0,1);
	var targets = args;
	return arr.filter(function(num){
		return targets.indexOf(num) === -1;
	});
}