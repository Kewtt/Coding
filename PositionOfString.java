/**
 * Find position of 1 string in another string .
 * @author bismoy
 *
 */
public class PositionOfString {

	public static void main(String args[]) {
		String s1 = "staccareerstack";
		String s2= "stack";
		int j=0,len=0, pos=0;
		for(int i=0;i<s1.length();i++) {
			if(j!=0 && s1.charAt(i)!=s2.charAt(j)) {
				j=0;
				len=0;
			}
			
			if(s1.charAt(i) == s2.charAt(j)) {
				if(j==0) {
					pos = i+1;
				}
				len++;
				j++;
			}
			
			if(len == s2.length()) {
				System.out.println("String found in position : " +pos);
				break;
			} 
			
		}
		
	}
	
}
