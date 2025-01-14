package BookStore.Strategy;

public class SelectorSorter implements Sorter{

    @Override
    public void sort(Comparable[] data) {
        for(int i = 0; i < data.length - 1; i++){
            for(int j = 0; j < data.length - i - 1; j++){
                if(data[j].compareTo(data[j+1]) > 0){
                    Comparable tem = data[j];
                    data[j] =  data[j+1];
                    data[j+1] = tem;
                }
            }
        }
    }
    
}
