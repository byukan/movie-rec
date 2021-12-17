/// <reference types="cypress" />

it("existing movie search test", function() {

    cy.visit('http://localhost:5000')
    cy.get('.field').type('Fight Club{enter}')
    cy.wait(2000)
    cy.get(':nth-child(1) > a > img').click()

})

it("movie error page test", function() {

    cy.visit('http://localhost:5000/view_movie')
    
})

it("garbage search test", function() {

    cy.visit('http://localhost:5000')
    cy.get('.field').type('/.,./,{enter}')
    cy.contains('No results to display!')
    
})

it("get random movie from movie error page test", function() {

    cy.visit('http://localhost:5000/view_movie')
    cy.contains('Show Me a Different Movie').click()

})

it("return to search from movie error page test", function() {

    cy.visit('http://localhost:5000/view_movie')
    cy.contains('Go Back to Search Page').click()

})

it("get random movie from existing movie page test", function() {

    cy.visit('http://localhost:5000/view_movie?id=345')
    cy.contains('Show Me a Different Movie').click()

})

it("return to search from existing movie page test", function() {

    cy.visit('http://localhost:5000/view_movie?id=345')
    cy.contains('Go Back to Search Page').click()

})


it("existing movie page test", function() {

    cy.visit('http://localhost:5000/view_movie?id=496')
    cy.get('.movie_name').should('be.visible')

})

it("movie name test", function() {

    cy.visit('http://localhost:5000/view_movie?id=496')
    cy.get('.movie_name').should('be.visible').contains('Letters from Iwo Jima')

})

it ("movie poster test", function() {

    cy.visit('http://localhost:5000/view_movie?id=496')
    cy.get('.imgBx > img').should('have.css', 'width', '300px' )

})
