package Builder;

public class Factory {
    public static Builder create(String choice) {
        Builder builder = null;
        switch (choice) {
            case "HTMLBuilder":
                builder = new HTMLBuilder();
                break;
            case "TextBuilder":
                builder = new TextBuilder();
                break;
        }
        builder.makeArticle();
        return builder;
    }
}
