

document.addEventListener("DOMContentLoaded", function () {});

    console.log("script loaded")

    if (window.location.pathname === "/home.html") {
        // Code for Page 1
        commonstuff();
        index_load();
    } else if (window.location.pathname === "/services.html") {
        // Code for Page 2
        commonstuff();
        service_load();
    } else {
        // Default common functionality
        commonstuff();
    }


function index_load(){

 //only sstuff for the home.html
}


function service_load(){

    console.log("Service js loaded suc")

   

}


function commonstuff() {


    const elementsToAnimate_slidefrombottom_slow_and_scaleUp = [


        ...document.querySelectorAll('.button_text'),

        ...document.querySelectorAll('.servicetext'),
    ...document.querySelectorAll('.reviewtext'),


    ];


    const elementsToAnimate = [
     
        ...document.querySelectorAll('.slideshow-container'),
        ...document.querySelectorAll('footer'),


    ];

    const elementsToAnimate_slideup = [
        ...document.querySelectorAll('.image_end'),
        /*...document.querySelectorAll('.review_row'),*/
        ...document.querySelectorAll('.header_body_border'),
        ...document.querySelectorAll('.bottom_review_row'),
        ...document.querySelectorAll('.review_row_servicespage'),
        ...document.querySelectorAll('.slideshow_row_manager'),    
        
    ]

    const elementsToAnimate_slideupfromleft = [
        ...document.querySelectorAll('.review_row_alt'),
    
    ]


    const elementsToAnimate_slideupfromright = [
        ...document.querySelectorAll('.image_end'),
        ...document.querySelectorAll('.review_row'),


    ]


    const elementsToAnimate_slideupfromtop_slow = [
        ...document.querySelectorAll('.button_row'),
         ...document.querySelectorAll('.service_title'),


    ]

    function createObserver(element, animationClass){

        const observer = new IntersectionObserver((entries)=>{
            entries.forEach((entry) => {
                if(entry.isIntersecting) {
                element.classList.add(animationClass);
                observer.unobserve(entry.target);
            }
        });
    });
        
            observer.observe(element);
    }



    elementsToAnimate_slidefrombottom_slow_and_scaleUp.forEach((element) => {
        createObserver(element, 'slidefrombottom_slow_and_scaleUp');
    });

    elementsToAnimate.forEach((element) => {
        createObserver(element, 'animate');
    });

    elementsToAnimate_slideup.forEach((element) => {
        createObserver(element, 'slidefrombottom_slow_and_fadeIn');

    });

    elementsToAnimate_slideupfromleft.forEach((element) => {
        createObserver(element, 'slidefromleft_slow_and_fadeIn');

    });
    elementsToAnimate_slideupfromright.forEach((element) => {
        createObserver(element, 'slidefromright_slow_and_fadeIn');

    });

    elementsToAnimate_slideupfromtop_slow.forEach((element) => {
        createObserver(element, 'slidefromtop');

    });
    elementsToAnimate_slideupfromtop_slow.forEach((element) => {
        createObserver(element, 'slidefromtop_slow');

    });



    /*  SINGLE ELEMETNS */ 
    const elementToAnimate_icon = document.querySelector('.icon');



    const elementToAnimate3 = document.querySelector('.containingreviewtext1');
    const elementToAnimate4 = document.querySelector('.containingreviewimage1');
    const elementToAnimate5 = document.querySelector('title');
    const elementToAnimate6 = document.querySelector('ul');
    const elementToAnimate7 = document.querySelector('nav');
    const elementToAnimate_header_body_border = document.querySelector('.header_body_border');
   

    const elementToAnimate9 = document.querySelector('.containingreviewtext2');
    const elementToAnimate10 = document.querySelector('.containingreviewimage2');
    const elementToAnimate11 = document.querySelector('.button_row');

    createObserver(elementToAnimate6, 'slidefrombottom_slow_and_scaleUp');
    createObserver(elementToAnimate_header_body_border, 'slidefrombottom_slow_and_scaleUp');

    createObserver(elementToAnimate7, 'slidefromtop_slow');
    createObserver(elementToAnimate11, 'slidefromtop_slow');

    /* 
    THESE STILL WORKS IF YOU WANT TO ISOLATE ANY 


    createObserver(elementToAnimate1, 'slidefrombottom_fast');
    createObserver(elementToAnimate2, 'animate');
    createObserver(elementToAnimate3, 'slidefrombottom_fast');
    createObserver(elementToAnimate4, 'slidefrombottom_fast');
    createObserver(elementToAnimate5, 'animate');

    createObserver(elementToAnimate8, 'slidefrombottom_slow_and_scaleUp');
    createObserver(elementToAnimate9, 'slidefrombottom_fast');
    createObserver(elementToAnimate10, 'slidefrombottom_fast');

    */
}
