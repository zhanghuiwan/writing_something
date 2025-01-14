package Iterator.IteratorTest;

import java.util.ArrayList;
import java.util.List;

public class BookShelf implements Aggregate{
    private List<Book> bookList;

    public BookShelf(){
        this.bookList = new ArrayList<>();
    }

    public Book getBookAt(int index){
        return bookList.get(index);
    }
    public void appendBook(Book book){
        this.bookList.add(book);
    }
    public int getLength(){
        return bookList.size();
    }

    @Override
    public Iterator iterator() {
        return new BookShelfIterator(this);
    }
}
