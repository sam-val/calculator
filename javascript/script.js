const my_grid = document.querySelector(".cal-grid");


const current_op = document.querySelector(".current-op");

const previous_op = document.querySelector(".previous-op");



my_grid.addEventListener('click', (event) => {
    const nodeName = event.target.nodeName;
    if (nodeName == "BUTTON") {
        var btn = event.target.innerHTML;
        if (isNaN(btn)) {

        } else {
            console.log(btn);
            if (current_op.innerHTML.trim() == "0") {
            current_op.innerHTML = btn;
            }else {
                current_op.innerHTML += btn;
            }

        }
    }
} )

function hello() {
    console.log("number 77777777");
}