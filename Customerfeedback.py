# Initialize an empty list to store feedback data
feedback_data = []

while True:
    print("\nCustomer Feedback System")
    print("1. Submit Feedback")
    print("2. View Feedback")
    print("3. Analyze Feedback")
    print("4. Exit")
    
    # Get user's choice
    choice = input("Enter your choice: ")
    
    # Submit feedback
    if choice == '1':
        print("Please provide your feedback.")
        rating = int(input("Enter your rating (1-5): "))
        
        # Validate the rating
        if rating < 1 or rating > 5:
            print("Invalid rating. Rating should be between 1 and 5.")
        else:
            comments = input("Enter your comments: ")
            feedback_data.append({'rating': rating, 'comments': comments})
            print("Thank you for your feedback!")

    # View feedback
    elif choice == '2':
        if not feedback_data:
            print("No feedback available.")
        else:
            print("\nAll feedback received:")
            for idx, feedback in enumerate(feedback_data, 1):
                print(f"Feedback {idx}: Rating - {feedback['rating']}, Comments - {feedback['comments']}")

    # Analyze feedback (average rating)
    elif choice == '3':
        if not feedback_data:
            print("No feedback available for analysis.")
        else:
            total_rating = 0
            for feedback in feedback_data:
                total_rating += feedback['rating']
            average_rating = total_rating / len(feedback_data)
            print(f"\nAverage rating: {average_rating:.2f}")

    # Exit the program
    elif choice == '4':
        print("Exiting the program.")
        break
    
    else:
        print("Invalid choice. Please try again.")
