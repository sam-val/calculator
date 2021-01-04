const my_grid = document.querySelector(".cal-grid");


const current_op = document.querySelector(".current-op");

const previous_op = document.querySelector(".previous-op");

const ops = ["x", "\u00f7", "-", "+"];
const chars = {"\u00f7":"/", "x":"*"}
var prev;
var just_finished = false; 
var current;

// test 
x = "hello world sam, ".trim();
console.log("minus: ", minus_last_word(x));

my_grid.addEventListener('click', (event) => {
    const nodeName = event.target.nodeName;
    if (nodeName == "BUTTON") {
        var btn = event.target.innerHTML.trim();
        current = current_op.textContent.trim();
        if (isNaN(btn)) {
            // We go through each case where it's not a number

            if (btn == ".") {
                dot();
            }

            else if (btn == "AC") {
                all_clear();
            }

            else if (btn == "=") {
                my_eval();
                return;
            }

            // if operators:
            else if (ops.includes(btn))
            {

                if (typeof prev !== "undefined") {
                    if (current == "0") {
                        current_op.textContent = prev;
                    }
                }

                let precede = what_before(current);
                console.log("before is", precede);
                if (precede == 0) {
                    if (btn != "-") {
                        let minus = minus_last_word(current);
                        console.log('minus test', minus);
                        current_op.textContent = `${minus}` + ` ${btn} `;
                        console.log("test", current_op.textContent);
                    }  else {
                        // if it's a "-" button we add minus sign:
                        current_op.textContent += " -";
                    }

                    

                } else if (precede == 1) {
                    
                    
                } else {
                    // else if it's a number:
                    current_op.textContent += ` ${btn} `;
                }

            } else  { // if 
                bracket(btn);
                
            }

        } else { // if a number:
            
            if (current_op.innerHTML.trim() == "0") {
            current_op.innerHTML = btn;
            }else if (just_finished){
                current_op.innerHTML = btn;
    
            }else {
                current_op.innerHTML += btn;
            }
        }

        if (just_finished) {
            previous_op.textContent = "ans = " + prev;
            just_finished = false;
        }

    }

} );

function what_before(words) {
    /*
        -1: number
        0: operators
        1: minus sign
    */
    let last = last_word(words);
    if (ops.includes(last)) {
        // check the minus sign -- if there is a space:
            let trimmed = current_op.textContent.trim();
            if (trimmed.length != current_op.textContent.length) {
                return 0;
            } else {
                // it's a minus sign not an op:
                return 1;
            }

    } else {
        return -1;
    }
}

function minus_last_word(string) {
    let words = string.split(" ");
    words = words.slice(0, words.length - 1);
    return words.join(" ");
}

function last_word(string) {
    let words = string.split(" ");
    console.log("words", words);
    return words[words.length - 1]; 
}

function my_eval() {
    let expression = current_op.textContent.replace(/[\u00f7,x]/g, c => chars[c]);
    try {
        var rs = eval(expression);
    // is result is the same as expression:
    if (rs == expression) {
        animate_flash(previous_op);
        return;
    }
    } catch (e) {
        previous_op.textContent = "error!" ;
        animate_flash(previous_op);
        return;
    }
    previous_op.textContent = current_op.textContent + " =";
    current_op.textContent = rs;
    prev = rs;
    just_finished = true;
}

function animate_flash(elem) {
    let opacity = 0;
    elem.style.opacity = opacity;
    let id = setInterval(func, 10);
    let value = 5;

    function func() {

        opacity += value;

        if (opacity > 100) {
            clearInterval(id);
            return; 
        }
        elem.style.opacity = opacity;
    }
}

function bracket(btn) {
    let print = btn + " ";
    if (isNaN(last_word(current))) {
        print = " " + btn + " ";
    }
    current_op.textContent += print; 
}


function dot() {
    if (last_word(current).split(".").length - 1 < 1) {
        current_op.textContent += "."; 
    }
};

function all_clear() {
    if (just_finished) {
        current_op.textContent = "0";
    } else {
        let trimmed = current_op.textContent.trim();
        current_op.textContent = trimmed.substring(0,trimmed.length-1).trim(); 
        if ( current_op.textContent == "" ) {
            current_op.textContent = "0";
        }
    }


}; 

