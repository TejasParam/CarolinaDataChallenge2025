# Space Economy Investment Advisor

A comprehensive AI-powered investment analysis platform that combines 12 years of Bureau of Economic Analysis space economy data with conversational artificial intelligence to provide evidence-based investment insights.

## Overview

This project analyzes historical space economy performance patterns, COVID-19 resilience scores, growth trajectories, and forecast predictability across space industry sectors to generate investment recommendations. The system features both a conversational AI chatbot interface and an interactive data visualization dashboard.

## Features

### Core Analysis Capabilities
- **Investment Scoring System**: Multi-dimensional analysis combining growth, resilience, and predictability metrics
- **COVID-19 Resilience Analysis**: Identifies sectors that survived the 2020 pandemic shock
- **Growth Trend Analysis**: 12-year historical performance evaluation
- **Forecast Backtesting**: MAPE (Mean Absolute Percentage Error) analysis for predictability assessment
- **Real-time Data Processing**: Live analysis execution using integrated R scripts

### User Interfaces
- **Streamlit Chatbot**: Conversational AI interface powered by local LLM (Ollama)
- **Interactive Dashboard**: HTML-based visualization platform with Plotly.js charts
- **Professional UI**: Space-themed interface suitable for business presentations

### Technical Features
- **Local LLM Integration**: Privacy-preserving AI using Ollama with Llama 3.2
- **Multi-language Architecture**: Python web interface with R statistical engine
- **Government Data Integration**: Direct processing of BEA space economy datasets
- **Real-time Analysis**: On-demand execution of statistical models

## Technology Stack

### Programming Languages
- **Python**: Main application framework and web interface
- **R**: Statistical analysis and data processing
- **JavaScript**: Interactive visualizations and dashboard functionality
- **HTML/CSS**: Web interface styling and animations

### Frameworks and Libraries
- **Streamlit**: Web application framework for chatbot interface
- **Ollama**: Local LLM infrastructure for conversational AI
- **Plotly.js**: Interactive data visualization library
- **Pandas**: Data manipulation and analysis
- **Requests**: HTTP client for API communication

### AI and Machine Learning
- **Llama 3.2:3b**: Primary language model for conversational responses
- **Custom Statistical Models**: R-based analysis for investment scoring
- **Forecast Validation**: MAPE analysis for predictability assessment

### Data Sources
- **Bureau of Economic Analysis (BEA)**: Official US government space economy data
- **Space Economy Real Value Added Dataset**: 12 years of sector-specific performance

## Installation and Setup

### Prerequisites
- Python 3.8+
- R 4.0+
- Ollama (for local LLM functionality)

### Required Python Packages
```bash
pip install streamlit pandas requests
```

### Required R Packages
Install required R packages for statistical analysis (specific packages depend on your R script).

### Ollama Setup
1. Install Ollama from [https://ollama.ai](https://ollama.ai)
2. Pull the required model:
```bash
ollama pull llama3.2:3b
```
3. Start the Ollama service:
```bash
ollama serve
```

## Usage

### Running the Streamlit Application
```bash
streamlit run space_chatbot.py
```

### Using the System
1. **Start Analysis**: Click "Run Analysis" to execute fresh data analysis
2. **Investment Insights**: Ask for "top investment picks" or use the sidebar buttons
3. **Conversational Queries**: Chat naturally about space economy trends and investments
4. **Dashboard Access**: Open the HTML dashboard for interactive visualizations

### Sample Queries
- "What are the best space investment opportunities?"
- "Which sectors survived COVID-19 best?"
- "Show me growth trends in the space economy"
- "Run fresh analysis for latest data"

## Project Structure

```
CarolinaDataChallenge2025/
├── space_chatbot.py              # Main Streamlit application
├── interactive_analysis_report.html  # Interactive dashboard
├── data_analysis_clean.r         # R statistical analysis script
├── Business.xlsx                 # Input data file
├── analysis_results.txt          # Generated analysis output
└── README.md                     # Project documentation
```

## Key Accomplishments

- **Successfully integrated multiple cutting-edge technologies** - Combined local LLM (Ollama), R statistical analysis, Python web framework (Streamlit), and JavaScript visualizations into a seamless investment advisory platform that processes 12 years of real government data.

- **Built a comprehensive dual-platform solution** - Created both an intelligent conversational chatbot interface and an interactive HTML dashboard with Plotly.js visualizations, demonstrating versatility in delivering complex economic insights through multiple user-friendly interfaces.

- **Developed a novel resilience-based investment framework** - Used the 2020 pandemic as a natural experiment to identify which space economy sectors actually survived crisis conditions, creating an evidence-based approach to investment risk assessment that goes beyond traditional financial metrics.

## Challenges Faced

Integrating multiple technologies (local LLMs, R analytics, Python web frameworks, and JavaScript visualizations) required careful architecture planning to ensure seamless data flow and error handling across different systems. The project taught us that real government economic data often needs extensive preprocessing and parsing to extract meaningful insights, and that creating user-friendly interfaces for complex analytical tools significantly improves accessibility and adoption. Most importantly, we learned that combining conversational AI with traditional data analysis creates a powerful hybrid approach that makes sophisticated economic research accessible to non-technical users through natural language interactions.

## What We Learned

We discovered that integrating multiple technologies requires careful architecture planning to ensure seamless data flow and error handling across different systems. The project demonstrated that real government economic data often needs extensive preprocessing and parsing to extract meaningful insights, and that creating user-friendly interfaces for complex analytical tools significantly improves accessibility and adoption. Most importantly, we learned that combining conversational AI with traditional data analysis creates a powerful hybrid approach that makes sophisticated economic research accessible to non-technical users through natural language interactions.

## What's Next

- **Expand our resilience-testing methodology to other emerging industries** - Apply our COVID-19 shock analysis framework to sectors like renewable energy, biotechnology, and quantum computing to identify which emerging markets can withstand future economic disruptions and provide stable investment opportunities.

- **Develop sector-specific investment timing models** - Use our 12-year BEA analysis experience to create predictive models that can identify optimal entry and exit points for space economy investments, helping investors understand not just what to invest in but when to make those investments for maximum returns.

- **Create an investor education platform** - Leverage our success in making complex government economic data accessible through conversational AI to build educational resources that teach retail investors how to analyze economic resilience patterns, interpret government datasets, and make evidence-based investment decisions rather than following market hype.

## Data Analysis Methodology

### Investment Scoring Framework
1. **Growth Score**: 12-year compound annual growth rate analysis
2. **Resilience Score**: Performance during 2020 pandemic shock
3. **Predictability Score**: MAPE analysis from forecast backtesting
4. **Overall Score**: Weighted combination of all metrics

### Resilience Analysis
- Measures actual performance drop during 2020 pandemic
- Identifies sectors that maintained stability during crisis
- Correlates essential service designation with performance resilience

### Forecast Validation
- MAPE calculation for sector predictability assessment
- Historical backtesting to validate model accuracy
- Identification of most/least predictable investment sectors

## Contributing

This project was developed for the Carolina Data Challenge 2025. For questions or contributions, please refer to the project repository.

## License

This project is developed for educational and research purposes as part of the Carolina Data Challenge 2025.

## Acknowledgments

- Bureau of Economic Analysis for providing comprehensive space economy datasets
- Carolina Data Challenge organizers for the opportunity to work with real government data
- Ollama team for local LLM infrastructure
- Streamlit team for the web application framework