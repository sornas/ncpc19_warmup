import java.io.*;
import java.util.ArrayList;

public class Digits {
   public static void main(String[] args) throws IOException {
      new Digits().run();
   }
   
   private void run() throws IOException {
      BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
      ArrayList<Integer> integers = new ArrayList<>();
      
      while (true) {
         String input = reader.readLine();
         if (input.equals("END"))
            break;
         if (input.equals("1")) {
            integers.add(1);  // FÖRLÅT :(
            continue;
         }
         integers.add(x_i(input.length(), 0));
      }
      for (int n: integers) {
         System.out.println(n);
      }
      reader.close();
   }
   
   private int x_i(int num, int i) {
      if (num == 1) return i + 2;
      return x_i(Integer.toString(num).length(), i + 1);
   }
}
