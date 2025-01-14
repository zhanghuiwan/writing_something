package BookStore.Strategy;

public class Main {

    public static void main(String[] args) {
        String[] books = {"ff", "ap", "bbs", "dde"};
        SortAndPrint sortAndPrint  = new SortAndPrint(books,new RandomSorter());
        sortAndPrint.execute();
    
    }
    
}
