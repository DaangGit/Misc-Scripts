# Misc-Scripts
> Repo of miscellaneous Python scripts.
> I also sometimes use this readme file as an online notepad.
> Please ignore everything under this.
---

```
import streamlit as st


def create_question(question, alt_question=None, options=None, input_type='text'):
    st.markdown(f"<h6 style='margin-bottom: -3em;'>{question}</h6>", unsafe_allow_html=True)
    if options is None:
        if input_type == 'text':
            answer = st.text_input('', key=f'{question}')
        elif input_type == 'number':
            answer = st.number_input('', key=f'{question}')
        elif input_type == 'yesno':
            answer = st.radio('', ['Yes', 'No'], key=f'{question}')
       
    else:
        
        if input_type == 'multiple':
            answer = st.multiselect('', options, key=f'{question}')
        else:
            answer = st.selectbox('', options, key=f'{question}')
    return answer



# Title of the questionnaire
st.title('Questionnaire - Section A')

st.markdown("___")
st.markdown(f"<center><h4>Client Information</h4></center>", unsafe_allow_html=True)

col1,col2 = st.columns(2)

# Questions
with col1:
    name = create_question('Name')
    age = create_question('Age', input_type='number')
    gender = create_question('Gender', options=['Male', 'Female', 'Other'])
    marital_status = create_question('Marital Status', options=['Single', 'Married', 'Divorced', 'Widowed'])
    
    
with col2:
    occupation = create_question('Occupation')
    income_options = ['$500,000', '$500,000 - $5,000,000', '$5,000,000 - $10,000,000', '>$10,000,000']
    annual_income = create_question('Annual Income', options=income_options)
    retirement_age = create_question('Target Retirement Age', input_type='number')
    dependents = create_question('No. of dependent family members', input_type='number')

st.markdown("___")
st.markdown(f"<center><h4>Investment Objectives</h4></center>", unsafe_allow_html=True)

col3,col4 = st.columns(2)

# Questions
with col3:
    investment_objective_options = [
        'Capital preservation (saving, i.e., preserving capital and avoiding loss of value)',
        'Income generation (constant income in the form of dividends, bond yields, and interest payments)',
        'Long-term growth (do not seek income, capital appreciation)',
        'Growth with Income (seek current income but also seek income and capital growth over time)'
    ]
    investment_objective = create_question('What are your primary investment objective? (Choose one)', options=investment_objective_options)

    # st.markdown(f"<h2>Time Horizon</h2>", unsafe_allow_html=True)
    time_horizon_options = ['Short-term (0-3 years)', 'Medium-term (3-10 years)', 'Long-term (10+ years)']
    investment_time_horizon = create_question('What is your investment time horizon? (Choose one)', options=time_horizon_options)

with col4:
    short_term_goals_options = [
        'Retirement savings', 'Education funding', 'Wealth transfer', 'Home Purchase/Upgrade/Repairs',
        'Vehicle Purchase', 'Special occasions (like weddings)', 'Philanthropy and charitable giving',
        'Vacation', 'Debt Elimination', 'Other (please specify)'
    ]
    short_term_goals = create_question('Do you have any financial goals below in the short-term? (select all that apply)', options=short_term_goals_options, input_type='multiple')

    long_term_goals_options = [
        'Retirement savings', 'Education funding', 'Wealth transfer', 'Home Purchase', 'Vehicle Purchase',
        'Philanthropy and charitable giving', 'Debt Elimination', 'Other (please specify)'
    ]
    long_term_goals = create_question('Do you have any financial goals below in the long-term? (select all that apply)', options=long_term_goals_options, input_type='multiple')


st.markdown("___")
st.markdown(f"<center><h4>Liquidity Needs</h4></center>", unsafe_allow_html=True)

col5,col6 = st.columns(2)

# Questions
with col5:
    liquidity_needs = create_question('Do you have any liquidity requirements or emergency funds to be considered?', input_type='yesno')

if liquidity_needs == 'Yes':
    with col6:
        annual_withdrawal_options = ['< 2%', '2% - 6%', '> 6%']
        annual_withdrawal_percentage = create_question('What % of the account’s value will you need annually?', options=annual_withdrawal_options)

        withdrawal_time_options = ['Immediately', '1 – 3 Years', '3 – 5 Years', '5 – 10 Years', '10 – 15 Years', 'Over 15 Years']
        withdrawal_time_frame = create_question('When do you expect to begin withdrawals from account for your goals?', options=withdrawal_time_options)


st.markdown("___")
st.markdown(f"<center><h4>Other Preferences</h4></center>", unsafe_allow_html=True)

# Questions
international_investments = create_question('Would you consider allocating a portion of your portfolio to international investments', input_type='yesno')

real_estate_investments = create_question('Would you consider allocating a portion of your portfolio to real estate investments?', input_type='yesno')

municipal_bonds = create_question('Would you consider allocating a portion of your portfolio to tax-exempt Municipal bonds?', input_type='yesno')
st.markdown("___")


st.title('Questionnaire - Section B')

st.markdown("___")
# Questions
question_1_options = ['A. Sell all of the investments? You do not intend to take risks.',
                      'B. Sell a portion of your portfolio to cut your losses and reinvest into more secure investment assets?',
                      'C. Hold the investment and sell nothing, expecting performance to improve?',
                      'D. Invest more funds to lower your average investment price?.']
question_1 = create_question('1. Assume you had an initial investment portfolio worth 100,000 dollars. If, due to market conditions, your portfolio fell to 85,000 dollars, would you:', options=question_1_options)

question_2_options = ['A. I am always concerned about possible losses.',
                      'B. I am somewhat concerned about possible losses.',
                      'C. I usually consider possible gains.',
                      'D. I always consider possible gains.']
question_2 = create_question('2. When considering your investments and making investment decisions, do you think about the impact of possible losses or possible gains?', options=question_2_options)

question_3_options = ['A. I am primarily concerned with limiting risk. I am willing to accept lower expected returns in order to limit my chance of loss.',
                      'B. Limiting risk and maximizing return are of equal importance to me. I am willing to accept moderate risk and a moderate chance of loss in order to achieve moderate returns.',
                      'C. I am primarily concerned with maximizing the returns of my investments. I am willing to accept high risk and a high chance of loss in order to maximize my investment return potential.']
question_3 = create_question('3. Which one of the following statements best describes your attitude toward the trade-off between risk and return?', options=question_3_options)

question_4_options = ['A. 100% in Investment A and 0% in Investment B',
                      'B. 80% in Investment A and 20% in Investment B',
                      'C. 50% in Investment A and 50% in Investment B',
                      'D. 20% in Investment A and 80% in Investment B',
                      'E. 0% in Investment A and 100% in Investment B']
question_4 = create_question('4. Consider two different investments:\nInvestment A, which provides an average annual return of 5% with a minimal risk of loss of value\nInvestment B, which provides an average annual return of 10% and a potential loss of 25% or more in any year.\nHow would you divide your investment dollars?', options=question_4_options)
# st.image('image.jpg', caption='', use_column_width=True)
question_5_options = ['A. Portfolio A',
                      'B. Portfolio B',
                      'C. Portfolio C',
                      'D. Portfolio D',
                      'E. Portfolio E']
question_5 = create_question('5. If you could choose only one of the five hypothetical portfolios characterized below, which would you select?', options=question_5_options)
# st.image('image.jpg', caption='', use_column_width=True)
st.markdown("___")


st.title('Questionnaire - Section C')

st.markdown("___")
# Questions for Overconfidence Bias
overconfidence_question_1_options = ['A. Go all-in on a high-risk opportunity.',
                                      'B. Reevaluate your strategy and consider potential risks.',
                                      'C. Diversify your portfolio to manage risk.']
overconfidence_question_1 = create_question("You've consistently outperformed the market for the past six months. What is your inclination for the next investment decision?", options=overconfidence_question_1_options)

overconfidence_question_2_options = ['A. Invest a significant portion of your portfolio in that stock.',
                                      'B. Reassess your analysis and consider alternative viewpoints.',
                                      'C. Seek advice from financial experts before making a decision.']
overconfidence_question_2 = create_question('Your recent analysis indicates a stock is undervalued. What action are you most likely to take?', options=overconfidence_question_2_options)

overconfidence_question_3_options = ['A. Take bold investment actions without seeking additional information.',
                                      'B. Remain open to different perspectives and adjust your strategy accordingly.',
                                      'C. Actively seek out diverse opinions to challenge your own views.']
overconfidence_question_3 = create_question('You believe you have a better understanding of the market than most investors. How does this belief influence your investment decisions?', options=overconfidence_question_3_options)

st.markdown("___")
# Questions for Loss Aversion Bias
loss_aversion_question_1_options = ['A. Sell investments to avoid further losses.',
                                     'B. Hold onto your investments and wait for the market to recover.',
                                     'C. Increase your investments to take advantage of lower prices.']
loss_aversion_question_1 = create_question('Your portfolio has decreased in value by 20% due to a market downturn. What is your immediate response?', options=loss_aversion_question_1_options)

loss_aversion_question_2_options = ['A. Become more risk-averse and avoid high-risk opportunities.',
                                     'B. Analyze each opportunity individually and assess potential risks and rewards.',
                                     'C. Take more risks to recover losses quickly.']
loss_aversion_question_2 = create_question('After a series of unsuccessful investments, what is your approach to future investment decisions?', options=loss_aversion_question_2_options)

loss_aversion_question_3_options = ['A. Opt for the risky option with the potential for substantial gain.',
                                     'B. Choose the option with the guaranteed small gain to avoid potential losses.',
                                     'C. Weigh the options carefully before making a decision.']
loss_aversion_question_3 = create_question('You are presented with two investment options: one with a 50% chance of a substantial gain and a 50% chance of a moderate loss, and the other with a guaranteed small gain. What would you be more inclined to choose?', options=loss_aversion_question_3_options)

st.markdown("___")
# Questions for Confirmation Bias
confirmation_bias_question_1_options = ['A. Rely solely on your preferred source for investment decisions.',
                                         'B. Occasionally check alternative sources to validate your views.',
                                         'C. Regularly seek out diverse perspectives from various sources.']
confirmation_bias_question_1 = create_question('Your preferred financial news source consistently supports your investment choices. How does this influence your information-seeking behavior?', options=confirmation_bias_question_1_options)

confirmation_bias_question_2_options = ['A. Dismiss the contradictory research and stick to your original thesis.',
                                         'B. Reevaluate your thesis and consider the new information.',
                                         'C. Seek additional information to confirm the validity of both perspectives.']
confirmation_bias_question_2 = create_question('You come across research that contradicts your current investment thesis. What is your response?', options=confirmation_bias_question_2_options)

confirmation_bias_question_3_options = ['A. Disregard the suggestion, as it goes against your existing beliefs.',
                                         'B. Consider the suggestion and evaluate its merits objectively.',
                                         'C. Follow your friend\'s suggestion without conducting additional research.']
confirmation_bias_question_3 = create_question('Your friend suggests an investment that contradicts your current strategy. How do you approach this suggestion?', options=confirmation_bias_question_3_options)

st.markdown("___")
# Questions for Gambler’s Fallacy
gamblers_fallacy_question_1_options = ['A. Expect a price decrease since the stock has been rising recently.',
                                        'B. Anticipate a random movement.',
                                        'C. Expect another increase to continue the positive trend.']
gamblers_fallacy_question_1 = create_question('A stock you own has experienced a series of consecutive price increases. What is your expectation for the next day\'s stock price movement?', options=gamblers_fallacy_question_1_options)

gamblers_fallacy_question_2_options = ['A. Choose different numbers.',
                                        'B. Stick with the same numbers.',
                                        'C. Avoid playing, as the repeated pattern seems suspicious.']
gamblers_fallacy_question_2 = create_question('In a lottery, the numbers 1, 2, 3, 4, 5, and 6 have been drawn for three consecutive weeks. What is your expectation for the next draw?', options=gamblers_fallacy_question_2_options)

gamblers_fallacy_question_3_options = ['A. Bet on black.',
                                        'B. Place a bet on red.',
                                        'C. Avoid betting, as the pattern suggests the wheel may be rigged.']
gamblers_fallacy_question_3 = create_question('You observe a roulette wheel in a casino, and it lands on red for the past seven spins. What is your expectation for the next spin?', options=gamblers_fallacy_question_3_options)

st.markdown("___")
# Questions for Status Quo Bias
status_quo_bias_question_1_options = ['A. Stick to your current strategy, as it has worked well for you so far.',
                                       'B. Research and assess the new strategy thoroughly before considering a change.',
                                       'C. Adopt the new strategy to capitalize on its recent success.']
status_quo_bias_question_1 = create_question('You come across a new investment strategy that has shown promising results for other investors. What would be your response?', options=status_quo_bias_question_1_options)

status_quo_bias_question_2_options = ['A. Hold onto the stock, expecting a potential rebound in the future.',
                                       'B. Sell the underperforming stock to cut losses and explore new opportunities.',
                                       'C. Avoid selling, as the stock has been a reliable long-term investment.']

status_quo_bias_question_2 = create_question('One of your long-term holdings has underperformed for the past year. What would be your decision?', options=status_quo_bias_question_2_options)

status_quo_bias_question_3_options = ['A. Resist rebalancing, as the current allocation has been successful.',
                                       'B. Monitor the portfolio but refrain from making any changes unless necessary.',
                                       'C. Rebalance the portfolio to maintain the initial allocation.']
status_quo_bias_question_3 = create_question('Your investment portfolio has performed well, and it currently aligns with your original asset allocation. What would be your inclination?', options=status_quo_bias_question_3_options)

st.markdown("___")
# Questions for Endowment Bias
endowment_bias_question_1_options = ['A. Avoid making any changes to the inherited portfolio.',
                                      'B. Evaluate the inherited portfolio and make changes if needed.',
                                      'C. Hold onto the inherited stocks as a form of family legacy, but be open for evaluation']
endowment_bias_question_1 = create_question('You inherit a portfolio of stocks from a family member. How would this inheritance affect your decision-making regarding the inherited stocks?', options=endowment_bias_question_1_options)

endowment_bias_question_2_options = ['A. Invest more in the property, expecting improved returns.',
                                      'B. Hold onto the property, valuing its sentimental significance.',
                                      'C. Consider selling the property if it aligns with your financial goals.']
endowment_bias_question_2 = create_question('You own a property that has sentimental value but is not performing well as an investment. What would you be more likely to do?', options=endowment_bias_question_2_options)

endowment_bias_question_3_options = ['A. Consider investing more in similar items, expecting a future increase in value.',
                                      'B. Hold onto the collectibles, valuing their sentimental and historical significance.',
                                      'C. Evaluate the current market conditions and sell if it makes financial sense.']
endowment_bias_question_3 = create_question('You have a collection of rare items that you\'ve accumulated over the years. The market for these items has been declining. What would be your decision?', options=endowment_bias_question_3_options)
st.markdown("___")
```
