function unflatten(flatArray) {
    let result = [];
    let index = 0;
    while (index < flatArray.length) {
        let value = flatArray[index];
        if (value < 3) {
            result.push(value);
            index += 1;
        } else {
            let subArray = flatArray.slice(index, index + value);
            result.push(subArray);
            index += value;
        }
    }
    return result;
}