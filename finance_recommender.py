def recommend_portfolio():
    print("💰 AI Investment Portfolio Recommender")
    print("Select your risk level:")
    print("1. Low Risk")
    print("2. Medium Risk")
    print("3. High Risk")

    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        print("\n📊 Recommended Portfolio (Low Risk):")
        print("• 60% Government Bonds")
        print("• 25% Blue-chip Stocks")
        print("• 10% Gold")
        print("• 5% Cash")
    
    elif choice == "2":
        print("\n📊 Recommended Portfolio (Medium Risk):")
        print("• 40% Index Funds")
        print("• 40% Growth Stocks")
        print("• 10% Bonds")
        print("• 10% Gold")
    
    elif choice == "3":
        print("\n📊 Recommended Portfolio (High Risk):")
        print("• 60% Growth Stocks")
        print("• 20% International Stocks")
        print("• 10% Crypto")
        print("• 10% Start-up Investments")
    
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

recommend_portfolio()