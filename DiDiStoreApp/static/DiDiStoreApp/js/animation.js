let bdy = document.body;


let search_line = document.querySelector('.search_line');
let search_icon = document.getElementById('search_icon');
let search_form = document.querySelector('.search_form');
search_icon.addEventListener('click', ()=>{
    search_line.classList.toggle('search_line_open');
    search_form.classList.toggle('search_form_animation');
});


// const showHideWindows = (show_prop, hide_prop, classList_prop, toggler_prop)=>{

//     show_prop.addEventListener('click', ()=>{
//         classList_prop.classList.toggle(toggler_prop);
//         bdy.style.overflowY = 'hidden';
        
//     });
//     hide_prop.addEventListener('click', ()=>{
//         classList_prop.classList.toggle(toggler_prop);
//         bdy.style.overflowY = 'auto';
//     });
// }

// let category_window = document.querySelector('.category_window');
// let hide_categories = document.getElementById('hide_categories');
// let show_categories = document.getElementById('show_categories');
// showHideWindows(show_categories,hide_categories,category_window,'show_window');


// let hide_registrations = document.getElementById('hide_registrations');
// let show_registrations = document.getElementById('show_registrations');
// showHideWindows(show_registrations,hide_registrations,registration_window,'show_window');

document.addEventListener('click', (e)=>{
    let id = e.target.dataset.toggleId;
    if(!id) return;
    let background = document.getElementById(id);
    background.hidden = !background.hidden;
})
  
let registration_window = document.querySelector('.registration_window');
let sign_up = document.querySelector('.sign_up');
let sign_in = document.querySelector('.sign_in');

let sign_up_btn = document.getElementById('#sign_up').addEventListener('click',()=>{
    registration_window.classList.remove('registration_window_sign_in')
    sign_in.style.display = 'none';
    sign_up.style.display = 'block';
});
let sign_in_btn = document.getElementById('#sign_in').addEventListener('click',()=>{
    registration_window.classList.add('registration_window_sign_in')
    sign_in.style.display = 'block';
    sign_up.style.display = 'none';
});



