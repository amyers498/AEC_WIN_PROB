import streamlit as st
import csv

# Define industry probabilities (adjust as needed)
industry_probabilities = {
    'Aviation': 0.25,
    'Transportation': 0.2,
    'Federal': 0.15,
    'Healthcare': 0.1,
    'Defense': 0.1,
    'Energy': 0.1,
    'Corporate': 0.1
}

# Define competitor companies
competitor_companies = [
    'Company A',
    'Company B',
    'Company C',
    'Company D',
    'Company E',
    'Company F',
    'Company G',
    'Company H',
    'Company I',
    'Company J'
]
# Define state adjustments
state_adjustments = {
    'Alabama': 0.02,
    'Alaska': -0.03,
    'Arizona': 0.04,
    'Arkansas': -0.02,
    'California': 0.1,
    'Colorado': -0.04,
    'Connecticut': 0.03,
    'Delaware': -0.01,
    'Florida': 0.02,
    'Georgia': -0.03,
    'Hawaii': 0.04,
    'Idaho': -0.02,
    'Illinois': 0.03,
    'Indiana': -0.01,
    'Iowa': 0.02,
    'Kansas': -0.03,
    'Kentucky': 0.04,
    'Louisiana': -0.02,
    'Maine': 0.03,
    'Maryland': -0.01,
    'Massachusetts': 0.02,
    'Michigan': -0.03,
    'Minnesota': 0.04,
    'Mississippi': -0.02,
    'Missouri': 0.03,
    'Montana': -0.01,
    'Nebraska': 0.02,
    'Nevada': -0.03,
    'New Hampshire': 0.04,
    'New Jersey': -0.02,
    'New Mexico': 0.03,
    'New York': -0.05,
    'North Carolina': 0.01,
    'North Dakota': -0.04,
    'Ohio': 0.02,
    'Oklahoma': -0.03,
    'Oregon': 0.04,
    'Pennsylvania': -0.02,
    'Rhode Island': 0.03,
    'South Carolina': -0.01,
    'South Dakota': 0.02,
    'Tennessee': -0.03,
    'Texas': 0.05,
    'Utah': -0.02,
    'Vermont': 0.03,
    'Virginia': -0.01,
    'Washington': 0.02,
    'West Virginia': -0.03,
    'Wisconsin': 0.04,
    'Wyoming': -0.02
}
def calculate_win_probability(input_values, state):
    # Define weights for each category (adjust as needed)
    weights = {
        'Past Performance': 0.2,
        'Team Qualifications': 0.15,
        'Project Fit': 0.15,
        'Competitive Analysis': 0.1,
        'Pricing': 0.1,
        'Client Relationship': 0.1,
        'Technical Expertise': 0.1,
        'Innovation': 0.05,
        'Market Trends': 0.05,
        'Industry Reputation': 0.05,
        'Contract Industry': 0.05,
        'Competitors Involved': 0.05
    }

    # Define scores for each category based on user input values
    scores = {
        'Past Performance': float(input_values['past_performance']),
        'Team Qualifications': float(input_values['team_qualifications']),
        'Project Fit': float(input_values['project_fit']),
        'Competitive Analysis': float(input_values['competitive_analysis']),
        'Pricing': float(input_values['pricing']),
        'Client Relationship': float(input_values['client_relationship']),
        'Technical Expertise': float(input_values['technical_expertise']),
        'Innovation': float(input_values['innovation']),
        'Market Trends': float(input_values['market_trends']),
        'Industry Reputation': float(input_values['industry_reputation']),
        'Contract Industry': float(industry_probabilities[input_values['contract_industry']]),
        'Competitors Involved': float(len(input_values['competitors_involved']))
    }

    # Adjust win probability based on competitors involved
    competitor_adjustments = {
        'Company A': 0.2,
        'Company B': -0.1,
        'Company C': -0.15,
        'Company D': -0.05,
        'Company E': 0.1,
        'Company F': -0.1,
        'Company G': 0.05,
        'Company H': 0.1,
        'Company I': -0.05,
        'Company J': 0.15
    }

    for competitor in input_values['competitors_involved']:
        if competitor in competitor_adjustments:
            scores['Competitors Involved'] += competitor_adjustments[competitor]

    # Calculate weighted score
    weighted_score = sum(scores[category] * weights[category] for category in scores)

    # Normalize the weighted score between 0 and 1
    normalized_score = weighted_score / len(weights)

    # Adjust win probability based on the state
    state_adjustments = {
        'Alabama': 0.02,
        'Alaska': -0.03,
        'Arizona': 0.04,
        'Arkansas': -0.02,
        'California': 0.1,
        'Colorado': -0.04,
        'Connecticut': 0.03,
        'Delaware': -0.01,
        'Florida': 0.02,
        'Georgia': -0.03,
        'Hawaii': 0.04,
        'Idaho': -0.02,
        'Illinois': 0.03,
        'Indiana': -0.01,
        'Iowa': 0.02,
        'Kansas': -0.03,
        'Kentucky': 0.04,
        'Louisiana': -0.02,
        'Maine': 0.03,
        'Maryland': -0.01,
        'Massachusetts': 0.02,
        'Michigan': -0.03,
        'Minnesota': 0.04,
        'Mississippi': -0.02,
        'Missouri': 0.03,
        'Montana': -0.01,
        'Nebraska': 0.02,
        'Nevada': -0.03,
        'New Hampshire': 0.04,
        'New Jersey': -0.02,
        'New Mexico': 0.03,
        'New York': -0.05,
        'North Carolina': 0.01,
        'North Dakota': -0.04,
        'Ohio': 0.02,
        'Oklahoma': -0.03,
        'Oregon': 0.04,
        'Pennsylvania': -0.02,
        'Rhode Island': 0.03,
        'South Carolina': -0.01,
        'South Dakota': 0.02,
        'Tennessee': -0.03,
        'Texas': 0.05,
        'Utah': -0.02,
        'Vermont': 0.03,
        'Virginia': -0.01,
        'Washington': 0.02,
        'West Virginia': -0.03,
        'Wisconsin': 0.04,
        'Wyoming': -0.02
    }

    state_adjustment = state_adjustments.get(state, 0)
    adjusted_score = normalized_score + state_adjustment

    # Calculate win probability (adjust as needed)
    win_probability = adjusted_score * 100

    # Make it more difficult to achieve 100% probability
    win_probability = min(win_probability, 99.99)

    return win_probability

