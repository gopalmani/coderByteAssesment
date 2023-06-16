Task - Add a staff into the system & fee collection

    Login to the application
        Description: Ensure the user can successfully log in to the application using the provided credentials.
        Precondition: None
        Steps:
            Open the application URL.
            Enter the username and password.
            Click the login button.
        Expected Result: User should be logged in and land on the Dashboard.

    Add a staff member
        Description: Verify that a new staff member can be added to the system.
        Precondition: User is logged in and on the Dashboard.
        Steps:
            Go to the 'Staff Profile Management' menu.
            Open the 'Staff Add' page.
            Fill in all mandatory fields in the 'Personal Details' section.
            Click the 'Save' button.
        Expected Result: A new staff member should be successfully added to the system.

    Navigate to Fee Collection
        Description: Ensure the user can navigate to the Fee Collection section.
        Precondition: User is logged in and on the Dashboard.
        Steps:
            Go to the 'Fee Configuration' menu.
            Navigate to the 'Fee Collection' page.
        Expected Result: User should land on the 'Fee Collection' page.

    Search for a student
        Description: Verify that a student can be searched using the 'Global Student Search' feature.
        Precondition: User is on the 'Fee Collection' page.
        Steps:
            Enter '200011312' into the 'Global Student Search' box.
            Perform the search.
        Expected Result: The student with the provided ID should be displayed.

    Select and pay a pending invoice
        Description: Ensure that a pending invoice can be selected and payment can be made.
        Precondition: User is on the 'Fee Collection' page and a pending invoice is available.
        Steps:
            Select a pending invoice from the 'Payable' -> 'Pending Invoice' section.
            Choose the payment mode from the 'Payments' section.
            Click the 'Pay' button.
        Expected Result: The payment should be processed successfully.

    Verify successful payment
        Description: Confirm that the payment has been completed successfully.
        Precondition: User has made a payment.
        Steps: None
        Expected Result: Payment should be completed successfully, and the system should reflect the updated payment status.