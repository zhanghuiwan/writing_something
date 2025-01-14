package Builder;

/**
 * 问题描述，现在要生成两个不同的模版代码
 */
public class Main {
    public static void main(String[] args) {

        String choice = "HTMLBuilder";

        /**
         * 最普通的方式，直接创建对象然后调用对象内的方法
         */
        // switch (choice) {
        // case "HTMLBuilder":
        // new HTMLBuilder().makeArticle();
        // new HTMLBuilder().makeArticle();
        // new HTMLBuilder().makeArticle();
        // new HTMLBuilder().makeArticle();
        // break;
        // case "TextBuilder":
        // new TextBuilder().makeArticle();
        // new TextBuilder().makeArticle();
        // new TextBuilder().makeArticle();
        // new TextBuilder().makeArticle();
        // break;
        // }

        /**
         * 使用工厂模式
         * 调用工厂模式创建对象，然后调用对象内的方法
         */
        // Factory.create(choice);

        /**
         * 使用Builder模式
         * 创建对象，然后使用Direcor去调用construct方法来使用textBuilder的内容
         * 总的来说，这个模式就解决了一个问题，比如要多次调用Builder中的复杂内容，为了代码不复杂
         * 将这部分功能拿出来放在Director中进行(代码看上去还是复杂，但是至少功能抽出去了)。
         * 工厂模式只负责创建对象，当然你要把调用的功能写在创建之后也可以。
         */
        Director director = null;
        switch (choice) {
            case "HTMLBuilder":
                HTMLBuilder htmlBuilder = new HTMLBuilder();
                director = new Director(htmlBuilder);   
                break;
            case "TextBuilder":
                TextBuilder textBuilder = new TextBuilder();
                director = new Director(textBuilder);
                break;
            default:
                break;
        }
        director.construct();

    }

}
