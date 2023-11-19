
document.addEventListener("DOMContentLoaded", function () {



 console.log("  ")


 console.log("   http://127.0.0.1:8080/home/                                ")
 console.log(" http://127.0.0.1:8080/about/                                  ")
 console.log(" http://127.0.0.1:8080/custom-accounts/signup/")
 console.log("  http://127.0.0.1:8080/accounts/password_change/")
 console.log("http://127.0.0.1:8080/accounts/password_change/done/")




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
