class Stack {
	private _items: { [key: number]: any };
	private _length: number;
	constructor(...items: any) {
		this._items = {};
		this._length = 0;
		this.push(...items);
	}

	push(...items: any): Stack {
		for (const item of items) {
			this._items[this._length] = item;
			this._length++;
		}
		return this;
	}

	pop() {
		if (this.isEmpty) return null;

		const removedItem = this._items[--this._length];
		delete this._items[this._length];
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

	clear(): Stack {
		this._items = {};
		this._length = 0;
		return this;
	}
	get peek() {
		return this._items[this._length - 1];
	}

	get items() {
		return Object.values(this._items);
	}

	get length(): number {
		return this._length;
	}

	get isEmpty(): boolean {
		return this._length == 0;
	}

	[Symbol.iterator] = () => {
		let index = 0;
		return {
			next: () => {
				return {
					value: this._items[index],
					done: index++ == this._length,
				};
			},
		};
	};
}

export default Stack;
