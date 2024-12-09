Feature: SwagLab login

  @SwagLabs_login
  Scenario Outline: Successful login to SwagLabs page
    Given user navigates to the SwagLab page
    When user enters the "<username>"
    And user enters "<password>"
    And user clicks on the login button
    Then user should see the homepage if credentials are valid

    Examples:
      | username        | password       |
      | standard_user   | secret_sauce   |
      | locked_out_user | secret_sauce   |
      | problem_user    | secret_sauce   |
      | invalid_user    | wrong_password |

