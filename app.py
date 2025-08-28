import random
import pandas as pd

# Dummy data which is provided by my end.
dummy_leads = [
    {"name": "Om Prakash Sinha", "business": "Retail Assests", "email": "omprakashsinha9155@gmail.com", "location": "India", "size": "medium"},
    {"name": "Jay Prakash Sinha", "business": "NGO", "email": "jayprakashsinha11@gmail.com", "location": "Delhi NCR", "size": "large"},
    {"name": "Aakash Pathak", "business": "VR World", "email": "vrworld@gmail.com", "location": "East Delhi", "size": "small"},
    {"name": "Satya Singh Rajput", "business": "Family Fun Hub", "email": "familyfunhub@gmail.com", "location": "Mumbai", "size": "medium"},
    {"name": "Sujeet Shreebastaw", "business": "Gaming World", "email": "gamingworld@gmail.com", "location": "South Delhi", "size": "large"}
]

def generate_leads(num=5):
    """AI simulates lead generation from web searches."""
    return dummy_leads[:num]

def qualify_leads(leads):
    """AI scores leads (simple rule-based; real AI would use ML)."""
    for lead in leads:
        size_score = {'small': 60, 'medium': 80, 'large': 100}
        lead['score'] = size_score.get(lead['size'], 50) + random.randint(-10, 10)
    return sorted(leads, key=lambda x: x['score'], reverse=True)

def draft_outreach(lead):
    """AI drafts personalized email (template-based; real AI uses LLM)."""
    return f"""Subject: Enhance Your FEC with Cutting-Edge Arcade/VR Products

Dear {lead['name']},

We've identified your {lead['business']} in {lead['location']} as a perfect fit for our innovative arcade and VR solutions that can elevate visitor experiences and increase revenue.

Are you available for a 15-minute call to discuss how we can tailor our products to your needs?

Best regards,
Senior HR
Bamigoes VR LLP"""

def simulate_response():
    """Simulate prospect response (random; real system parses emails)."""
    responses = ["Interested, let's schedule.", "Not interested.", "More info please."]
    return random.choice(responses)

def main():
    print("Sales & Marketing System powered by AI\n")
    
    # Step 1: Lead Generation
    print("1. Generating Leads...")
    leads = generate_leads()
    print(f"Generated {len(leads)} leads.\n")
    
    # Step 2: Lead Qualification
    print("2. Qualifying Leads...")
    qualified_leads = qualify_leads(leads)
    df = pd.DataFrame(qualified_leads)
    print(df[['name', 'business', 'score']])
    print("\n")
    
    # Process top leads (demo: first 2)
    for lead in qualified_leads[:2]:
        print(f"Processing lead: {lead['name']} ({lead['business']}) - Score: {lead['score']}\n")
        
        # Step 3: Draft Outreach
        draft = draft_outreach(lead)
        print("AI Drafted Outreach:\n")
        print(draft)
        
        # Step 4: Human Review
        action = input("Human Review: (a)pprove, (e)dit, (s)kip: ").lower()
        if action == 'e':
            print("Enter edited email body (keep subject):")
            edited_body = input()
            draft = draft.split('\n', 1)[0] + '\n' + edited_body
        elif action == 's':
            continue
        
        # Step 5: Simulate Send and Response
        print("\nSimulating Sending Outreach...\n")
        response = simulate_response()
        print(f"Received response: {response}\n")
        
        # Step 6: Handle Response
        if "interested" in response.lower():
            print("AI Detects Interest. Proposing Schedule...")
            # Step 7: Scheduling
            schedule = input("Human input: Enter meeting time (e.g., Sept 1, 2pm): ")
            print(f"Meeting Scheduled for {schedule}.\n")
        elif "more info" in response.lower():
            print("AI Drafting Follow-up With More Info...\n")
            # Simulate follow-up
            print("Follow-up Drafted: [AI-generated Details on products]. Human approve/send.")
        else:
            print("No Interest. Archiving lead.\n")
    
    print("Demo Complete. In Production, Loop Back to CRM Analytics.")

if __name__ == "__main__":
    main()