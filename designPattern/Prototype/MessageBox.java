package Prototype;

public class MessageBox implements Product{
    private char ulchar;

    public MessageBox(char ulchar) {
        this.ulchar = ulchar;
    }
    
    @Override
    public void use(String s) {
        int length = s.getBytes().length;
        for(int i = 0; i < length + 4; i++){
            System.out.print(ulchar);
        }
        System.out.print("");
        System.out.print("\"" + s + "\"");
        for(int i = 0; i < length + 4; i++){
            System.out.print(ulchar);
        }
        System.out.println("");
    }
    @Override
    public Product createClone() {
        Product p = null;
        try {
            p = (Product) clone();
        } catch (CloneNotSupportedException e) {
            e.printStackTrace();
        }
        return p;
    }
}
