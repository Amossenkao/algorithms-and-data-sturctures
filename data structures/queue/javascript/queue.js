class Queue {
	#length;
	#items;
	#head;
	#tail;

	constructor(...items) {
		this.#items = {};
		this.#length = 0;
		this.#head = 0;
		this.#tail = 0;
		this.enqueue(...items);
	}

	enqueue(...items) {
		for (const item of items) {
			this.#items[this.#tail++] = item;
			this.#length++;
		}

		return this;
	}

	dequeue() {
		if (this.isEmpty) return null;

		const removedItem = this.#items[this.#head];
		delete this.#items[this.#head];
		this.#length--;
		this.#head++;
		return removedItem;
	}

	forEach(callback) {
		let index = 0;
		for (const item of this) {
			callback(item, index++);
		}
	}

	includes(item) {
		return Object.values(this.#items).includes(item);
	}

	every(callback) {
		let index = 0;
		for (const item of this) {
			if (!callback(item, index++)) return false;
		}

		return true;
	}

	some(callback) {
		let index = 0;
		for (const item of this) {
			if (callback(item, index++)) return true;
		}

		return false;
	}

	clear() {
		this.#items = {};
		this.#length = 0;
		this.#head = 0;
		this.#tail = 0;
		return this;
	}

	get peek() {
		return this.#items[this.#head];
	}
	get isEmpty() {
		return this.#length == 0;
	}

	get items() {
		return Object.values(this.#items);
	}

	get length() {
		return this.#length;
	}

	[Symbol.iterator] = () => {
		let index = this.#head;
		return {
			next: () => {
				return {
					value: this.#items[index],
					done: index++ == this.#tail,
				};
			},
		};
	};
}

export default Queue;
