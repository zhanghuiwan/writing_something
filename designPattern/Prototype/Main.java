package Prototype;

public class Main {
    public static void main(String[] args) {
        // 准备
        Manager manager = new Manager();
        Product upen = new UnderlinePen('~');
        Product mbox = new MessageBox('*');
        Product sbox = new MessageBox('/');

        manager.register("strong message", upen);
        manager.register("warning box", mbox);
        manager.register("slash box", sbox);

        // 生成
        upen.use("Hello，world.");
        Product p0 = upen.createClone();
        p0.use("Hello");
        
        Product p1 = manager.create("strong message");
        p1.use("Hello，world.");
        Product p2 = manager.create("warning box");
        p2.use("Hello，world.");
        Product p3 = manager.create("slash box");
        p3.use("Hello，world.");
    }
}
