class Node {
	constructor() {
		this.num = null;
		this.op = '';
		this.string_rep = "";
		this.next = null;
	}
}

var display = document.querySelector("#display");
var head = new Node();
var current = head;

function press(num) {
	if(current.op.length > 0) {
		var n = new Node();
		current.next = n;
		current = n;
	}

	current.string_rep += num;
	current.num = parseFloat(current.string_rep);

	DisplayAllNodes();
}

function press_dot() {
	if(current.num != null && 
	   !current.string_rep.includes('.') &&
	   current.op.length === 0) 
	{
		current.string_rep += '.';
		console.log(current.string_rep);
		current.num = parseFloat(current.string_rep);

		DisplayAllNodes();
	}
}

function setOP(op_char) {
	if(current.num != null)
	{
		if(current.string_rep[current.string_rep.length - 1] === '.') {
			current.string_rep += '0';
		}
		current.op = op_char;
		DisplayAllNodes();
	}
}

function calculate() {
	if(current.op.length > 0) {
		current.op = '';
	}

	// priority ops first
	var prev = null;
	var n = head;
	while(n) {
		if(n.op === '*') {
			n.next.num = n.num * n.next.num;
			if(prev) {
				prev.next = n.next;
			}
		}
		else if(n.op === '/') {
			n.next.num = n.num / n.next.num;
			if(prev) {
				prev.next = n.next;
			}
		}
		prev = n;
		n = n.next;
	}

	// plus minus
	prev = null;
	n = head;
	while(n) {
		if(n.op === '+') {
			n.next.num = n.num + n.next.num;
		}
		else if(n.op === '-') {
			n.next.num = n.num - n.next.num;
		}
		prev = n;
		n = n.next;
	}

	head = prev;
	head.op = '';
	head.string_rep = "" + head.num;
	current = head;

	DisplayAllNodes();
}

function clr() {
	display.innerHTML = "";

	// TODO: Does this enable all nodes for the garbage collector ??
	head = null;
	head = new Node();
	current = head;
}

function DisplayAllNodes() {
	var display_string = "";
	var n = head;
	while(n != null) {
		display_string += n.string_rep;
		if(n.op.length > 0) {
			display_string += ' ' + n.op + ' ';
		}

		n = n.next;
	}

	display.innerHTML = display_string;
	display.scrollLeft = display.scrollWidth;
}

window.onkeyup = function (event) {
	switch(event.keyCode) {
		// 0
		case 48: {
			press(0);
		} break;

		// 1
		case 49: {
			press(1);
		} break;

		// 2
		case 50: {
			press(2);
		} break;

		// 3
		case 51: {
			press(3);
		} break;

		// 4
		case 52: {
			press(4);
		} break;

		// 5
		case 53: {
			press(5);
		} break;

		// 6
		case 54: {
			press(6);
		} break;

		// 7
		case 55: {
			press(7);
		} break;

		// 8
		case 56: {
			press(8);
		} break;

		// 9
		case 57: {
			press(9);
		} break;

		// plus
		case 187: {
			setOP('+');
		} break;

		// minus
		case 189: {
			setOP('-');
		} break;

		// multiply / x
		case 88: {
			setOP('*');
		} break;

		// divide / /
		case 191: {
			setOP('/');
		} break;

		// dot
		case 190: {
			press_dot();
		} break;

		// esc / clear
		case 27: {
			clr();
		} break;

		// enter / equals
		case 13: {
			calculate();
		} break;
	}
}