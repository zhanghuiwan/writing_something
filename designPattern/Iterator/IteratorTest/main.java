package Iterator.IteratorTest;

public class main {
    public static void main(String[] args) {
        BookShelf bookShelf = new BookShelf();
        bookShelf.appendBook(new Book("AAA"));
        bookShelf.appendBook(new Book("BBB"));
        bookShelf.appendBook(new Book("ccc"));
        bookShelf.appendBook(new Book("null"));
        Iterator it = bookShelf.iterator();
        while(it.hasNext()){
            Book book = (Book) it.next();
            System.out.println(book.getName());
        }
    }
    
}
