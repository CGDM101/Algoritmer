// DIVIDE AND CONQUER
function Search(aList, key) {
  // let mid = Math.floor(aList.length / 2)
  let mid = parseInt(aList.length / 2)
  console.log("Searching mid point at " + aList[mid])

  if (mid == 0) {
    console.log("Key not found!")
    return key
  } else if (key == aList[mid]) {
    // recursion ends
    console.log("Key found!")
    return aList[mid]
  } else if (key > aList[mid]) {
    console.log("aList now contains..." + aList.slice(mid, aList.length))
    Search(aList.slice(mid, aList.length), key)
  } else {
    console.log("aList now contains ..." + aList.slice(0, mid))
    Search(aList.slice(0, mid), key)
  }
}

let aList = [
  1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
]
Search(aList, 5); // Söker efter 5 i aList
