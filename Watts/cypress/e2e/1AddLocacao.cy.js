describe('Adicionar Locação', () => {
  beforeEach(() => {
    cy.visit('/');
  });

  it('Adicionar Locação com nome vazio', () => {
    cy.get('[href="/addLocacao/"]').click();
    cy.get('#estado').select('Pernambuco');
    cy.get('button').click();
    cy.contains('O campo nome é obrigatório').should('be.visible');
  });

  it('Adicionar Locação com estado vazio', () => {
    cy.get('[href="/addLocacao/"]').click();
    cy.get('#nome').type('Predio Boa Vista');
    cy.get('button').click();
    cy.contains('O campo estado é obrigatório').should('be.visible');
  });

  it('Adicionar Locação com sucesso', () => {
    cy.get('[href="/addLocacao/"]').click();
    cy.get('#nome').type('Predio Boa Vista');
    cy.get('#estado').select('Pernambuco');
    cy.get('button').click();
    cy.url().should('eq', 'http://127.0.0.1:8000/');
  });
  it('Adicionar Segunda Locação com sucesso', () => {
    cy.get('[href="/addLocacao/"]').click();
    cy.get('#nome').type('Predio Vila Olimpia');
    cy.get('#estado').select('São Paulo');
    cy.get('button').click();
    cy.url().should('eq', 'http://127.0.0.1:8000/');
  });
});