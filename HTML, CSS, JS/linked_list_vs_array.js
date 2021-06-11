class DoublyLinkedList {
    constructor() {
        this.head = this.tail = null;
        this.count = 0;
    }
    addFirst(data) {
        ++this.count;
        const new_node = new DoublyLinkedList.Node(data);
        if(this.head == null) {
            this.head = this.tail = new_node;
        } else {
            this.head.prev = new_node;
            new_node.next = this.head;
            this.head = new_node;
        }
    }
    addLast(data) {
        ++this.count;
        const new_node = new DoublyLinkedList.Node(data);
        if(this.head == null) {
            this.head = this.tail = new_node;
        } else {
            this.tail.next = new_node;
            new_node.prev = this.tail;
            this.tail = new_node;
        }
    }
    getFirst() {
        if(this.head) {
            return this.head.data;
        }
    }
    getLast() {
        if(this.head) {
            return this.tail.data;
        }
    }
    getByIndex(idx) {
        if(idx < this.count / 2) {
            let node = this.head;
            for(let i = 0; i < idx; ++i) {
                node = node.next;
            }
            return node.value;
        } else if(idx < this.count) {
            let node = this.tail;
            for(let i = 0; i < n - idx - 1; ++i) {
                node = node.prev;
            }
            return node.value;
        }
    }
    removeFirst() {
        if(this.head) {
            --this.count;
            const cur_head_data = this.head.data;
            const new_head = this.head.next;
            if(new_head) {
                new_head.prev = null;
            }
            this.head = new_head;
            return cur_head_data;
        }
    }
    removeLast() {
        if(this.head) {
            --this.count;
            const cur_tail_data = this.tail.data;
            const new_tail = this.tail.prev;
            if(new_tail) {
                new_tail.next = null;
            }
            this.tail = new_tail;
            return cur_tail_data;
        }
    }
    [Symbol.iterator]() {
        return {
            cur_node: this.head,
            next() {
                if(this.cur_node == null) {
                    return { done: true };
                } else {
                    const cur_data = this.cur_node.data;
                    this.cur_node = this.cur_node.next;
                    return { done: false, value: cur_data };
                }
            }
        };
    }
}
DoublyLinkedList.Node = class {
    constructor(data) {
        this.data = data;
        this.prev = this.next = null;
    }
}



const n = 100000,
a = "Doubly Linked List",
b = "Array";

console.log(a + " vs " + b);
console.log("\nNotes:");
console.log("- all values are in milliseconds");
console.log("- values can be slightly different each run");
console.log("- wait for all tests are done!");

console.log("\nTests:");


console.log("\nAdd to beginning");

console.log(a);
var arr = new DoublyLinkedList();
var t = Date.now();
for(var i = 0; i < n; ++i) {
    arr.addFirst(i);
}
console.log(Date.now() - t);

console.log(b);
var arr = [];
var t = Date.now();
for(var i = 0; i < n; ++i) {
    arr.unshift(i);
}
console.log(Date.now() - t);


console.log("\nAdd to end");

console.log(a);
var arr = new DoublyLinkedList();
var t = Date.now();
for(var i = 0; i < n; ++i) {
    arr.addLast(i);
}
console.log(Date.now() - t);

console.log(b);
var arr = [];
var t = Date.now();
for(var i = 0; i < n; ++i) {
    arr.push(i);
}
console.log(Date.now() - t);


console.log("\nRemove from beginning");

console.log(a);
var arr = new DoublyLinkedList();
for(var i = 0; i < n; ++i) {
    arr.addLast(i);
}
var t = Date.now();
for(var i = 0; i < n; ++i) {
    arr.removeFirst();
}
console.log(Date.now() - t);

console.log(b);
var arr = [];
for(var i = 0; i < n; ++i) {
    arr.push(i);
}
var t = Date.now();
for(var i = 0; i < n; ++i) {
    arr.shift();
}
console.log(Date.now() - t);


console.log("\nRemove from end");

console.log(a);
var arr = new DoublyLinkedList();
for(var i = 0; i < n; ++i) {
    arr.addLast(i);
}
var t = Date.now();
for(var i = 0; i < n; ++i) {
    arr.removeLast();
}
console.log(Date.now() - t);

console.log(b);
var arr = [];
for(var i = 0; i < n; ++i) {
    arr.push(i);
}
var t = Date.now();
for(var i = 0; i < n; ++i) {
    arr.pop();
}
console.log(Date.now() - t);


console.log("\nIterate through elements");

console.log(a);
var arr = new DoublyLinkedList();
for(var i = 0; i < n; ++i) {
    arr.addLast(i);
}
var t = Date.now();
for(var elem of arr) {}
console.log(Date.now() - t);

console.log(b);
var arr = [];
for(var i = 0; i < n; ++i) {
    arr.push(i);
}
var t = Date.now();
for(var elem of arr) {}
console.log(Date.now() - t);


console.log("\nAccesing elements randomly");

console.log(a);
var arr = new DoublyLinkedList();
for(var i = 0; i < n; ++i) {
    arr.addLast(i);
}
var t = Date.now();
for(var i = 0; i < n; ++i) {
    var elem = arr.getByIndex(Math.floor(Math.random() * n));
}
console.log(Date.now() - t);

console.log(b);
var arr = [];
for(var i = 0; i < n; ++i) {
    arr.push(i);
}
var t = Date.now();
for(var i = 0; i < n; ++i) {
    var elem = arr[Math.floor(Math.random() * n)];
}
console.log(Date.now() - t);

console.log("\nThat is all");
