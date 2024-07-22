class Queue {
	private _items: { [key: number]: any };
	private _length: number;
	private _head: number;
	private _tail: number;

	constructor(...items: any) {
		this._items = {};
		this._length = 0;
		this._head = 0;
		this._tail = 0;
		this.enqueue(...items);
	}

	enqueue(...items: any): Queue {
		for (const item of items) {
			this._items[this._tail++] = item;
			this._length++;
		}

		return this;
	}

	dequeue() {
		if (this.isEmpty) return null;

		const removedItem = this._items[this._head];
		delete this._items[this._head];
		this._length--;
		this._head++;
		return removedItem;
	}

	forEach(callback: Function) {
		let index = 0;
		for (const item of this) {
			callback(item, index++);
		}
	}

	includes(item: any): boolean {
		return Object.values(this._items).includes(item);
	}

	every(callback: Function): boolean {
		let index = 0;
		for (const item of this) {
			if (!callback(item, index++)) return false;
		}

		return true;
	}

	some(callback: Function): boolean {
		let index = 0;
		for (const item of this) {
			if (callback(item, index++)) return true;
		}

		return false;
	}

	clear() {
		this._items = {};
		this._length = 0;
		this._head = 0;
		this._tail = 0;
		return this;
	}

	get peek() {
		return this._items[this._head];
	}
	get isEmpty() {
		return this._length == 0;
	}

	get items() {
		return Object.values(this._items);
	}

	get length() {
		return this._length;
	}

	[Symbol.iterator] = () => {
		let index = this._head;
		return {
			next: () => {
				return {
					value: this._items[index],
					done: index++ == this._tail,
				};
			},
		};
	};
}

export default Queue;
