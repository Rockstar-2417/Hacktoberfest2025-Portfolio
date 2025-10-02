# Simple Logic Verifier CLI
# Can check basic math/logical statements like "2 + 3 = 5" or "5 > 2"

def verify_statement(statement):
    try:
        # Evaluate the statement safely
        result = eval(statement)
        if result:
            return True
        else:
            return False
    except:
        return None

def main():
    print("Logic Verifier ✅ CLI Tool")
    print("Enter logical/mathematical statements (e.g., 2+3==5, 4>2)")
    print("Type 'exit' to quit.\n")
    while True:
        stmt = input("Enter statement: ")
        if stmt.lower() == 'exit':
            print("Exiting Logic Verifier.")
            break
        result = verify_statement(stmt)
        if result is True:
            print("✅ Correct!")
        elif result is False:
            print("❌ Incorrect!")
        else:
            print("⚠️ Invalid statement")

if __name__ == "__main__":
    main()
