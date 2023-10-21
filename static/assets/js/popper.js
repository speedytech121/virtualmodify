// // JavaScript to show and hide the popup for ux
// const webreadMoreLink = document.getElementById('read-more-link-ux');
// const webpopupux = document.getElementById('popup');
// const closePopupux = document.getElementById('close-popup');

// readMoreLink.addEventListener('click', (e) => {
//     e.preventDefault();
//     popupux.style.display = 'block';
// });

// closePopupux.addEventListener('click', (e) => {
//     e.preventDefault();
//     popupux.style.display = 'none';
// });


// JavaScript to show and hide the popup for web
const readMoreweb = document.getElementById('read-more-link-web');
const popupweb = document.getElementById('popupweb');
const closePopupweb = document.getElementById('close-popupweb');

readMoreweb.addEventListener('click', (e) => {
    if (popupweb.style.display!=='block'){
        e.preventDefault();
        popupweb.style.display = 'block';
    }
});

closePopupweb.addEventListener('click', (e) => {
    e.preventDefault();
    popupweb.style.display = 'none';
});


// music
const readMoremusic = document.getElementById('read-more-link-music');
const popupmusic=document.getElementById('popupmusic')
const closePopupmusic=document.getElementById('close-popupmusic')

readMoremusic.addEventListener('click', (e) => {
    if (popupmusic.style.display!='block'){
        e.preventDefault();
        popupmusic.style.display='block'
    }
});
closePopupmusic.addEventListener('click', (e) =>{
    e.preventDefault();
    popupmusic.style.display='none';
});


// uxui
const readMoreuxui = document.getElementById('read-more-link-uxui');
const popupuxui=document.getElementById('popupuxui')
const closePopupuxui=document.getElementById('close-popupuxui')

readMoreuxui.addEventListener('click', (e) => {
    if (popupuxui.style.display!='block'){
        e.preventDefault();
        popupuxui.style.display='block'
    }
    
});
closePopupuxui.addEventListener('click', (e) =>{
    e.preventDefault();
    popupuxui.style.display='none';
});


// digital
const readMoredigital = document.getElementById('read-more-link-digital');
const popupdigital=document.getElementById('popupdigital')
const closePopupdigital=document.getElementById('close-popupdigital')

readMoredigital.addEventListener('click', (e) => {
    if (popupdigital.style.display!='block'){
        e.preventDefault();
        popupdigital.style.display='block'
    }
    
});
closePopupdigital.addEventListener('click', (e) =>{
    e.preventDefault();
    popupdigital.style.display='none';
});
