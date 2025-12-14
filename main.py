from agents.manager import manager_agent
from agents.hotel import hotel_agent
from agents.restaurant import restaurant_agent
from agents.activity import activity_agent
from agents.auditor import auditor_agent

def main():
    # --- SCENARIO: A tricky low budget request ---
    user_request = "I want a 2 days weekend in Timisoara. I have a low budget of 200$ total."
    print(f"📢 User Request: {user_request}")

    # --- STEP 1: Manager Works ---
    plan = manager_agent.work(user_request)
    print("\n--- 📋 Manager's Plan ---")
    print(plan)

    # --- STEP 2: The Specialists Work ---
    print("\n... Specialists are working ...")
    
    hotel_input = f"The plan is: {plan}. Find cheap hotels."
    hotels = hotel_agent.work(hotel_input)

    restaurant_input = f"The plan is: {plan}. Find cheap food."
    restaurants = restaurant_agent.work(restaurant_input)

    activity_input = f"The plan is: {plan}. Find cheap activities."
    activities = activity_agent.work(activity_input)

    # --- STEP 3: The Auditor Checks the Math ---
    print("\n... Auditor is calculating ...")
    
    # We combine all previous information into one big report for the Auditor
    auditor_input = f"""
    Here is the trip data:
    
    1. MANAGER'S PLAN (Includes Budget): 
    {plan}
    
    2. HOTEL COSTS: 
    {hotels}
    
    3. FOOD COSTS: 
    {restaurants}
    
    4. ACTIVITY COSTS: 
    {activities}
    
    Please calculate the total and give your verdict.
    """
    
    verdict = auditor_agent.work(auditor_input)
    
    # --- STEP 4: Final Output ---
    print("\n" + "="*30)
    print("      FINAL AUDIT REPORT")
    print("="*30)
    print(verdict)
    
    # Optional: Visual check of the suggestions
    print("\n(Context for user:)")
    print(f"Hotels: {hotels}")
    print(f"Food: {restaurants}")

if __name__ == "__main__":
    main()