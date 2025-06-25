# ai-hedge-fund flow diagrams

## One analyst
![buffett](warren_buffett_graph.png)

## Multiple analysts
![munger, buffett, and tech analyst](charlie_munger_warren_buffett_technical_analyst_graph.png)

## Main – Preprocessing
![Preprocessing](preprocessing.png)

## run_hedge_fund
![run hedge fund](run_hedge_fund.png)

## Warren Buffett Agent
    for each ticker,
        // Note: at each one of these steps, the agent's progress changes accordingly
        get financial_metrics
        get line items (capital expenditure, net_income, etc)
        get market_cap
        make fundamental_analysis
        make consistency_analysis
        make moat_analysis
        make pricing_power_analysis
        make book_value_analysis
        make mgmt_analysis
        make intrinsic_value_analysis
        total_score = sum of each analysis's "score"
        get max_possible_score
        if intrinsic_value and market_cap,
            margin_of_safety = (intrinsic_value - market_cap) / market_cap
        else margin_of_safety = none
        fill analysis_data with the above
        buffett_analysis[ticker] = generate_buffett_output(ticker, analysis_data)
    create message from buffett_analysis
    show_agent_reasoning if requested
    add buffett's signals to the current state
    return the message and data from the current state

### Analysis functions
Each analysis function follows a similar structure: calculate metrics numerically (according to some formula/inequality/etc) and add a text label to each calculation (eg, strong/weak metric), which is added to a ``reasoning: str`` list, while the total score is kept in a ``score`` variable. Return both ``score`` and ``''.join(reasoning)``

### generate_buffett_output
    prompt = [system prompt, template prompt filled with ticker and analysis_data] # Note: the template prompt includes expected output in JSON format with "signal," "confidence," and "reasoning"
    create a default_signal
    return call_llm(prompt, default_signal, pydantic_model=WarrenBuffettSignal, agent_name="warren_buffett_agent", state=state) # the last 3 arguments are not dependent on this function

## Risk Analysis Agent
The risk analysis agent performs strictly numerical calculations

## Portfolio Manager Agent
    get portfolio, analyst signals, and tickers from the state
    position_limits = {}
    current_prices = {}
    max_shares = {}
    signals_by_ticker = {}
    for each ticker,
        get risk_data from risk_management_agent
        position_limits[ticker] = position limit from risk_data
        current_prices[ticker] = current price from risk_data
        max_shares[ticker] = max(0, int(position_limits[ticker] / current_prices[ticker]))
        ticker_signals = {}
        for each agent & their signal,
            if agent != risk_management_agent and agent has a signal,
                add the signal & confidence to ticker_signals[ticker]
        signals_by_ticker[ticker] = ticker_signals
    generate_trading_decision(tickers, signals_by_ticker, current_prices, max_shares, portfolio, state)
    Turn the decision to a HumanMessage
    show reasoning if requested
    return all messages from state with message and data from state

### generate_trading_decision
    make a prompt with system prompt and template that includes JSON-formatted ouput
    fill the template with signals_by_ticker, current_prices, max_shares, portfolio_cash, portfolio_positions, margin_requirements, total_margin_used
    create default_output
    call_llm(prompt, default_output,pydantic_model=PortfolioManagerOutput, agent_name="portfolio_manager", state=state)
