function popup() {
    const popup = document.querySelector('.popup');

    // Toggle the display property between 'none' and 'block'
    if (popup.style.display === 'none' || popup.style.display === '') {
        popup.style.display = 'block';
    } else {
        popup.style.display = 'none';
    }
}
