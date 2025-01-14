package Bridge;

public class Main {
    public static void main(String[] args) {
        Display dl = new Display(new StringDisplayImpl("Hello,China."));
        Display d2 = new CountDisplay(new StringDisplayImpl("Hello, World."));
        CountDisplay d3 = new CountDisplay(new StringDisplayImpl("Hello，Universe."));
        dl.display();
        d2.display();
        d3.display();
        d3.multiDisplay(5);

        CountDisplay d4 = new CountDisplay(new StringDisplayImpl("d4d4"));
        d4.randomDisplay();

        Display a = new CountDisplay(null);
        CountDisplay b = new CountDisplay(null);
        a.father();
        b.father();


        // a.son(); //无法调用
        CountDisplay d = (CountDisplay) a;
        d.son();  //通过向上转型可以调用
        
        b.son();
        

        Display c = new Display(null);
        c.father();
        
    }
}