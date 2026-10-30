void heapify(int arr[], int n, int i)
{
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && arr[left] > arr[largest])
        largest = left;

    if (right < n && arr[right] > arr[largest])
        largest = right;

    if (largest != i)
    {
        int temp = arr[i];
        arr[i] = arr[largest];
        arr[largest] = temp;

        heapify(arr, n, largest);
    }
}

int* sortArray(int* nums, int numsSize, int* returnSize)
{
    for (int i = numsSize / 2 - 1; i >= 0; i--)
    {
        heapify(nums, numsSize, i);
    }

    for (int i = numsSize - 1; i > 0; i--)
    {
        int temp = nums[0];
        nums[0] = nums[i];
        nums[i] = temp;

        heapify(nums, i, 0);
    }

    *returnSize = numsSize;
    return nums;
}