package Factory;

public class AnotherFactory {
    
    public static Product createIDCard(String str){
        return new IDCard(str);
    }
}
