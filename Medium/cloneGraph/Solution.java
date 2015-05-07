/**
 * Definition for undirected graph.
 * class UndirectedGraphNode {
 *     int label;
 *     List<UndirectedGraphNode> neighbors;
 *     UndirectedGraphNode(int x) { label = x; neighbors = new ArrayList<UndirectedGraphNode>(); }
 * };
 */
public class Solution {
	public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
		if(node == null) return null;

		Queue<UndirectedGraphNode> q = new LinkedList<UndirectedGraphNode>();
		Map<Integer, UndirectedGraphNode> map = new HashMap<Integer, UndirectedGraphNode>();
		q.add(node);
		while(!q.isEmpty()) {
			UndirectedGraphNode curr = q.poll();
			if(!map.containsKey(curr.label))    map.put(curr.label, new UndirectedGraphNode(curr.label));
			if(curr != null) {
				for(UndirectedGraphNode neighborNode : curr.neighbors){
					if(!map.containsKey(neighborNode.label)) {
						q.add(neighborNode);
						map.put(neighborNode.label, new UndirectedGraphNode(neighborNode.label));
					}
					map.get(curr.label).neighbors.add(map.get(neighborNode.label));
				}
			}
		}

		return map.get(node.label);
	}
}
