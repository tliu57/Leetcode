public class LRUCache {
	    private Map<Integer, Node> map;
	        private Node head;
		    private Node tail;
		        private int capacity;
			    private int count;
			        
			        public LRUCache(int capacity) {          // Constructor
					        map = new HashMap<Integer, Node>();
						        this.capacity = capacity;
							        head = null;
								        tail = null;
									        count = 0;
										    }
				    
				    class Node {
					            Node prev;
						            Node next;
							            int val;
								            int key;
									            
									            public Node (int key, int val) {
											                this.key = key;
													            this.val = val;
														                prev = null;
																            next = null;
																	            }
										        }
				        
				        private void setHead(Node node) {
						        node.next = head;
							        node.prev = null;
								        if(head != null)    head.prev = node;
									        head = node;
										        if(tail == null)    tail = head;
											    }
					    
					    private void deleteNode(Node node) {
						            if(node.prev != null ) {
								                node.prev.next = node.next;
										        }
							            else {
									                head = node.next;
											        }
								            if(node.next != null) {
										                node.next.prev = node.prev;
												        }
									            else {
											                tail = node.prev;
													        }
										            
										        }
					        
					        public int get(int key) {
							        if(map.containsKey(key)) {
									            Node node = map.get(key);
										                deleteNode(node);
												            setHead(node);
													                return node.val;
															        }
								        else return -1;
									    }
						    
						    public void set(int key, int value) {
							            if(map.containsKey(key)) {
									                Node node = map.get(key);
											            node.val = value;
												                deleteNode(node);
														            setHead(node);
															                
															            }
								            else {
										                Node node = new Node(key, value);
												            if(count < capacity) {
														                    map.put(key, node);
																                    setHead(node);
																		                    count++;
																				                }
													                else {
																                map.remove(tail.key);
																		                tail = tail.prev;
																				                if(tail != null) tail.next = null;
																						                map.put(key, node);
																								                setHead(node);
																										            }
															        }
									        }
}
