describe('Remover Cômodo', () => {
    beforeEach(() => {
      cy.visit('/');
    });
  
    it('Remover Cômodo', () => {
        cy.get('form[action*="deleteComodo"]').then(($forms) => {
            const formCount = $forms.length;
            for (let i = 0; i < formCount; i++) {
                cy.get('form[action*="deleteComodo"]').first().find('button').click();
                cy.wait(1000); // Aguarde um segundo para a página ser recarregada
                cy.reload(); // Recarrega a página para garantir que o elemento foi removido
            }
        });
    });
});