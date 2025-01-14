package Strategy;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.TreeSet;

public class Test {

    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        list.add("test1");
        list.add("test2");
        Iterator<String> it = list.iterator();
        while (it.hasNext()) {
            String str = it.next();
            System.out.println(str);

        }
        TreeSet<Integer> set = new TreeSet<>();
        set.add(3);
        set.add(1);
        set.add(2);
        Iterator<Integer> iterator = set.iterator();
        while (iterator.hasNext()) {
            Integer number = iterator.next();
            System.out.println(number);
        }
    }
}
