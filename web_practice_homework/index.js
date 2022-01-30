var header = document.querySelector('header'),
nav = document.querySelector('nav');
/*
nav에 마우스를 올리면 header 높이를 32.5rem로
nav에서 마우스를 내리면 높이를 6rem으로 변경
*/
nav.addEventListener('mouseover',function(){
    header.style.height = "32.5rem"
})
nav.addEventListener('mouseout',function(){
    header.style.height = "6em"
})