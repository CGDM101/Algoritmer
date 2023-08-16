// Räkna ut faktorn med rekursion
// (Faktorn: Multiplikation av en sekvens där varje nummer är ett mindre än föregående nummer i sekvensen)

function Factorial(n) {
  console.log("factorial is called with  n = " + n)
  if (n == 1 || n == 0) {
    console.log("Ending condition is met")
    return 1
  } else {
    return n * Factorial(n - 1) // Reducerar startargumentet med ett.
  }
}
console.log(Factorial(5)); // 5! = 120

function FactorialAlternative(n) {
  console.log("Factorial is called with  n = " + n)
  if (n > 1) {
    // checks the continuations condiiton (above it is the ending cond that is checked)
    return n * FactorialAlternative(n - 1)
  } else {
    console.log("Ending condition is met.")
    return 1
  }
}
console.log("second: " + FactorialAlternative(5))
// Instead of checking the ending condition, this version checks the continuation condiiton. As long as n is > 1, the programme will continue to  make rekursive calls. The code is horter, but less clear because you must think  about what condiiton will e nd the recukriosn.

// Eliminating tail recursion
// return n * factorial(n - 1) is the tail call.
// One approach is to create an iterative alternative.
function FactorialIterative(n) {
  console.log("Factorial is called with  n = " + n)
  result = 1
  while (n > 1) {
    result = result * n
    n = n - 1
    console.log("current value of n: " + n)
  }
  console.log("Ending condition met")
  return result
}
console.log("iterative factorial: " + FactorialIterative(5))
// A while loop replaces the recursive call, but you sittl need to check for the same condiiton and continue looping until the data meets the condiiton.


// ANNAT EXEMPEL PÅ REKURSION:
console.log(SumRecursively(10))

function SumRecursively(k) {
  if (k > 0) {
    return k + SumRecursively(k - 1)
  } else {
    return 0;
  }
} // När k == 0 slutar funktionen anropa sig själv.

// ITERATIV VERSION:
let sum = 0
SumIteratively(10)
function SumIteratively(k) {
  while(k > 0) {
    sum = sum + k
    k = k - 1
  }
}
console.log(sum)
