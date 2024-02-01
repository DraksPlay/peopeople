export default {

    updated(el) {
        el.scrollTop = el.scrollHeight;
        console.log(el);
    },
    
    name: "scroll_down"
}