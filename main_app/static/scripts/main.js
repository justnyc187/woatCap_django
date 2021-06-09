$(".navbar-burger").click(function () {
    // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
    $(".navbar-burger").toggleClass("is-active");
    $(".navbar-menu").toggleClass("is-active");
});


// // ANIMATION

// //Movement Animation to happen
// const card1 = document.querySelector(".card1");
// const container1 = document.querySelector(".container1");
// //Items
// const title1 = document.querySelector(".title1");
// const sneaker1 = document.querySelector(".sneaker1 img");
// const purchase1 = document.querySelector(".purchase1");
// const description1 = document.querySelector(".info1 h3");
// const sizes1 = document.querySelector(".sizes1");

// //Moving Animation Event
// container1.addEventListener("mousemove", (e) => {
//     let xAxis = (window.innerWidth / 2 - e.pageX) / 25;
//     let yAxis = (window.innerHeight / 2 - e.pageY) / 25;
//     card1.style.transform = `rotateY(${xAxis}deg) rotateX(${yAxis}deg)`;
// });
// //Animate In
// container1.addEventListener("mouseenter", (e) => {
//     card1.style.transition = "none";
//     //Popout
//     title1.style.transform = "translateZ(150px)";
//     sneaker1.style.transform = "translateZ(200px) rotateZ(-45deg)";
//     description1.style.transform = "translateZ(125px)";
//     sizes1.style.transform = "translateZ(100px)";
//     purchase1.style.transform = "translateZ(75px)";
// });
// //Animate Out
// container1.addEventListener("mouseleave", (e) => {
//     card1.style.transition = "all 0.5s ease";
//     card1.style.transform = `rotateY(0deg) rotateX(0deg)`;
//     //Popback
//     title1.style.transform = "translateZ(0px)";
//     sneaker1.style.transform = "translateZ(0px) rotateZ(0deg)";
//     description1.style.transform = "translateZ(0px)";
//     sizes1.style.transform = "translateZ(0px)";
//     purchase1.style.transform = "translateZ(0px)";
// });





//Movement Animation to happen
const $cards = $(".card");
const container = document.querySelector(".container");
//Items
// const title = document.querySelector(".title-inventory");
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
});
$cards.on("mouseleave", (e) => {
    $(e.target).parents(".card")[0].style.transform = `rotateY(0deg) rotateX(0deg)`;
});


// MODAL
const editButton = document.querySelector('#edit-btn');
const modalBg = document.querySelector('.modal-background');
const modal = document.querySelector('.modal');

editButton.addEventListener('click', () => {
    console.log("modal working?")
    modal.classList.add('is-active');
});

modalBg.addEventListener('click', () => {
    modal.classList.remove('is-active');
});