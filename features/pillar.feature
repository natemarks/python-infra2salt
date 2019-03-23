Feature: Generate pillar from configured and discovered data
    In order to provide infrastructure data to salt
    Devops engineers should be able to
    generate pillars from dynamically discovered IaC data


  Scenario: Runs with good seed data
    Given a path to a valid and complete yaml seed data file
      When a user runs the program
      Then a valid pillar directory structure is created



  Scenario: Return seed data summary in dry run mode
    Given a path to a valid and complete yaml seed data file
      When a user runs the program
      Then a valid pillar directory structure is created
