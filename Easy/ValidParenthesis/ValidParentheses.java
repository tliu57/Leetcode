import java.tuil.*;

boolean isValid(String s) {
        Stack<Integer> stack = new Stack<Integer>();
        if(s.length() <= 1) return false;
        
        for(int i = 0; i < s.length(); i++){
            int num = s.charAt(i); //num is the asc ii code of char i
            if (stack.empty()) stack.push(num);
            
            else if((stack.peek() + 1 == num) || (stack.peek() + 2 == num)){
                stack.pop();
            }
            else
                stack.push(num);
        }
        
            return stack.empty();
    }
