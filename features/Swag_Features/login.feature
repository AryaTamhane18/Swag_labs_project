Feature: SwagLab login
  @SwagLabs_login
   Scenario: Successful login to SwagLabs page
     Given user navigates to the SwagLab page
     When user enters the username
     And user enters the password
     And user clicks on the login button
     Then user should see the homepage