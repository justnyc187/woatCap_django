$(".navbar-burger").click(function () {
    // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
    $(".navbar-burger").toggleClass("is-active");
    $(".navbar-menu").toggleClass("is-active");
});
//Movement Animation to happen
const $cards = $(".card");
const container = document.querySelector(".container");
//Items
const title = document.querySelector(".title-inventory");
const sneaker = document.querySelector(".sneaker img");
const purchase = document.querySelector(".purchase");
const description = document.querySelector(".info h3");
const sizes = document.querySelector(".sizes");

//Moving Animation Event
$cards.on("mousemove", (e) => {
    const position = $(e.target).parents(".card").eq(0).offset()
    console.log(position)
    let xAxis = (position.left + 280 - e.pageX) / 10;
    let yAxis = (position.top + 465 - e.pageY) / 10;
    $(e.target).parents(".card")[0].style.transform = `rotateY(${xAxis}deg) rotateX(${yAxis}deg)`;
    // $(e.target).parents(".card").children(".card-header")[0].style.transform = "translateZ(150px)";
    // $(e.target).parents(".card").children(".sneaker")[0].style.transform = "translateZ(200px) rotateZ(-45deg)";
});

// $cards.on("mouseenter", (e) => {
//     $(e.target).parents(".card")[0].style.transform = "none";
//     $(e.target).parents(".card")[0].style.transform = "translateZ(150px)";
//     $(e.target).parents(".card").children(".card-header")[0].style.transform = "translateZ(200px) rotateZ(-45deg)";
//     $(e.target).parents(".card").children(".card-header")[0].style.transform = "translateZ(100px)";
//     $(e.target).parents(".card").children(".sneaker")[0].style.transform = "translateZ(75px)";
// });

$cards.on("mouseleave", (e) => {
    // $(e.target).parents(".card")[0].style.transition = "all 0.5s ease";
    $(e.target).parents(".card")[0].style.transform = `rotateY(0deg) rotateX(0deg)`;
    // $(e.target).parents(".card").children(".card-header")[0].style.transform = "translateZ(0px)";
    // $(e.target).parents(".card").children(".sneaker")[0].style.transform = "translateZ(0px) rotateZ(0deg)";
});


