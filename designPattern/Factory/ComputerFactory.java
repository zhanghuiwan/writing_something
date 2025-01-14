package Factory;

public class ComputerFactory extends Factory{

    @Override
    protected Product createProduct(String owner) {
        return new Computer(owner);
    }
    
}
