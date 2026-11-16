
document.addEventListener('DOMContentLoaded', function () {
    const botaoContraste = document.getElementById('alternar-contraste');

    botaoContraste.addEventListener('click', function () {
        const contrasteAtivo = document.body.classList.toggle('alto-contraste');

        botaoContraste.setAttribute('aria-pressed', contrasteAtivo);
    });
});