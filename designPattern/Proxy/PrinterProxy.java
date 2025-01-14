package Proxy;

public class PrinterProxy implements Printable {
    private String name;
    // private Printer real;
    private Printable real;
    private String className;

    public PrinterProxy() {
    }

    public PrinterProxy(String name, String className) {// 构造函数
        this.name = name;
        this.className = className;
    }

    public synchronized void setPrinterName(String name) {// 设置名字
        if (real != null) {
            real.setPrinterName(name);
        }
        this.name = name;
    }

    public String getPrinterName() {

        return name;
    }

    public void print(String string) {
        realize();
        real.print(string);
    }

    private synchronized void realize() {
        // if (real == null) {
        //     real = new Printer(name);
        // }
        // if (real == null) {
        //     if("realSubject".equals(realSubject))
        //         real = new Printer(name);
        // }
        if(real == null){
            try{
                real = (Printable) Class.forName(className).getConstructor().newInstance();
                real.setPrinterName(name);
            }catch(ClassNotFoundException e){
                System.err.println("not fount " + className);
            }catch(Exception e){
                e.printStackTrace();
            }
        }

    }

    // String realSubject;
    // public PrinterProxy(String name, String realSubject) {// 构造函数
    //     this.name = name;
    //     this.realSubject = realSubject;
    // }

    
}
