// background.js
document.addEventListener('mousemove', (e) => {
    const x = (e.clientX / window.innerWidth) - 0.5;
    const y = (e.clientY / window.innerHeight) - 0.5;

    document.body.style.transform = `translate(${x * 10}px, ${y * 10}px)`;
});