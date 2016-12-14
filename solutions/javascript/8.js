function validName(array) {
  if (!array || array.length == 0) {
    return 'You must test at least one name.';
  }
  if (array.length == 1) {
    return 'Congratulations, you can choose any name you like!';
  }
  return ((array) => {
    for (let index = 0; index < array.length - 1; ++index) {
      let currentName = array[index].toLowerCase();
      let nextName = array[index + 1].toLowerCase();
      if (currentName.charAt(currentName.length - 1) != nextName.charAt(0)) {
        return false;
      }
    }
    return true;
  })(array) ? 'Congratulations, your baby names are compatible!' :
              'Back to the drawing board, your baby names are not compatible.';
}