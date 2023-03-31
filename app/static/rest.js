function select_button(button) {
    let route = "/button" + String(button);
    console.log(route);
    fetch(route);
}