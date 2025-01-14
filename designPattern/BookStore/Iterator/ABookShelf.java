package BookStore.Iterator;

import java.util.ArrayList;
import java.util.List;

public class ABookShelf implements Bookshelf{
    List<Book> bookList;
    int index;

    public ABookShelf(){
        bookList = new ArrayList<>();
    }

    public void append(Book book){
        bookList.add(book);
    }


    public Boolean hasNext(){
        if(index < bookList.size())
            return true;
        else
            return false;
    } 

    public Book next(){
        Book book = bookList.get(index);
        index++;
        return book;
    }
    
}
