import Node from './node';

class LinkedList {
	private _head: any;
	private _length: number;
	constructor(head: any = null) {
		this._head = null;
		this._length = 0;
		head !== null && this.prepend(head);
	}

	append(...data: any) {
		for (const item of data) {
			if (this.isEmpty) {
				this._head = new Node(item);
				this._length++;
				continue;
			}

			let current = this._head;
			while (current.next) {
				current = current.next;
			}
			current.next = new Node(item);
			this._length++;
		}

		return this;
	}

	prepend(...data: any) {
		for (const item of data) {
			this._head = new Node(item, this._head);
			this._length++;
		}

		return this;
	}

	deleteHead() {
		if (this.isEmpty) return null;
		const data = this._head.value;
		this._head = this._head.next;
		this._length--;
		return data;
	}

	deleteTail() {
		if (this.isEmpty) return null;

		if (this._length == 1) {
			const data = this._head.value;
			this._head = null;
			this._length--;
			return data;
		}
		let previous = this._head;
		let current = previous.next;
		while (current.next) {
			current = current.next;
			previous = previous.next;
		}

		const data = current.value;
		previous.next = null;
		this._length--;
		return data;
	}

	display() {
		let list = '';
		for (const item of this) {
			list += `${item} -> `;
		}

		list += 'null';
		console.log(list);
	}

	get isEmpty() {
		return this._length === 0;
	}

	get length(): number {
		return this._length;
	}

	// get head() {
	// 	return this._head;
	// }

	get tail() {
		if (this.isEmpty) return null;

		let current = this._head;
		while (current.next) {
			current = current.next;
		}

		return current.value;
	}

	[Symbol.iterator] = () => {
		let current = this._head;
		return {
			next: () => {
				let value = current?.value;
				current = current?.next;
				return {
					value,
					done: value == undefined,
				};
			},
		};
	};
}

const list = new LinkedList(5);
list.prepend(4, 6);

const row = ['dwarves'];
const col = ['quiz', 'job'];
let table = new Array(row.length);
table = table.fill('').map(() => new Array(col.length).fill(''));

function fillTable() {
	for (let i = 0; i < row.length; i++) {
		outter: for (let j = 0; j < col.length; j++) {
			for (let char of row[i]) {
				if (col[j].includes(char)) {
					table[i][j] = char;
					continue outter;
				}
			}
		}
	}
}

function findSecrectDirective() {
	fillTable();
	let directive = '';
	for (let i = 0; i < row.length; i++) {
		for (let j = 0; j < col.length; j++) {
			if (table[i][j]) {
				let word = '';
				let a = i,
					b = j;
				while (a < row.length && b < col.length) {
					word += table[a][b];
					a++;
					b++;
				}
				directive = word.length > directive.length ? word : directive;
			}
		}
	}
	directive = directive == '' ? '-' : directive;
	console.log(directive);
}

findSecrectDirective();
