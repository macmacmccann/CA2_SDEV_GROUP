
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

var myDiv = document.getElementById("myDiv");
var toggleButton = document.getElementById("toggleButton");

toggleButton.addEventListener("click", function() {
    if (myDiv.clientHeight === 0) {
        myDiv.style.height = "100%"; // Set the height you want when expanded
        myDiv.querySelector("h3").style.display = "block"; // Set the display value for the content
        myDiv.querySelector("h1").style.display = "block"; // Set the display value for the content
        myDiv.querySelector("iframe").style.display = "block"; // Set the display value for the content
    
    
    } else {
        myDiv.querySelector("h3").style.display = "none"; // Set the display value for the content
        myDiv.querySelector("h1").style.display = "none"; // Set the display value for the content
        myDiv.querySelector("iframe").style.display = "none"; // Set the display value for the content
        myDiv.style.height = "0";
    }
});






});
