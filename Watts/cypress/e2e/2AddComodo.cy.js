describe('Adicionar Comodo', () => {
  beforeEach(() => {
    cy.visit('/');
  });

  it('Adicionar Comodo com nome vazio', () => {
    cy.get('[href="/addComodo/"]').click();
    cy.get('#locacao').select('Predio Vila Olimpia');
    cy.get('button').click();
    cy.contains('O campo nome é obrigatório').should('be.visible');
  });

  it('Adicionar Segundo Comodo com locação vazia', () => {
    cy.get('[href="/addComodo/"]').click();
    cy.get('#nome').type('Sala');
    cy.get('button').click();
    cy.contains('O campo locação é obrigatório').should('be.visible');
  });

  it('Adicionar Terceiro Comodo com sucesso', () => {
    cy.get('[href="/addComodo/"]').click();
    cy.get('#nome').type('Sala');
    cy.get('#locacao').select('Predio Boa Vista');
    cy.get('button').click();
    cy.url().should('eq', 'http://127.0.0.1:8000/');
  });

  it('Adicionar Segundo Comodo com sucesso', () => {
    cy.get('[href="/addComodo/"]').click();
    cy.get('#nome').type('Quarto');
    cy.get('#locacao').select('Predio Boa Vista');
    cy.get('button').click();
    cy.url().should('eq', 'http://127.0.0.1:8000/');
  });

  it('Adicionar Terceiro Comodo com sucesso', () => {
    cy.get('[href="/addComodo/"]').click();
    cy.get('#nome').type('Quarto de Visitas');
    cy.get('#locacao').select('Predio Vila Olimpia');
    cy.get('button').click();
    cy.url().should('eq', 'http://127.0.0.1:8000/');
  });
});