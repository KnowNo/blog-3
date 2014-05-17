public class Solution {
    public static void main(String[] args) {
        assert is_valid_parentheses(''); // empty is valid
        assert is_valid_parentheses('*');
        assert is_valid_parentheses('()');
        assert is_valid_parentheses('{}');
        assert is_valid_parentheses('[]');
        assert is_valid_parentheses('{()}');
        assert is_valid_parentheses('([{}])');
        
        
        
        assert is_valid_parentheses('([)]');
    }
    
    
    public static boolean is_valid_parentheses(final String input) {
        assert input != null
        
        HashMap<Character, Character> charMap = new HashMap<Character ,Character>();
        charMap['{'] = '}';
        charMap['['] = ']';
        charMap['('] = ')';
        
        Stack<Character> st = new Stack<Character>();
        for(Character ch: input.toCharArray()) {
            if(charMap.keySet().contains(ch)) { // BUG: why this always returns false
                println ch
                st.push(ch);
            } else if(charMap.values().contains(ch)) {
                if (!st.empty() && ch.equals(st.peek())) {
                    st.pop();
                }
            }
        }
        return st.empty();
    }
}
