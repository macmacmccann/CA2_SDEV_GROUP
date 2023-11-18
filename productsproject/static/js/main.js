
document.addEventListener("DOMContentLoaded", function () {







    console.log("script loaded")



//const elementToAnimate_icon = document.querySelector('.icon');
//createObserver(elementToAnimate_icon, 'animate');



const elementsToAnimate = [
     
    ...document.querySelectorAll('h1'),
    ...document.querySelectorAll('.icon'),
    ...document.querySelectorAll('a'),
    ...document.querySelectorAll('whoamI'),



];


function createObserver(element, animationClass){

    const observer = new IntersectionObserver((entries)=>{
        entries.forEach((entry) => {
            if(entry.isIntersecting) {
                console.log("intereseting")
            element.classList.add(animationClass);
            observer.unobserve(entry.target);
        }
    });
});
        console.log("Observing ")
        observer.observe(element);
}

elementsToAnimate.forEach((element) => {
    createObserver(element, 'animate');
});
});
