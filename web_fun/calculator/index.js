/*
TODO: Anytime a change is made, the entire display string
       is recreated from scratch. Maybe track this and only
       change what is necessary.
TODO: Add backspace
*/

// Linked list node
// Each node is a number with the operation to it's right
// The string_rep only includes this.num not this.op
class Node {
	constructor() {
		this.op = '';
		this.string_rep = "";

		this.next = null;
	}
}

var head_node = new Node();
var current_node = head_node;

var display = document.querySelector("#display");

function press(num) {
	// If an operation was already attached to this node
	// it is time to make a new node
	if(current_node.op.length > 0) {
		var n = new Node();
		current_node.next = n;
		current_node = n;
	}

	current_node.string_rep += num;

	DisplayAllNodes();
}

function press_dot() {
	// Only allow a dot press if there already is a num: (.333 is not allowed but 0.333 is)
	// Only allow dot if one doesn't exist in current num
	// Don't allow dot if op was already attached. That would result in
	// a display string like 3 * .

	if(current_node.string_rep.length > 0 &&
	   !current_node.string_rep.includes('.') &&
	   current_node.op.length === 0) 
	{
		current_node.string_rep += '.';

		DisplayAllNodes();
	}
}

function setOP(op_char) {
	// Must be num to attach op
	if(current_node.string_rep.length > 0)
	{
		// If the last thing added to num was a decimal and no number
		// was added after, add a 0 to end of num
		if(current_node.string_rep[current_node.string_rep.length - 1] === '.') {
			current_node.string_rep += '0';
		}
		current_node.op = op_char;

		DisplayAllNodes();
	}
}

/*
The basic strategy is to walk the linked list 2 times, first doing 
mult / div, then plus / minus.

Every node except the last node will have an op. That means every
node with an op will have a node after it.

We grab the current value, apply the op to current val and next val, and
store it in next.string_rep. Then we unlink the current node from the list and
continue.

By the end, our prev node has the full result so we can just set that to
the new head node after we reprocess it.
*/

function calculate() {
	// Delete last op if no num was created after
	// We don't want "2 + 3 +"
	// Turn it into "2 + 3"
	if(current_node.op.length > 0) {
		current_node.op = '';
	}

	// mult / divide first
	var prev = null;
	var n = head_node;
	while(n) {
		if(n.op === '*') {
			n.next.string_rep = parseFloat(n.string_rep) * parseFloat(n.next.string_rep);
			if(prev) {
				prev.next = n.next;
			}
		}
		else if(n.op === '/') {
			n.next.string_rep = parseFloat(n.string_rep) / parseFloat(n.next.string_rep);
			if(prev) {
				prev.next = n.next;
			}
		}
		prev = n;
		n = n.next;
	}

	// plus / minus
	prev = null;
	n = head_node;
	while(n) {
		if(n.op === '+') {
			n.next.string_rep = parseFloat(n.string_rep) + parseFloat(n.next.string_rep);
		}
		else if(n.op === '-') {
			n.next.string_rep = parseFloat(n.string_rep) - parseFloat(n.next.string_rep);
		}
		prev = n;
		n = n.next;
	}

	// Set result node (prev) to be new head
	head_node = prev;
	// String rep turns into a float so we convert it back
	head_node.string_rep = head_node.string_rep.toString();
	current_node = head_node;

	DisplayAllNodes();
}

function clr() {
	display.innerHTML = "";

	// TODO: Does this enable all nodes for the garbage collector ??
	head_node = null;
	head_node = new Node();
	current_node = head_node;
}

function backspace() {
	if(current_node.op.length > 0) {
		current_node.op = '';
		DisplayAllNodes();
	}
	else if(current_node.string_rep.length > 0) {
		current_node.string_rep = current_node.string_rep.substring(0, current_node.string_rep.length - 1);
		current_node.num = parseFloat(current_node.string_rep);
		DisplayAllNodes();
	}

	if(current_node.string_rep.length === 0) {
		// go to previous node
		console.log("should go to prev node now");
	}
}

function DisplayAllNodes() {
	var display_string = "";
	var n = head_node;
	while(n != null) {
		if(n.string_rep.length > 0) {
			display_string += n.string_rep;
		}
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