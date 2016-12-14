var titleCase = (title, ignore, separator = " ") => {
    let words = title.split(separator);
    ignore = ignore && ignore.toLowerCase().split(" ") || [];
    for (let index = 0; index < words.length; ++index) {
        words[index] = words[index].toLowerCase();
        if (!(index > 0 && ignore && ignore.indexOf(words[index].toLowerCase()) >= 0)) {
            words[index] = words[index].substr(0, 1).toUpperCase() 
                + words[index].substr(1).toLowerCase();
        }
    }
    return words.join(separator);
}