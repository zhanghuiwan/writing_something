package BookStore.Strategy;

public class SortAndPrint {
    Comparable[] data;
    Sorter sorter;
    SortAndPrint(Comparable[] data, Sorter sorter){
        this.data = data;
        this.sorter = sorter;
    }

    public void execute(){
        print();
        sorter.sort(data);
        print();
    }

    public void print(){
        for(Comparable cc : data){
            System.out.print(cc+" ");
        }
        System.out.println("");
    }
}
