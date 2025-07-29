var btn = document.getElementById("menu-button");
var menu = document.getElementById("menu-list");

function toggleMenu(){
    if (menu.style.display === "none" || menu.style.display === "") {
        menu.style.display = "block";
    } else {
        menu.style.display = "none";
    }
}