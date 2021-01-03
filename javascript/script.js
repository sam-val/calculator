const my_grid = document.querySelector(".cal-grid");


const current_op = document.querySelector(".current-op");

const previous_op = document.querySelector(".previous-op");

var prev;
var just_finished = false; 

my_grid.addEventListener('click', (event) => {
    const nodeName = event.target.nodeName;
    if (nodeName == "BUTTON") {
        var btn = event.target.innerHTML.trim();
        var current = current_op.textContent;
        if (isNaN(btn)) {
            if (btn == ".") {
                if (current.split(".").length - 1 < 1) {
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
                just_finished = false;
                current_op.innerHTML = btn;
            }else {
                current_op.innerHTML += btn;
            }

        }
    }
} );

function my_eval() {
    var rs = eval(current_op.textContent);
    current_op.textContent = rs;
    prev = rs;
    previous_op.textContent = "ans = " + prev;
    just_finished = true;
}

function add() {
}

function sub() {
    
}

fu
