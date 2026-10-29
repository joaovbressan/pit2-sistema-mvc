// Interatividade e melhorias de IHC - PIT II

document.addEventListener('DOMContentLoaded', function () {

    // 1. Bloqueio de Duplo Clique no envio de formulários (Feedback do Rodrigo)
    const forms = document.querySelectorAll('form');
    forms.forEach(function (form) {
        form.addEventListener('submit', function (e) {
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn && !submitBtn.disabled) {
                submitBtn.disabled = true;
                const originalText = submitBtn.innerHTML;
                submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Processando...';
                
                // Reativa caso demore mais de 8s (fallback de segurança)
                setTimeout(() => {
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = originalText;
                }, 8000);
            }
        });
    });

    // 2. Limpeza/Reset de formulários ao clicar no botão de Cancelar (Feedback da Beatrice)
    const cancelBtns = document.querySelectorAll('.btn-reset-form');
    cancelBtns.forEach(function (btn) {
        btn.addEventListener('click', function (e) {
            e.preventDefault();
            const form = btn.closest('form');
            if (form) {
                form.reset();
                // Limpa selects se houver
                const inputs = form.querySelectorAll('input, select, textarea');
                inputs.forEach(input => input.classList.remove('is-invalid', 'is-valid'));
            }
        });
    });
});
