class Node {
	value: any;
	next: any;
	constructor(data: any, next = null) {
		this.value = data;
		this.next = next;
	}
}

export default Node;
