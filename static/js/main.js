
const dots = document.querySelectorAll(".scroll_indicator a");

const removeActiveClass = () => {
    dots.forEach(dot => {
        dot.classList.remove("active");
    })
};

const addActiveClass = (entries, observer) => {
    entries.forEach(entry => {
        if(entry.isIntersecting) {
            console.log(entry.target.id);
            let currentDot = document.querySelector(
                `.scroll_indicator a[href="#${entry.target.id}"]`);
            removeActiveClass();
            currentDot.classList.add("active");
        }
    })
};

const options = {
    threshold: 0.8, 
};

const observer = new IntersectionObserver(addActiveClass, options);

const sections = document.querySelectorAll("section");

sections.forEach(section => {
    observer.observe(section);
});

// for horizontal scroll

const init = function(){
  let items = document.querySelectorAll('.gallery li');
  for (let i = 0; i < items.length; i++){
    items[i].style.minWidth = gra(30,60) + 'vw';
    items[i].style.background = randomColor({luminosity: 'light'});
  }
  cssScrollSnapPolyfill()
}
init();

