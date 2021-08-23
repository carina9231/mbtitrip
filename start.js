const main = document.querySelector("#main")
const qna = document.querySelector("#qna")
const button = document.querySelector("button")



function begin() {
    main.style.WebkitAnimation = "fadeOut 1s";
    main.style.animation = "fadeOut 1s";
    button.style.WebkitAnimation = "fadeOut 1s";
    button.style.animation = "fadeOut 1s";
    setTimeout(() => {
        qna.style.WebkitAnimation = "fadeIn 1s";
        qna.style.animation = "fadeIn 1s";
        setTimeout(() => {
            main.style.display = "none";
            button.style.display = "none";
            qna.style.display = "block";
        }, 500)
    }, 500);
}