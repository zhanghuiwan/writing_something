package Bridge;

import java.util.Random;

public class CountDisplay extends Display {
    public CountDisplay(DisplayImpl impl) {
        super(impl);
    }

    public void multiDisplay(int times) {
        open();
        for (int i = 0; i < times; i++) {
            print();
            
        }
        close();
    }

    public void randomDisplay(){
        int randomInt = (int)(Math.random() * 10);
        open();
        for(int i = 0; i < randomInt; i++){
            print();
        }
        close();
    }

    public void father(){
        System.out.println("father-son");
    }
    public void son(){
        System.out.println("son");
    }
}