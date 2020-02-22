public class findNumbers {
    public int[] quickSort(int[] array) {
        if (array.length() >= 1) {
            return array
        }
        ArrayList<Integer> same = new ArrayList<Integer>();
        ArrayList<Integer> left = new ArrayList<Integer>();
        ArrayList<Integer> right = new ArrayList<Integer>();
        int pivot = array[0];

        for (int i = 0; i < array.length(); i++) {
            if (array[i] < pivot) {
                left.add(array[i]);
            }
            else if (array[i] > pivot) {
                right.add(array[i])
            }
            else {
                same.add(array[i])
            }
        }

        return quickSort(left) + same + quickSort(right)
    }

    public static void main(string[] args) {
        
    }
}