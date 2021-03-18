document.addEventListener('DOMContentLoaded', function () {
    //Stop Inspect Element
    document.onkeydown = function (e) {
        if (event.keyCode == 123) {
            return false;
        }
        if (e.ctrlKey && e.shiftKey && e.keyCode == 'I'.charCodeAt(0)) {
            return false;
        }
        if (e.ctrlKey && e.shiftKey && e.keyCode == 'C'.charCodeAt(0)) {
            return false;
        }
        if (e.ctrlKey && e.shiftKey && e.keyCode == 'J'.charCodeAt(0)) {
            return false;
        }
        if (e.ctrlKey && e.keyCode == 'U'.charCodeAt(0)) {
            return false;
        }
    }

    // User Menu Start
    let userSubMenu = document.querySelector('#user-access');

    document.querySelector('#user-icon').onclick = function () {
        userSubMenu.style.display = 'block';
    };
    window.addEventListener('mouseup', function(event){
        if(event.target != userSubMenu){
            userSubMenu.style.display = 'none';
        }
    });

    
    //Mobile Menu Start
    let showMenu = document.querySelector('#all-menu');
    let closeMenu = document.querySelector('#im');

    document.querySelector('#menu').onclick = function () {
        showMenu.style.display = 'block';
        closeMenu.style.overflow = 'hidden';
    };

    document.querySelector('.close').onclick = function () {
        showMenu.style.display = 'none';
        closeMenu.style.overflow = 'visible';
    };

});