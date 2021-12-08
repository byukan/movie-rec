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

it.only ("movie buttons test", function (){

    cy.visit('http://localhost:5000/view_movie')
    cy.contains('Show me a different movie').click()
    
    

})

it.only ("movie buttons test", function (){

    cy.visit('http://localhost:5000/view_movie')
    cy.contains('Go Back to Search Page').click()
    
    

})


it.only ("movie buttons test", function (){

    cy.visit('http://localhost:5000/view_movie?id=345')
    cy.contains('Show Me a Different Movie').click()
    
    

})

it.only ("movie buttons test", function (){

    cy.visit('http://localhost:5000/view_movie?id=345')
    cy.contains('Go Back to Search Page').click()
    
    

})



it("movie name test", function (){

    cy.visit('http://localhost:5000/view_movie?id=496')
    cy.get('.movie_name').should('be.visible')

})


it ("movie poster test", function (){

    cy.visit('http://localhost:5000/view_movie?id=496')
    cy.get('.imgBx > img').should('have.css', 'width', '300px' )

})

