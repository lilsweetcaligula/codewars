"use strict";

function flattenAndSort(array) {
    return array && array
      .reduce((a, b) => a.concat(b), [])
      .sort((a, b) => a - b) || [];
}"use strict"

const numerically = (v,w) => v-w;
const flattenAndSort = a => [].concat(...a).sort(numerically);