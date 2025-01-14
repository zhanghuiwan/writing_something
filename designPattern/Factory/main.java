package Factory;

public class main {
    public static void main(String[] args){
        Factory factory = new IDCardFactory();
        Product card1 = factory.create("aaa");
        Product card2 = factory.create("bbb");
        Product card3 = factory.create("ccc");
        card1.use();
        card2.use();

        Product card4 = AnotherFactory.createIDCard("ddd");
        Product card5 = AnotherFactory.createIDCard("eee");
        card4.use();

        Factory factory2 = new ComputerFactory();
        Product computer1 = factory2.create("ffff");
        computer1.use();
    }
}
