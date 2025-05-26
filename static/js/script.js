function menuSanduiche() {
        const nav = document.querySelector(".menuNavegação nav");
        nav.classList.toggle("show");


// Fecha o menu ao clicar num link (em mobile)
document.querySelectorAll(".menuNavegação nav a").forEach(link => {
    link.addEventListener("click", () => {
        document.querySelector(".menuNavegação nav").classList.remove("show");
    });
});