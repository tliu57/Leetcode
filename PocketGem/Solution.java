import java.io.BufferedReader;
import java.io.FileReader;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.HashSet;

public class Solution{
	
	private static String start = "";
	private static String end = "";
	private static HashMap<String, String[]> map = new HashMap<String, String[]>();

	public static void main(String[] args){
		String filename = "text.txt";
		Solution sol = new Solution();
		map = readinFile(filename);
		
		//System.out.printf("Start is:%s\n", start);
		//System.out.printf("End is:%s\n", end);

		//Set set = ret_map.entrySet();
		//Iterator i = set.iterator();
		//while(i.hasNext()) {
		//	HashMap.Entry me = (HashMap.Entry)i.next();
		//	System.out.print(me.getKey() + ":");
		//	System.out.println(me.getValue());
		HashSet<String> visited = new HashSet<String>();
		ArrayList<String> path = new ArrayList<String>();
		findAllPathUtil(start, end, visited, path, 0);
		}
	
	
	public static HashMap<String, String[]> readinFile(String filename){
		String line = null;
		int line_counter = 0;
		HashMap<String, String[]> map = new HashMap<String, String[]>();
		try {
		    FileReader fileReader = new FileReader(filename);
		    BufferedReader bufferedReader = new BufferedReader(fileReader);

		    while ((line = bufferedReader.readLine()) != null) {
		    	if (line_counter == 0){
				start = line.split("\\s+")[0];
				end = line.split("\\s+")[1];
			}
			else {
				String[] data = line.split(":");
				map.put(data[0],data[1].split("\\s+"));
			}
			line_counter ++;
		    }
		    bufferedReader.close();
		}
		catch(Exception ex) {
			System.out.println("Exception occurred to open file:" + filename + ".");
		}
		return map;
	}

	public static void findAllPathUtil(String begin, String destination, HashSet<String> visited, ArrayList<String> path, int pathIndex){
		visited.add(begin);
		path.add(pathIndex, begin);
		pathIndex ++;
		if (begin == destination) {
			for (int i = 0; i< pathIndex; i++){
				System.out.printf("%s\t",path.get(i));
			}
			System.out.println();
		}
		else {
			String[] values = map.get(begin);
			if(values.length != 0){
				for(String str : values){
					if (!visited.contains(str)){
						findAllPathUtil(str, destination, visited, path, pathIndex);
					}
				}
			}
		}

	}

}
