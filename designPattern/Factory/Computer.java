package Factory;

public class Computer extends Product{
    String owner;
    Computer(String owner){
        this.owner = owner;
    }

    @Override
    public void use() {
        System.out.println(owner + "'s computer");
    }
    
}
