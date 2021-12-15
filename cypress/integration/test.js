/// <reference types="cypress" />

it ("search test", function (){

    cy.visit('http://localhost:5000')
    cy.get('.field').type('Fight Club{enter}')
    cy.wait(2000)
    cy.get(':nth-child(1) > a > img').click()

})

it ("movie page test", function (){

    cy.visit('http://localhost:5000/view_movie')
    
})
it ("garbage search test", function (){

    cy.visit('http://localhost:5000')
    cy.get('.field').type('/.,./,{enter}')
    cy.contains('Internal error occurred: no results to display!')
    
})

it ("buttons test1", function (){

    cy.visit('http://localhost:5000/view_movie')
    cy.contains('Show me a different movie').click()

})

it ("buttons test2", function (){

    cy.visit('http://localhost:5000/view_movie')
    cy.contains('Go Back to Search Page').click()

})

it ("buttons test3", function (){

    cy.visit('http://localhost:5000/view_movie?id=345')
    cy.contains('Show Me a Different Movie').click()

})

it ("buttons test4", function (){

    cy.visit('http://localhost:5000/view_movie?id=345')
    cy.contains('Go Back to Search Page').click()

})


it.only ("movie info test", function (){

    cy.visit('http://localhost:5000/view_movie?id=496')
    cy.get('.movie_name').should('be.visible')

})

it ("movie name test", function (){

    cy.visit('http://localhost:5000/view_movie?id=496')
    cy.get('.movie_name').should('be.visible').contains('Letters from Iwo Jima')

})

it ("movie poster test", function (){

    cy.visit('http://localhost:5000/view_movie?id=496')
    cy.get('.imgBx > img').should('have.css', 'width', '300px' )

})
