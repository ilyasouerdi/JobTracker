from services import *


def main():
    load_data()

    while True:
        print("\n=== Job Application Tracker ===")
        print("1. User Management")
        print("2. Company Management")
        print("3. Application Management")
        print("4. Generate Statistics")
        print("5. Export Data to CSV")
        print("6. Save Data")
        print("7. Exit")

        choice = input("Enter your choice: ")

        # User Management
        if choice == "1":
            print("\n=== User Management ===")
            print("1. Add User")
            print("2. View Users")

            user_choice = input("Enter your choice: ")

            if user_choice == "1":
                name = input("Enter user name: ")
                email = input("Enter user email: ")
                password = input("Enter user password: ")

                user = create_user(name, email, password)

                if user:
                    print("User created successfully.")
                else:
                    print("Failed to create user.")

            elif user_choice == "2":
                for user in list_users():
                    print(user.to_dict())

            else:
                print("Invalid choice.")

        # Company Management
        elif choice == "2":
            print("\n=== Company Management ===")
            print("1. Add Company")
            print("2. View Companies")

            company_choice = input("Enter your choice: ")

            if company_choice == "1":
                name = input("Enter company name: ")
                website = input("Enter company website: ")
                location = input("Enter company location: ")
                industry = input("Enter company industry: ")

                company = create_company(
                    name,
                    website,
                    location,
                    industry
                )

                if company:
                    print("Company created successfully.")
                else:
                    print("Failed to create company.")

            elif company_choice == "2":
                for company in list_companies():
                    print(company.to_dict())

            else:
                print("Invalid choice.")

        # Application Management
        elif choice == "3":
            print("\n=== Application Management ===")
            print("1. Add Application")
            print("2. View Applications")
            print("3. Find Application By ID")

            application_choice = input("Enter your choice: ")

            if application_choice == "1":
                user_id = int(input("Enter user ID: "))
                company_id = int(input("Enter company ID: "))
                position = input("Enter position: ")
                salary_expected = float(
                    input("Enter expected salary: ")
                )
                note = input("Enter note: ")

                application = apply_to_company(
                    user_id,
                    company_id,
                    position,
                    salary_expected,
                    note
                )

                if application:
                    print("Application created successfully.")
                else:
                    print("Failed to create application.")

            elif application_choice == "2":
                for application in list_applications():
                    print(application.to_dict())

            elif application_choice == "3":
                application_id = int(
                    input("Enter application ID: ")
                )

                application = get_application_by_id(
                    application_id
                )

                if application:
                    print(application.to_dict())
                else:
                    print("Application not found.")

            else:
                print("Invalid choice.")

        # Statistics
        elif choice == "4":
            stats = generate_statistics()

            print("\n=== Statistics ===")
            for key, value in stats.items():
                print(f"{key}: {value}")

        # CSV Export
        elif choice == "5":
            if export_to_csv():
                print("CSV files exported successfully.")
            else:
                print("Export failed.")

        # Save Data
        elif choice == "6":
            if save_data():
                print("Data saved successfully.")
            else:
                print("Save failed.")

        # Exit
        elif choice == "7":
            save_data()
            print("Data saved. Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()