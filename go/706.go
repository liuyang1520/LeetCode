/*
Sample:
[[Pair(1, 3), Pair(11, 10)], ..., [Pair(10, 5)]] when length of Max is 10
*/

type Pair struct {
    key int
    value int
}

type MyHashMap struct {
    hashmap [][]Pair
}

var Max = 1000

/** Initialize your data structure here. */
func Constructor() MyHashMap {
    hashmap := make([][]Pair, Max)
    for i := 0; i < Max; i++ {
        hashmap[i] = make([]Pair, 0)
    }
    return MyHashMap{
        hashmap: hashmap,
    }
}


/** value will always be non-negative. */
func (this *MyHashMap) Put(key int, value int)  {
    index := key % Max
    for i, _ := range this.hashmap[index] {
        if this.hashmap[index][i].key == key {
            this.hashmap[index][i].value = value
            return
        }
    }
    this.hashmap[index] = append(this.hashmap[index], Pair{
        key: key,
        value: value,
    })
}


/** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
func (this *MyHashMap) Get(key int) int {
    index := key % Max
    for _, pair := range this.hashmap[index] {
        if pair.key == key {
            return pair.value
        }
    }
    return -1
}


/** Removes the mapping of the specified value key if this map contains a mapping for the key */
func (this *MyHashMap) Remove(key int)  {
    index := key % Max
    for i, pair := range this.hashmap[index] {
        if pair.key == key {
            this.hashmap[index] = append(this.hashmap[index][:i], this.hashmap[index][i+1:]...)
            return
        }
    }
}
