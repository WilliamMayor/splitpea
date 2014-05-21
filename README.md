#splitpea

Share the cost of products equally across the customers. Be transparent in pricing and costs.

## Tasks

- [ ] add user accounts
    - [ ] sign up
    - [ ] log in
    - [ ] log out
    - [ ] see account page
        - [ ] product
            - [ ] summary
            - [ ] profile
            - [ ] costs
            - [ ] customers
        - [ ] customer
            - [ ] products
                - [ ] settings
                    - [ ] email frequency
                    - [ ] tip amount
                    - [ ] leave product
- [ ] add text for home page
- [ ] add text for about page
- [ ] create directory
- [ ] create product profile
    - [ ] JSON breakdown
- [ ] database design
    - User
        - id
        - email (required)
        - password (optional)
            - salt
            - hash
        - stripe
        - email_preference
    - Product
        - id
        - name
        - description
        - website
        - ex_directory
        - admin
    - ProductCustomers
        - product
        - customer
        - tip
    - ProductBreakdown
        - product
        - parent
        - name
        - description
        - cost
