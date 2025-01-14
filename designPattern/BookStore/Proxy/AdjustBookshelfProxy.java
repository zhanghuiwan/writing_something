package BookStore.Proxy;

public class AdjustBookshelfProxy implements AdjustBookshelfable {
    AdjustBookshelf adjustBookshelf;

    @Override
    public void adjust() {

    }

    @Override
    public void printBookshelf() {
        if (adjustBookshelf == null)
            adjustBookshelf = new AdjustBookshelf();
        adjustBookshelf.printBookshelf();

    }

}
