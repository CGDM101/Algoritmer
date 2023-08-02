// STACK

//myStack = [101, 10, 234]
myStack = []
StackSize = 3

function DisplayStack() {
  console.log("Stack currently contains:")
  for (let i = 0; i < StackSize; i++) {
    console.log(myStack[i])
  }
}

function Push(value) {
  if (myStack.length < StackSize) {
    myStack.push(value)
  } else {
    console.log("Stack is full")
  }
}

function Pop() {
  if (myStack.length > 0) {
    console.log("Popping: " + myStack.pop())
  } else {
    console.log("Stack is empty")
  }
}

Push(1)
Push(2)
Push(3)
DisplayStack()

Push(4)

Pop()
DisplayStack()

Pop()
Pop()
Pop()

// The stack maintains the integrity of the data. It works with it in the order you expect.

// QUEUE
myQueue = []
stackSize = 3

function DisplayQueue() {
  console.log("Queue currently contains:")
  for (let i = 0; i < StackSize; i++) {
    console.log(myQueue[i])
  }
}

function PushToQueue(value) {
  if (myQueue.length < StackSize) {
    myQueue.push(value)
  } else {
    console.log("Queue is full")
  }
}

function RemoveFromQueue() {
  if (myQueue.length > 0) {
    console.log("Shifting: " + myQueue.shift()) // shift tar bort första, t sk fr pop som tar bort sista (men 2 hoppar till 1:s plats??)
  } else {
    console.log("Queue is empty")
  }
}

PushToQueue(1)
PushToQueue(2)
PushToQueue(3)
DisplayQueue()

PushToQueue(4) // q is full

RemoveFromQueue()
DisplayQueue()

RemoveFromQueue()
RemoveFromQueue()
RemoveFromQueue()
