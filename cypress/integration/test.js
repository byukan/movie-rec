/// <reference types="cypress" />

it ("search test", function (){

    cy.visit('http://localhost:5000')
    cy.get('.field').type('Fight Club{enter}')
    cy.wait(2000)
    cy.get(':nth-child(1) > a > img').click()

})

it ("search garbage", function (){

    cy.visit('http://localhost:5000')
    cy.get('.field').type('/.,./,{enter}')
    cy.contains('Internal error occurred: no results to display!')
    
})


it ("movie buttons test", function (){

    cy.visit('http://localhost:5000/view_movie')
    cy.contains('Show me a different movie').click()

})

it ("movie buttons test", function (){

    cy.visit('http://localhost:5000/view_movie')
    cy.contains('Go Back to Search Page').click()

})

it ("movie buttons test", function (){

    cy.visit('http://localhost:5000/view_movie?id=345')
    cy.contains('Show Me a Different Movie').click()

})

it ("movie buttons test", function (){

    cy.visit('http://localhost:5000/view_movie?id=345')
    cy.contains('Go Back to Search Page').click()

})


it("movie info test", function (){

    cy.visit('http://localhost:5000/view_movie?id=496')
    cy.get('.movie_name').should('be.visible')

})

it.only("movie name test", function (){

    cy.visit('http://localhost:5000/view_movie?id=496')
    cy.get('.movie_name').should('be.visible').contains('Letters from Iwo Jima')

})

it ("movie poster test", function (){

    cy.visit('http://localhost:5000/view_movie?id=496')
    cy.get('.imgBx > img').should('have.css', 'width', '300px' )

})
