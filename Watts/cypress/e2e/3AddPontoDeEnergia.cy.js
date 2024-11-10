describe('Adicionar Ponto de Energia', () => {
  beforeEach(() => {
    cy.visit('/');
  });

  it('Adicionar Ponto de Energia com sucesso', () => {
    // Navegar para a página de adicionar ponto de energia
    cy.get('[href="/addPontodeenergia/"]').click();
    cy.get('#locacao').select('Predio Boa Vista');
    cy.get('#comodo').select('Sala');
    cy.get('#nome').type('Lg dual Inverter');
    cy.get('#gastos').type('22');
    cy.get('#quantidade').type('1');
    cy.get('button').click();

    // Verificar se a URL está correta após a submissão
    cy.url().should('eq', 'http://127.0.0.1:8000/');
  });

  it('Adicionar segundo Ponto de Energia com sucesso', () => {
    // Navegar para a página de adicionar ponto de energia
    cy.get('[href="/addPontodeenergia/"]').click();
    cy.get('#locacao').select('Predio Vila Olimpia');
    cy.get('#comodo').select('Quarto de Visitas');
    cy.get('#nome').type('Ventilador de Mesa 30cm Super Power');
    cy.get('#gastos').type('1.35');
    cy.get('#quantidade').type('2');
    cy.get('button').click();

    // Verificar se a URL está correta após a submissão
    cy.url().should('eq', 'http://127.0.0.1:8000/');
  });

  it('Adicionar Ponto de Energia com nome vazio', () => {
    cy.get('[href="/addPontodeenergia/"]').click();
    cy.get('#locacao').select('Predio Boa Vista');
    cy.get('#comodo').select('Sala');
    cy.get('#gastos').type('22');
    cy.get('#quantidade').type('1');
    cy.get('button').click();
    cy.contains('O campo nome é obrigatório').should('be.visible');
  });

  it('Adicionar Ponto de Energia com gastos vazio', () => {
    cy.get('[href="/addPontodeenergia/"]').click();
    cy.get('#locacao').select('Predio Boa Vista');
    cy.get('#comodo').select('Sala');
    cy.get('#nome').type('Lg dual Inverter');
    cy.get('#quantidade').type('1');
    cy.get('button').click();
    cy.contains('O campo gastos é obrigatório').should('be.visible');
  });

  it('Adicionar Ponto de Energia com quantidade vazia', () => {
    cy.get('[href="/addPontodeenergia/"]').click();
    cy.get('#locacao').select('Predio Boa Vista');
    cy.get('#comodo').select('Sala');
    cy.get('#nome').type('Lg dual Inverter');
    cy.get('#gastos').type('22');
    cy.get('button').click();
    cy.contains('O campo quantidade é obrigatório').should('be.visible');
  });

  it('Adicionar Ponto de Energia com gastos negativo', () => {
    cy.get('[href="/addPontodeenergia/"]').click();
    cy.get('#locacao').select('Predio Boa Vista');
    cy.get('#comodo').select('Sala');
    cy.get('#nome').type('Lg dual Inverter');
    cy.get('#gastos').type('-22');
    cy.get('#quantidade').type('1');
    cy.get('button').click();
    cy.contains('O campo gastos não pode ser negativo').should('be.visible');
  });

  it('Adicionar Ponto de Energia com quantidade negativa', () => {
    cy.get('[href="/addPontodeenergia/"]').click();
    cy.get('#locacao').select('Predio Boa Vista');
    cy.get('#comodo').select('Sala');
    cy.get('#nome').type('Lg dual Inverter');
    cy.get('#gastos').type('22');
    cy.get('#quantidade').type('-1');
    cy.get('button').click();
    cy.contains('O campo quantidade não pode ser negativo').should('be.visible');
  });

  it('Adicionar Ponto de Energia com cômodo não pertencente à locação', () => {
    cy.get('[href="/addPontodeenergia/"]').click();
    cy.get('#locacao').select('Predio Boa Vista');
    cy.get('#comodo').select('Quarto de Visitas'); // Supondo que este cômodo não pertence à locação 'Predio Boa Vista'
    cy.get('#nome').type('Lg dual Inverter');
    cy.get('#gastos').type('22');
    cy.get('#quantidade').type('1');
    cy.get('button').click();
    cy.contains('Cômodo não pertence à locação').should('be.visible');
  });
});



