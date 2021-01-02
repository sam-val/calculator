const my_grid = document.getElementsByClassName("cal-grid")[0];


my_grid.addEventListener('click', (event) => {
    const nodeName = event.target.nodeName;
    if (nodeName == "BUTTON") {
        console.log(event.target.innerHTML);
    }
} )