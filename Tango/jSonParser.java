/** Input: {
  *		"server": "example.com",
  *		"post": "80",
  *		"message": "hello world"
  *	   }
  *
  * Function: get_value_of(server)
  *
  * Hint: Use enumerate and structs
  *
  */

public class jSonParser {

	public enum InputCondit {
		Initialization,
		LookingForKey,
		ReadingKey,
		LookingForColon,
		LookingForValue,
		ReadingValue,
		LookingForNextIntention

	}

	public HashMap<String, String> parseInput(String s) {
		
		HashMap<String, String> map = new HashMap<String, String>();
		StringBuffer strKey;
		StringBuffer strValue;

		for(int i = 0 ; i < s.length(); i++) {
			switch(InputCondit) {
				case Initialization:
					if(Character.isWhiteSpace(s.charAt(i)))	continue;
					else if(s.charAt(i) == '{') LookingForKey;
					else System.out.println("Wrong format!");
					break;

				case LookingForKey:
					if(Character.isWhiteSpace(s.charAt(i)) continue;
					else if(s.charAt(i) == '\"') ReadingKey;
					else System.out.println("Wrong format!");
					break;

				case ReadingKey:
					strKey = new StringBuffer();
					while(s.charAt(i)!= '\"') strKey.append(s.charAt(i));
					if(s.charAt(i) == '\"') {
						map.put(strKey.toString);
						LookingForColon;
					}

			}
		}	
	}
}


