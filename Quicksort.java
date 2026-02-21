public class Quicksort {
    public static void partition(int[] arr) {
        int n = arr.length;
        int pivot = n-1;

        int i= -1;
        for(int j=0;j<n;j++){
            if(arr[j]<=pivot){
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;

            }
        }

         // place the pivot at its correct position
         int temp = arr[i+1];
         arr[i+1] = arr[i-1];
         

    }
    public static void main(String[] args) {
        int[] arr = {5,3,8,9,7};
        partition(arr);

    }
}