def generate_ai_comment(contract_industry, state):
    with open('dummy.csv', 'r') as file:
        reader = csv.DictReader(file)
        filtered_data = [row for row in reader if row['State'] == state and row['Industry'] == contract_industry]

    if filtered_data:
        average_fee = sum(float(row['Fee']) for row in filtered_data) / len(filtered_data)
        average_square_footage = sum(float(row['Square Footage']) for row in filtered_data) / len(filtered_data)
    else:
        average_fee = 0
        average_square_footage = 0

    comment = f"In {state}, for {contract_industry} projects, our average fee is approximately ${average_fee:,.2f}, and our average square footage is {average_square_footage:.2f} sqft."

    return comment

# Streamlit app code
def main():
    st.set_page_config(page_title='AEC WIN PROB', layout='wide')
    st.title('AEC WIN PROB 1st CONCEPT')

        # Define explanations and criteria for each category
    category_explanations = {
        'Past Performance': 'Evaluation of the company\'s past performance on similar projects. Higher scores indicate a more successful track record.',
        'Team Qualifications': 'Assessment of the qualifications and expertise of the project team. Higher scores indicate stronger qualifications.',
        'Project Fit': 'Compatibility of the company\'s capabilities with the project requirements. Higher scores indicate a better fit.',
        'Competitive Analysis': 'Comparison of the company\'s strengths against competitors. Higher scores indicate a more favorable competitive position.',
        'Pricing': 'Competitiveness of the proposed pricing. Higher scores indicate more competitive pricing.',
        'Client Relationship': 'Quality of the existing relationship with the client. Higher scores indicate a stronger client relationship.',
        'Technical Expertise': 'Depth of technical knowledge and expertise in relevant areas. Higher scores indicate higher expertise.',
        'Innovation': 'Demonstration of innovative ideas or approaches for the project. Higher scores indicate higher levels of innovation.',
        'Market Trends': 'Awareness and understanding of current market trends. Higher scores indicate better awareness of market trends.',
        'Industry Reputation': 'Overall reputation and credibility within the industry. Higher scores indicate a stronger industry reputation.',
        'Contract Industry': 'Industry in which the contract is for. Different industries may have varying probabilities.',
        'Competitors Involved': 'Competitor companies involved in the bidding process. Selection of certain competitors may affect the win probability.'
    }

    # Collect user input values for different categories
    input_values = {}
    for category, explanation in category_explanations.items():
        st.subheader(category)
        st.write(explanation)
        if category == 'Contract Industry':
            input_values['contract_industry'] = st.selectbox(category, list(industry_probabilities.keys()))
        elif category == 'Competitors Involved':
            input_values['competitors_involved'] = st.multiselect(category, competitor_companies)
        else:
            input_values[category.lower().replace(' ', '_')] = st.slider(f'{category} (1-5)', 1, 5, 3)

    # Allow user to enter state with searchable dropdown
    state = st.selectbox('State', list(state_adjustments.keys()))

    # Calculate win probability
    win_probability = calculate_win_probability(input_values, state)

    # Generate AI comment
    ai_comment = generate_ai_comment(input_values['contract_industry'], state)

    # Display results
    st.header('Results')
    st.subheader(f'Win Probability: {win_probability:.2f}%')
    st.header('Databose Bot')
    st.subheader(f'Database Comment: {ai_comment}')
    st.header("NOTES:")
    st.write('Every variable on this page is given a "weight" including the variables such as state which is in direct correlation to industry and competitors. The datatbase bot compiles its information from a fake database of a 1000 points I created using a for loop python script. This is very rough around the edges but with the potential to pull from various data streams could be deemed useful.')
    st.markdown("[Link to the code on my GITHUB ](#https://github.com/amyers498/AEC_WIN_PROB/blob/main/app.py)")
if __name__ == '__main__':
    main()

