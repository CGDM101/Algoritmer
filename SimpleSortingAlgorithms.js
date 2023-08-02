// https://www.digitalocean.com/community/tutorials/js-bubble-selection-insertion-sort

// BUBBLE SORT
// For each element, check if the next element is larger; if then, swap their indexes.
// To avoid recomparing already sorted elements, start from the back while another loop gets the preceding element.
// All of the largest elements build up/bubbles up to the end.

const unsortedArr = [
  31, 27, 28, 42, 13, 8, 11, 30, 17, 41, 15, 43, 1, 36, 9, 16, 20, 35, 48, 37,
  7, 26, 34, 21, 22, 6, 29, 32, 49, 10, 12, 19, 24, 38, 5, 14, 44, 40, 3, 50,
  46, 25, 18, 33, 47, 4, 45, 39, 23, 2,
]

const bubble = (arr) => {
  const swap = (list, a, b) => ([list[a], list[b]] = [list[b], list[a]]);

  for (i = arr.length; i > 0; i--) {
    // yttre loopen från slutet
    for (j = 0; j < i - 1; j++) {
      // inre från början
      if (arr[j] > arr[j + 1]) {
        // if next item larger...
        swap(arr, j, j + 1); // ...swap their indexes
      }
    }
  }

  return arr;
};

console.log(bubble(unsortedArr)); // stigande 1-50

// SELECTION SORT
// Instead of pushing large values to end, push low values to start.
const selection = (arr) => {
  const swap = (list, a, b) => ([list[a], list[b]] = [list[b], list[a]]);

  arr.forEach((item, i) => {
    let min = i;
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[j] < arr[min]) min = j // Om finner mindre värde, detta blir det nya lägsta värdet
    }
    swap(arr, i, min)
  })

  return arr
}

console.log(selection(unsortedArr));

// INSERTION SORT
const insertion = (arr) => {
  arr.forEach((item, i) => {
    let num = arr[i]
    let j

    for (j = i - 1; j >= 0 && arr[j] > num; j--) {
      arr[j + 1] = arr[j]
    }
    arr[j + 1] = num
  })

  return arr
}

console.log(insertion(unsortedArr))

// Alla tre är O(n^2).
