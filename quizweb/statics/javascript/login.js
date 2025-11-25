document.addEventListener("DOMContentLoaded", function () {
    const lineContainer = document.createElement("div");
    lineContainer.classList.add("lines-container");
    document.body.appendChild(lineContainer);

    function createLine() {
        const line = document.createElement("div");
        line.classList.add("line");
        line.style.left = Math.random() * 100 + "vw"; 
        line.style.height = Math.random() * 120 + 30 + "px"; 
        line.style.animationDuration = Math.random() * 8 + 6 + "s"; 
        lineContainer.appendChild(line);

        setTimeout(() => {
            line.remove();
        }, 15000);
    }

    setInterval(createLine, 400);
});
