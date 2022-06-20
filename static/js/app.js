const bo = document.querySelector('.boll');


window.addEventListener("mousemove", (e) => {
    bo.style.left = e.pageX + "px";
    bo.style.top = e.pageY + "px";
});