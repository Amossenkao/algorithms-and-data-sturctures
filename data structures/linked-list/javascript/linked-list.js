const Node = require('./node');

class LinkedList {
	#head;
	#length;
	constructor(head = null) {
		this.#head = null;
		this.#length = 0;
		head == null || this.append(head);
	}

	append(...data) {
		for (const item of data) {
			if (this.isEmpty) {
				this.#head = new Node(item);
			} else {
				let current = this.#head;
				while (current.next) {
					current = current.next;
				}
				current.next = new Node(item);
			}
			this.#length++;
		}
	}

	prepend(...data) {
		for (let item of data) {
			this.#head = new Node(item, this.#head);
			this.#length++;
		}
	}

	deleteHead() {
		if (this.isEmpty) return null;

		const head = this.#head.value;
		this.#head = this.#head.next;
		this.#length--;
		return head;
	}

	deleteTail() {
		if (this.isEmpty) return null;
		if (this.#length == 1) {
			const data = this.#head.value;
			this.#head = null;
			this.#length--;
			return data;
		}
		let previous = this.#head;
		let current = previous.next;
		while (current.next) {
			current = current.next;
			previous = previous.next;
		}
		const data = current.value;
		previous.next = null;
		this.#length--;
		return data;
	}

	getAt(index) {
		if (this.isEmpty) return null;

		let currentIndex = 0;
		let current = this.#head;
		while (current) {
			if (currentIndex == index) {
				return current.value;
			}
			current = current.next;
			currentIndex++;
		}
	}

	display() {
		let list = '';
		let current = this.#head;
		while (current) {
			list += `${current.value} -> `;
			current = current.next;
		}
		list += 'null';

		console.log(list);
	}

	get isEmpty() {
		return this.#length == 0;
	}

	get length() {
		return this.#length;
	}

	get head() {
		return this.#head?.value ?? null;
	}

	get tail() {
		let current = this.#head;
		while (current?.next) {
			current = current.next;
		}
		return current?.value ?? null;
	}
}

const myList = new LinkedList(45);
myList.append(45, 12, 90);
myList.prepend(78);
myList.display();
console.log(myList.head);
