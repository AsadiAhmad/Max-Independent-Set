# Max-Independent-Set
Calculating Max Independent Set with greedy algorithm

## Tech :hammer_and_wrench: Languages and Tools :
<div>
  <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" title="Python" alt="Python" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/networkx/networkx-original.svg"  title="Networkx" alt="Networkx" width="40" height="40"/>&nbsp;
</div>

For Tree : anytree Lib

For Graph : networkX Lib

## Max Independent Set for Tree

### Time complexity : O(n*h(n))

Always return correct answer (Always return Max Independent Set)

<img src="/Pictures/1.png"/>

### Prove : 

**Step 1 : Initialization** The initial set ```unCutNodesSet``` is constructed by adding the root and all descendants. Using ```Root.descendants``` from the ```anytree``` library, this operation takes O(n), where n is the number of nodes in the tree.

**Step 2 : Independent Set Iteration** 
- Checking if a node has no children (leaf check) is O(1).
- Appending to ```IndependentSet``` and removing from ```unCutNodesSet``` are both O(1).
- For each non-leaf node, the function calls itself recursively on each child. and we can say if we have k nodes under the selected subtree then complexity should be O(k)
- what does this section do ? it found all of leaf nodes of a subtree then add those to the independent set list then remove all leafs and preant leafs from the tree.

**Step 3 : Main Loop** The main loop iterates as long as unCutNodesSet is not empty. Within each iteration:
- Choosing a node in ```unCutNodesSet```: The line ```next(iter(unCutNodesSet))``` takes O(1) time.
- Calling ```IndependentSetIteration```: The core of the complexity lies in this recursive function.

**Total Complexity :** The while loop calls Independent Set Iteration function O(h(n)) times since Complexity of the Independent Set Iteration function is O(n) then the total complexity should be O(n) + O(n* h(n)) = O(n*h(n))

**Best Case :** Now if we have a full tree it shows the Best case and the complexity should be Ω(n*Log(n)).

**Worst Case :** if we had a line tree then is shows the worst case and the complexity should be O(n^2).

## Optimized Max Independent Set for Tree

### Time complexity : O(n)

## Max Independent Set for Graph

### Time complexity : O(V^2+VE)

Sometimes return correct answer (because its greedy algorithm)

### Correct answer :

<img src="/Pictures/3.png"/>

<img src="/Pictures/2.png"/>

<img src="/Pictures/4.png"/>

### Wrong answer :

<img src="/Pictures/5.png"/>

the answer should be : F and E for the A, B, C, E, F, G set and a D node for whole graph then the answer should be : E, F, D but in greedy way we first choose G then can't choose E and F then we just should choose a Node from the complete-4 graph A, B, C, D and the greedy answer being G and A which is incorrect.

## Conclusion :

Greedy algorithm works correct for trees not graphs

Also greedy algorithm for tree has better complexity
