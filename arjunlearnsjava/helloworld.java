import java.sql.Struct;

/**
 * helloworld
 */
class Lol {
    public String name;
    public boolean noob;
    Lol(String na, boolean no) {
        this.name = na;
        this.noob = no;
    }
}

public class helloworld {
    public static void main(String[] args) {
       Lol[] Arj = new Lol[3];
       Arj[0] = new Lol("Arjun", false);
       Arj[1] = new Lol("Steve", false);
       Arj[2] = new Lol("Jeff", true);

        for (int i = 0; i < Arj.length; i++) {
            if (Arj[i].noob) {
                System.out.println(Arj[i].name + " is a noob!");
            } else if (!Arj[i].noob) {
                System.out.println(Arj[i].name + " is not a noob!");
            }
        
        }
    }  
}