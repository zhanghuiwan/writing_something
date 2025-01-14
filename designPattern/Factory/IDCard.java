package Factory;


public class IDCard extends Product{
    private String owner;

    @Override
    public void use(){
        System.out.println("use " + owner + " card!");
    }

    IDCard(String owner){
        System.out.println("make " + owner);
        this.owner = owner;
    }

    // public String getOwner(){
    //     return owner;
    // }
}
