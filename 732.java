/*
The idea is to sort all (start, end) pairs by start time.
Then go through all pairs, count+1 for start, count-1 for end.
Find the max count during the whole process.
It needs some data structure like Redblack tree to quickly sort the ranges.
Therefore it is relatively hard for Python, and easy for C++ and Java.
*/
class MyCalendarThree {
    public TreeMap<Integer, Integer> treemap = new TreeMap<Integer, Integer>();

    public MyCalendarThree() {
        treemap = new TreeMap<Integer, Integer>();
    }

    public int book(int start, int end) {
        int temp = 0;
        int maxCount = 0;
        treemap.put(start, treemap.getOrDefault(start, 0) + 1);
        treemap.put(end, treemap.getOrDefault(end, 0) - 1);
        for (int key: treemap.keySet()) {
            temp += treemap.get(key);
            maxCount = Math.max(temp, maxCount);
        }
        return maxCount;
    }
}
