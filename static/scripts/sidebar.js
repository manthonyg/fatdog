document.getElementById('menu-toggle').addEventListener('click', function(e) {
    e.preventDefault();
    document.getElementById('wrapper').classList.toggle('toggled')
})

const rer = document.getElementById('rer')
const mer = document.getElementById('mer')

const popoverOptions = {
    trigger: 'focus'
}
const RERpopover = new bootstrap.Popover(rer, popoverOptions)
const MERpopover = new bootstrap.Popover(mer, popoverOptions)