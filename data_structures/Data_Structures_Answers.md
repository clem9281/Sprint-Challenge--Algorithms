For each of the methods associated with each data structure, classify it based on its runtime, using Big O notation.

## Linked List

1. `addToTail` - O(1) since the linked list has a pointer directly to the tail of the list.
  
    a. What if our list implementation didn't have a reference to the tail of the list in its constructor? What would be the runtime of the `addToTail` method?

    Without the tail pointer, `addToTail` would be an O(n) method since we'd have to start at the head pointer and traverse along the entire length of the list.

2. `removeHead` - O(1) since the linked list has a pointer directly to the head of the list.

3. `contains` - O(n) regardless of whether an iterative or recursive solution was used.

4. `getMax` - O(n) since in the worst case we need to iterate through the entire length of the list to check every value to ensure we have the max value of the entire list.

## Queue

1. `enqueue` - O(1) since the underlying `addToTail` method runs in constant time.

2. `dequeue` - O(1) since the underlying `removeHead` method runs in constant time.

3. `isEmpty` - O(1)

4. `length` - O(1)

## Doubly Linked List

1. `ListNode.insertAfter` - O(1) since we're just adding a new node as this node's `next` node, which we can access in constant time.

2. `ListNode.insertBefore` - O(1) since we're just adding a new node as this node's `prev` node, which we can access in constant time. 

3. `ListNode.delete` - O(1) since we're simply rearranging `prev` and `next` pointers. This operation only ever touches the calling node's previous and next nodes. 

4. `DoublyLinkedList.addToHead` - O(1) since we have a pointer to the head of the list.

5. `DoublyLinkedList.removeFromHead` - O(1) since we have a pointer to the head of the list.

6. `DoublyLinkedList.addToTail` - O(1) since we have a pointer to the tail of the list.

7. `DoublyLinkedList.removeFromTail` - O(1) since we have a pointer to the tail of the list.

8. `DoublyLinkedList.moveToFront` - O(1) since this method receives the node that we wish to move to the front of the list. We don't need to go searching through the list to find the node.

9. `DoublyLinkedList.moveToBack` - O(1) since this method receives the node that we wish to move to the end of the list. We don't need to go searching through the list to find the node.

10. `DoublyLinkedList.delete` - O(1) since we simply call the node's `delete` method, which runs in constant time. 

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the `Array.splice` method. Which method generally performs better?

    The `Array.splice` method has a worst-case runtime of O(n). This is because when splicing an element out of an array, the elements that come after the element that was deleted in the array need to all be shifted up to fill the empty spot the deleted element left behind. Thus, in the worst case, we could have to shift _every_ element forward one spot if the very first array element was spliced out of the array.

## Binary Search Tree

1. `insert` - O(log n) since we're traversing the binary search tree in 'levels' instead of inspecting each element in turn. At each level we determine whether we continue traversing down the left subtree or the right subtree, meaning we don't need to check the other side of the tree at every level. 

2. `contains` - O(log n) since we're traversing the binary search tree in 'levels' instead of inspecting each element in turn. At each level we determine whether we continue traversing down the left subtree or the right subtree, meaning we don't need to check the other side of the tree at every level. 

3. `getMax` - O(log n) even though we simply walk the right subtree as far as it goes. This operation still depends upon the number of elements in the tree, since that contributes to how far right we need to keep going in the tree.

4. `depthFirstForEach` - O(n) since we're traversing _all_ of the elements in the tree. The fact that we're doing this in a depth-first fashion doesn't change that fact.

5. `breadthFirstForEach` - O(n) wince we're traversing _all_ of the elements in the tree. The fact that we're doing this in a breadth-first fashion doesn't change that fact.

## Heap

1. `bubbleUp` - O(log n) since a heap has a binary tree structure. In the worst case, we only need to bubble up a heap element up along a single 'path' in the heap. All the other elements in the heap don't need to be touched. In other words, when bubbling up an element to the top of the heap, each recursive call of the `bubbleUp` function moves an element up a level in the heap.

2. `siftDown` - O(log n) following the same logic of the `bubbleUp` method, excect in this case, elements are swapped down the tree, with each recursive call to `siftDown` moving the element down a level in the heap.

3. `insert` - O(log n) since `push`ing to the `storage` array is a constant time operation, so the biggest contributor is the call to the `bubbleUp` method, which incurs O(log n) complexity. 

4. `delete` - O(log n) since the dominating operation is the call to the `siftDown` method. 

5. `getMax` - O(1) since the heap maintains the invariant that the maximum value is located at `this.storage[1]`. 