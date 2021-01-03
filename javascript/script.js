const my_grid = document.querySelector(".cal-grid");


const current_op = document.querySelector(".current-op");

const previous_op = document.querySelector(".previous-op");

var prev;
var just_finished = false; 

my_grid.addEventListener('click', (event) => {
    const nodeName = event.target.nodeName;
    if (nodeName == "BUTTON") {
        if (just_finished) {
            previous_op.textContent = "ans = " + prev;
        }
        var btn = event.target.innerHTML.trim();
        var current = current_op.textContent;
        var last_word = current.split(" ");
        last_word = last_word[last_word.length - 1];
        console.log("last word", last_word)
        if (isNaN(btn)) {
            just_finished = false;
            if (btn == ".") {
                if (last_word.split(".").length - 1 < 1) {
                    current_op.textContent += "."; 
                }
                return;
            }

            if (btn == "AC") {
                current_op.textContent = "0";
                return;
            }

            if (btn == "=") {
                my_eval()
                return;
            }

            // if operators:
            if (["x","\u00f7", "-", "+", "="].includes(btn))
            {
                if (prev) {
                    if (current == "0") {
                        current_op.textContent = prev;
                    }
                }
                if (btn == "+") {
                    // check if an operator precedes it:
                    
                    // then do something...

                    // else if it's a number:
                    current_op.textContent += " + ";
                } else if (btn == "-") {
                    
                } else if (btn == "\u00f7") {
                    
                } else {
                    
                }

            } else if (["(", ")"].includes(btn)) { // if 
                
            }

        } else { // if a number:
            
            if (current_op.innerHTML.trim() == "0") {
            current_op.innerHTML = btn;
            }else if (just_finished){
                current_op.innerHTML = btn;
                just_finished = false;
            }else {
                current_op.innerHTML += btn;
            }

        }
        
    }
} );

function my_eval() {
    let expression = current_op.textContent;
    try {
        var rs = eval(expression);
    // is result is the same as expression:
    if (rs == expression) {
        throw "Expresion is unvalid";
    }
    } catch (e) {
        return;
    }
    current_op.textContent = rs;
    prev = rs;
    previous_op.textContent = expression + " =";
    just_finished = true;
}

function add() {
}

function sub() {
    
}

