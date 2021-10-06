class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int length = nums1.length + nums2.length;
        if (length == 0) {
            return 0.0;
        }
        int i = 0, index1 = 0, index2 = 0;
        while (i < length) {
            if (length % 2 == 0) {
                if (i == (length - 1) / 2) {
                    double median = (double) (((index1 < nums1.length) && ((index2 >= nums2.length) || (nums1[index1] < nums2[index2]))) ? nums1[index1++] : nums2[index2++]);
                    median = (median + ((double) (((index1 < nums1.length) && ((index2 >= nums2.length) || (nums1[index1] < nums2[index2]))) ? nums1[index1++] : nums2[index2++]))) / 2.0;
                    return median;
                } else if ((index1 < nums1.length) && ((index2 >= nums2.length) || (nums1[index1] < nums2[index2]))) {
                    index1++;
                } else {
                    index2++;
                }
            } else {
                if (i == (length) / 2) {
                    double median = (double) (((index1 < nums1.length) && ((index2 >= nums2.length) || (nums1[index1] < nums2[index2]))) ? nums1[index1++] : nums2[index2++]);
                    return median;
                } else if ((index1 < nums1.length) && ((index2 >= nums2.length) || (nums1[index1] < nums2[index2]))) {
                    index1++;
                } else {
                    index2++;
                }
            }
            i++;
        }
        return 0.0;
    }
}
