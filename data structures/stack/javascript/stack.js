class Stack {
	#items;
	#length;
	constructor(...items) {
		this.#items = {};
		this.#length = 0;
		this.push(...items);
	}

	push(...items) {
		for (const item of items) {
			this.#items[this.#length] = item;
			this.#length++;
		}
		return this;
	}

	pop() {
		if (this.isEmpty) return null;

		const removedItem = this.#items[--this.#length];
		delete this.#items[this.#length];
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
		return this;
	}
	get peek() {
		return this.#items[this.#length - 1];
	}

	get items() {
		return Object.values(this.#items);
	}

	get length() {
		return this.#length;
	}

	get isEmpty() {
		return this.#length == 0;
	}

	[Symbol.iterator] = () => {
		let index = 0;
		return {
			next: () => {
				return {
					value: this.#items[index],
					done: index++ == this.#length,
				};
			},
		};
	};
}

export default Stack;
