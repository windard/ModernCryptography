public class quiz43{
    public static boolean checkDigital(long a){
        long            b;
        int             i;
        boolean         flag = true;
        for (i = 6; i >= 0; --i) {
            b = a / (long)Math.pow(10, i) % (long)Math.pow(10, 3);
            // System.out.println(b);

            if (i == 6 && (b % 2) != 0){
                flag = false;
                break;
            }

            if (i == 5 && (b % 3) != 0){
                flag = false;
                break;
            }

            if (i == 4 && (b % 5) != 0){
                flag = false;
                break;
            }

            if (i == 3 && (b % 7) != 0){
                flag = false;
                break;
            }

            if (i == 2 && (b % 11) != 0){
                flag = false;
                break;
            }

            if (i == 1 && (b % 13) != 0){
                flag = false;
                break;
            }

            if (i == 0 && (b % 17) != 0){
                flag = false;
                break;
            }

        }
        return flag;
    }

    public static boolean checkAll(long a){
        int                 i;
        String              s, j;
        boolean             flag = true;
        s = Long.toString(a);
        for (i = 0; i < 10; ++i) {
            j = Integer.toString(i);

            if (s.indexOf(j) < 0) {
                flag = false;
                break;
            }
        }
        return flag;
    }

    public static void main(String[] args) {
        long            i, sum = 0;
        for (i = 1000000001l; i <= 9999999999l; ++i) {
            if(checkDigital(i) && checkAll(i)) {
                System.out.println(i);
                sum += i;
            }
        }
        System.out.println("Sum: " + sum);
        // String             s;
        // s = Integer.toString(1406357289);
        // System.out.println(s.indexOf('1'));
        // System.out.println(checkAll(1234567890));
        // if (checkAll(1406357289)) {
        //     System.out.println(s);
        // }
    }
}

// 1406357289
// 1430952867
// 1460357289
// 4106357289
// 4130952867
// 4160357289
// Sum: 16695334890