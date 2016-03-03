import java.util.ArrayList;
import java.util.HashMap;
import java.util.Date;
import java.util.Iterator;
import java.text.SimpleDateFormat;
import java.io.BufferedReader;
import java.io.FileReader;

public class Solution{
	
	public static void main(String[] args){
		String filename = "input_1.txt";
		parseInput(filename);
	}
	
	public static void parseInput(String filename){
		Date dt;
		SimpleDateFormat ft = new SimpleDateFormat("(MM/dd/yyyy-HH:mm:ss)");
		Date start = new Date();
		Date connected = new Date();
		Date disconnected = new Date();
		Date stop = new Date();
		long connectedDuration = 0;
		long loggedDuration = 0;

		String line = null;
		try {
		    FileReader fileReader = new FileReader(filename);
		    BufferedReader bufferedReader = new BufferedReader(fileReader);
		    while((line = bufferedReader.readLine()) != null){
		    	String[] input = line.split("::");
			dt = ft.parse(input[0].trim());
			if (input[1].trim().equals("START")){
				start = dt;	
			}
			if (input[1].trim().equals("CONNECTED")){
				connected = dt;				
			}
			if (input[1].trim().equals("DISCONNECTED")){
				disconnected = dt;
				connectedDuration += disconnected.getTime() - connected.getTime();
			}
			if (input[1].trim().equals("SHUTDOWN")){
				stop = dt;
				loggedDuration += stop.getTime() - start.getTime();
				if(connected.after(disconnected)) {
					connectedDuration += stop.getTime() - connected.getTime();
				}
			}
		    }
		    bufferedReader.close();	
		}
		catch(Exception ex){
			System.out.println("Exception occurred when opening file:" + filename);
		}
	
		System.out.println("connected duration is"+ connectedDuration);
		System.out.println("logged duration is"+ loggedDuration);
		float percentage = (float) connectedDuration / (float) loggedDuration * 100 ;
		int perc = (int) percentage;
		String str = String.valueOf(perc).concat("%");
		System.out.println(str);
	}

	/*
	public static void calculateConnectionRatio(HashMap<Date, String> map){
		int line_counter = 0;
		Date start = new Date();
		//System.out.println("start is initialized to :" + start);
		Date connected = new Date();
		Date disconnected = new Date();
		Date stop = new Date();
		long connectedDuration = 0;
		long loggedDuration = 0;
		Iterator it = map.entrySet().iterator();
		while (it.hasNext()) {
			HashMap.Entry pair = (HashMap.Entry)it.next();
			if (pair.getValue().equals("START")){
				start = (java.util.Date)pair.getKey();
			}
			if (pair.getValue().equals("CONNECTED")) {
				connected = (java.util.Date)pair.getKey();
			}
			if (pair.getValue().equals("DISCONNECTED")) {
				disconnected = (java.util.Date)pair.getKey();
				connectedDuration += disconnected.getTime() - connected.getTime();
			}
			if (pair.getValue().equals("SHUTDOWN")) {
				stop = (java.util.Date)pair.getKey();
				loggedDuration += stop.getTime() - start.getTime();
			}
			
			it.remove();
		}
		float percentage = (float) connectedDuration/loggedDuration;
		System.out.printf("final percentage is:%f\n",percentage);
	}
	*/
}
