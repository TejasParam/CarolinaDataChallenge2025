"""
🚀 Space Economy Investment Advisor Chatbot
Uses BEA space economy data analysis for investment insights
"""

import streamlit as st
import pandas as pd
import json
import re
import subprocess
import os
from datetime import datetime
import time

# Page config
st.set_page_config(
    page_title="🚀 Space Economy Investment Advisor",
    page_icon="🛰️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced space theme CSS with animations
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 25%, #16213e 50%, #0f3460 75%, #000000 100%);
        color: #ffffff;
        font-family: 'Orbitron', monospace;
    }
    
    .main-header {
        background: linear-gradient(90deg, #00bcd4, #2196f3, #9c27b0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: 0 0 30px #00bcd4;
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes glow {
        from { text-shadow: 0 0 20px #00bcd4, 0 0 30px #00bcd4, 0 0 40px #00bcd4; }
        to { text-shadow: 0 0 30px #00bcd4, 0 0 40px #00bcd4, 0 0 50px #00bcd4; }
    }
    
    .stTitle {
        color: #00bcd4 !important;
        font-family: 'Orbitron', monospace !important;
        font-weight: 900 !important;
        text-shadow: 0 0 20px #00bcd4 !important;
    }
    
    .stHeader {
        color: #64b5f6 !important;
        font-family: 'Orbitron', monospace !important;
        font-weight: 700 !important;
    }
    
    .stTextInput > div > div > input {
        background-color: rgba(0, 188, 212, 0.1) !important;
        color: white !important;
        border: 2px solid #00bcd4 !important;
        border-radius: 10px !important;
        font-family: 'Orbitron', monospace !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #2196f3 !important;
        box-shadow: 0 0 15px #00bcd4 !important;
    }
    
    .stButton > button {
        background: linear-gradient(45deg, #1976d2, #00bcd4, #9c27b0) !important;
        border: none !important;
        color: white !important;
        font-weight: bold !important;
        font-family: 'Orbitron', monospace !important;
        border-radius: 25px !important;
        padding: 0.5rem 1.5rem !important;
        transition: all 0.3s ease !important;
        position: relative !important;
        overflow: hidden !important;
    }
    
    .stButton > button:hover {
        background: linear-gradient(45deg, #0d47a1, #006064, #6a1b9a) !important;
        box-shadow: 0 0 25px #00bcd4 !important;
        transform: translateY(-2px) !important;
    }
    
    .stButton > button:before {
        content: '' !important;
        position: absolute !important;
        top: 0 !important;
        left: -100% !important;
        width: 100% !important;
        height: 100% !important;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent) !important;
        transition: left 0.5s !important;
    }
    
    .stButton > button:hover:before {
        left: 100% !important;
    }
    
    .chat-message {
        padding: 1.5rem !important;
        border-radius: 15px !important;
        margin: 1rem 0 !important;
        border-left: 5px solid #00bcd4 !important;
        background: rgba(0, 188, 212, 0.05) !important;
        backdrop-filter: blur(10px) !important;
        box-shadow: 0 8px 32px rgba(0, 188, 212, 0.1) !important;
        animation: slideIn 0.5s ease-out !important;
    }
    
    @keyframes slideIn {
        from { opacity: 0; transform: translateX(-20px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    .user-message {
        background: rgba(0, 188, 212, 0.1) !important;
        border-left-color: #2196f3 !important;
    }
    
    .bot-message {
        background: rgba(100, 181, 246, 0.1) !important;
        border-left-color: #00bcd4 !important;
    }
    
    .sidebar-content {
        background: rgba(0, 0, 0, 0.3) !important;
        border-radius: 15px !important;
        padding: 1rem !important;
        margin: 1rem 0 !important;
        backdrop-filter: blur(10px) !important;
    }
    
    .space-particles {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100% !important;
        height: 100% !important;
        pointer-events: none !important;
        z-index: -1 !important;
    }
    
    .particle {
        position: absolute !important;
        background: white !important;
        border-radius: 50% !important;
        animation: float 6s ease-in-out infinite !important;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); opacity: 0; }
        50% { transform: translateY(-20px) rotate(180deg); opacity: 1; }
    }
    
    .metric-card {
        background: rgba(0, 188, 212, 0.1) !important;
        border: 1px solid #00bcd4 !important;
        border-radius: 10px !important;
        padding: 1rem !important;
        margin: 0.5rem 0 !important;
        text-align: center !important;
    }
    
    .metric-value {
        font-size: 2rem !important;
        font-weight: 900 !important;
        color: #00bcd4 !important;
        font-family: 'Orbitron', monospace !important;
    }
    
    .metric-label {
        font-size: 0.9rem !important;
        color: #64b5f6 !important;
        font-family: 'Orbitron', monospace !important;
    }
</style>
""", unsafe_allow_html=True)

# Add space particles background
st.markdown("""
<div class="space-particles">
    <div class="particle" style="left: 10%; animation-delay: 0s; width: 2px; height: 2px;"></div>
    <div class="particle" style="left: 20%; animation-delay: 1s; width: 1px; height: 1px;"></div>
    <div class="particle" style="left: 30%; animation-delay: 2s; width: 3px; height: 3px;"></div>
    <div class="particle" style="left: 40%; animation-delay: 0.5s; width: 1px; height: 1px;"></div>
    <div class="particle" style="left: 50%; animation-delay: 1.5s; width: 2px; height: 2px;"></div>
    <div class="particle" style="left: 60%; animation-delay: 3s; width: 1px; height: 1px;"></div>
    <div class="particle" style="left: 70%; animation-delay: 0.8s; width: 2px; height: 2px;"></div>
    <div class="particle" style="left: 80%; animation-delay: 2.5s; width: 1px; height: 1px;"></div>
    <div class="particle" style="left: 90%; animation-delay: 1.2s; width: 3px; height: 3px;"></div>
</div>
""", unsafe_allow_html=True)

class SpaceEconomyBot:
    def __init__(self):
        self.analysis_tools = self.setup_analysis_tools()
        self.keywords = {
            'investment': ['invest', 'investment', 'portfolio', 'returns', 'growth', 'profit'],
            'resilience': ['resilient', 'resilience', 'stable', 'shock', 'crisis', 'covid'],
            'growth': ['growth', 'growing', 'expansion', 'trend', 'increase'],
            'industries': ['industry', 'sector', 'companies', 'business'],
            'space': ['space', 'satellite', 'aerospace', 'launch', 'orbital', 'rocket'],
            'defense': ['defense', 'military', 'national security'],
            'manufacturing': ['manufacturing', 'production', 'tech', 'electronics'],
            'forecast': ['predict', 'forecast', 'future', 'outlook', 'projection'],
            'analysis': ['analyze', 'analysis', 'run', 'calculate', 'compute'],
            'data': ['data', 'numbers', 'statistics', 'metrics', 'results']
        }
        
    def setup_analysis_tools(self):
        """Setup available analysis tools from your R script"""
        return {
            'run_full_analysis': {
                'description': 'Run the complete space economy analysis using BEA data',
                'command': 'Rscript data_analysis_clean.r',
                'output_files': ['analysis_results.txt', 'top5_industries_plot.png', 'shock_resilience_plot.png', 'investability_quadrant_plot.png']
            },
            'get_current_results': {
                'description': 'Read existing analysis results',
                'command': None,
                'output_files': ['analysis_results.txt']
            }
        }
    
    def run_analysis_tool(self, tool_name):
        """Execute an analysis tool and return results"""
        tool = self.analysis_tools.get(tool_name)
        if not tool:
            return "Tool not found"
        
        try:
            if tool['command']:
                # Run the R script
                result = subprocess.run(
                    tool['command'].split(),
                    capture_output=True,
                    text=True,
                    timeout=60
                )
                
                if result.returncode != 0:
                    return f"Analysis failed: {result.stderr}"
            
            # Read the results
            return self.read_analysis_results()
            
        except subprocess.TimeoutExpired:
            return "Analysis timed out. Please try again."
        except Exception as e:
            return f"Error running analysis: {str(e)}"
    
    def read_analysis_results(self):
        """Read and parse the analysis results file"""
        try:
            if os.path.exists('analysis_results.txt'):
                with open('analysis_results.txt', 'r') as f:
                    content = f.read()
                return self.parse_analysis_results(content)
            else:
                return "No analysis results found. Please run the analysis first."
        except Exception as e:
            return f"Error reading results: {str(e)}"
    
    def parse_analysis_results(self, content):
        """Parse the analysis results into structured data with fixed logic"""
        results = {
            'top_investments': [],
            'resilient_sectors': [],
            'forecast_results': {},
            'pitch_table': []
        }
        
        # Extract top 10 overall score table
        if "=== TOP 10 BY OVERALL SCORE ===" in content:
            # Find the start and end of the section
            start_marker = "=== TOP 10 BY OVERALL SCORE ==="
            end_marker = "=== MOST RESILIENT TO 2020 SHOCK ==="
            
            start_idx = content.find(start_marker)
            end_idx = content.find(end_marker)
            
            if start_idx != -1 and end_idx != -1:
                section = content[start_idx:end_idx]
                lines = section.split('\n')
                
                for line in lines:
                    if '|' in line and not line.startswith('|:') and not 'Overall Score' in line and not 'Industry' in line:
                        parts = [part.strip() for part in line.split('|') if part.strip()]
                        if len(parts) >= 5:
                            try:
                                industry = parts[0]
                                if industry and industry not in ['Industry', '']:
                                    overall_score = parts[1]
                                    invest_score = parts[2] 
                                    growth_score = parts[3]
                                    resilience_score = parts[4]
                                    
                                    results['top_investments'].append({
                                        'industry': industry,
                                        'overall_score': overall_score,
                                        'investability': invest_score,
                                        'growth': growth_score,
                                        'resilience': resilience_score
                                    })
                            except Exception as e:
                                continue
        
        # Extract resilient sectors
        if "=== MOST RESILIENT TO 2020 SHOCK ===" in content:
            start_marker = "=== MOST RESILIENT TO 2020 SHOCK ==="
            end_marker = "=== FORECAST BACKTEST RESULTS ==="
            
            start_idx = content.find(start_marker)
            end_idx = content.find(end_marker)
            
            if start_idx != -1 and end_idx != -1:
                section = content[start_idx:end_idx]
                lines = section.split('\n')
                
                for line in lines:
                    if '|' in line and not line.startswith('|:') and not '2020 Resilience Score' in line and not 'Industry' in line:
                        parts = [part.strip() for part in line.split('|') if part.strip()]
                        if len(parts) >= 2:
                            industry = parts[0]
                            if industry and industry not in ['Industry', '']:
                                score = parts[1] if len(parts) > 1 else 'N/A'
                                results['resilient_sectors'].append({
                                    'industry': industry,
                                    'score': score
                                })
        
        # Extract forecast results  
        if "=== FORECAST BACKTEST RESULTS ===" in content:
            start_marker = "=== FORECAST BACKTEST RESULTS ==="
            start_idx = content.find(start_marker)
            
            if start_idx != -1:
                section = content[start_idx:]
                
                # Extract lowest MAPE (most predictable)
                if "5 Lowest MAPE" in section:
                    low_mape_start = section.find("5 Lowest MAPE")
                    high_mape_start = section.find("5 Highest MAPE")
                    
                    if low_mape_start != -1:
                        if high_mape_start != -1:
                            low_mape_section = section[low_mape_start:high_mape_start]
                        else:
                            low_mape_section = section[low_mape_start:low_mape_start + 500]  # Take next 500 chars
                        
                        lines = low_mape_section.split('\n')
                        best_forecast = []
                        for line in lines:
                            if '|' in line and not line.startswith('|:') and not 'MAPE' in line and not 'Industry' in line:
                                parts = [part.strip() for part in line.split('|') if part.strip()]
                                if len(parts) >= 2:
                                    industry = parts[0]
                                    mape = parts[1]
                                    if industry and industry not in ['Industry', '']:
                                        best_forecast.append({'industry': industry, 'mape': mape})
                        results['forecast_results']['best_predictable'] = best_forecast
                
                # Extract highest MAPE (least predictable)
                if "5 Highest MAPE" in section:
                    high_mape_start = section.find("5 Highest MAPE")
                    if high_mape_start != -1:
                        high_mape_section = section[high_mape_start:high_mape_start + 500]  # Take next 500 chars
                        lines = high_mape_section.split('\n')
                        worst_forecast = []
                        for line in lines:
                            if '|' in line and not line.startswith('|:') and not 'MAPE' in line and not 'Industry' in line:
                                parts = [part.strip() for part in line.split('|') if part.strip()]
                                if len(parts) >= 2:
                                    industry = parts[0]
                                    mape = parts[1]
                                    if industry and industry not in ['Industry', '']:
                                        worst_forecast.append({'industry': industry, 'mape': mape})
                        results['forecast_results']['worst_predictable'] = worst_forecast
        
        return results
    
    def categorize_question(self, question):
        """Categorize user question based on keywords"""
        question_lower = question.lower()
        categories = []
        
        for category, keywords in self.keywords.items():
            if any(keyword in question_lower for keyword in keywords):
                categories.append(category)
        
        return categories if categories else ['general']
    
    def generate_response(self, question):
        """Generate response based on question category and use analysis tools"""
        categories = self.categorize_question(question)
        
        # Check if user wants fresh analysis
        if any(word in question.lower() for word in ['run', 'analyze', 'fresh', 'new', 'update', 'calculate']):
            return self.run_fresh_analysis(question)
        elif 'investment' in categories:
            return self.investment_advice_with_data(question)
        elif 'resilience' in categories:
            return self.resilience_insights_with_data(question)
        elif 'growth' in categories:
            return self.growth_analysis_with_data(question)
        elif 'forecast' in categories:
            return self.forecast_insights_with_data(question)
        elif 'industries' in categories or 'space' in categories:
            return self.industry_insights_with_data(question)
        else:
            return self.general_space_info_with_data(question)
    
    def run_fresh_analysis(self, question):
        """Run fresh analysis using R script"""
        st.info("🔄 Running fresh space economy analysis...")
        
        with st.spinner("Analyzing 12 years of BEA space economy data..."):
            results = self.run_analysis_tool('run_full_analysis')
        
        if isinstance(results, str) and "Error" in results:
            return f"❌ Analysis failed: {results}\n\nUsing cached data instead."
        
        response = "✅ **Fresh Analysis Complete!**\n\n"
        response += "�� I've just analyzed the latest BEA space economy data (2012-2023) using your R analysis script.\n\n"
        
        if isinstance(results, dict) and results.get('top_investments'):
            response += "📊 **Top Investment Opportunities:**\n"
            for i, inv in enumerate(results['top_investments'][:3], 1):
                response += f"{i}. **{inv['industry']}** (Score: {inv['investability']})\n"
            response += "\n"
        
        response += "💡 **What would you like to know about these results?**\n"
        response += "• Investment recommendations\n"
        response += "• Resilience analysis\n" 
        response += "• Growth trends\n"
        response += "• Market forecasts\n"
        
        return response
    
    def investment_advice_with_data(self, question):
        """Provide investment advice using real analysis data"""
        results = self.read_analysis_results()
        
        if isinstance(results, str):
            return f"📊 {results}\n\nPlease ask me to run a fresh analysis first."
        
        response = "💰 **Live Space Economy Investment Analysis:**\n\n"
        
        if results.get('top_investments'):
            response += "🏆 **TOP INVESTMENT OPPORTUNITIES (Based on BEA Data Analysis):**\n\n"
            for i, pick in enumerate(results['top_investments'][:5], 1):
                response += f"**{i}. {pick['industry']}**\n"
                response += f"   • Overall Score: {pick['overall_score']}\n"
                response += f"   • Investability Score: {pick['investability']}\n"
                response += f"   • Growth Score: {pick['growth']}\n"
                response += f"   • Resilience Score: {pick['resilience']}\n\n"
        
        if results.get('pitch_table'):
            response += "🎯 **DETAILED INVESTOR PITCH (Top 3 Robust Selections):**\n\n"
            for i, pitch in enumerate(results['pitch_table'], 1):
                response += f"**{i}. {pitch['industry']}**\n"
                response += f"• Investability: {pitch['investability']}\n"
                response += f"• Growth Score: {pitch['growth']}\n"
                response += f"• Resilience Score: {pitch['resilience']}\n"
                response += f"• Key Metrics: {pitch['talking_point']}\n\n"
        
        # Add forecast insights if available
        if results.get('forecast_results', {}).get('best_predictable'):
            response += "📈 **MOST PREDICTABLE INVESTMENTS (Low Forecast Error):**\n"
            for pred in results['forecast_results']['best_predictable'][:3]:
                response += f"• {pred['industry']} (Forecast Error: {pred['mape']})\n"
            response += "\n"
        
        response += "💡 **Investment Strategy Recommendation:**\n"
        response += "Based on 12 years of BEA space economy data, these sectors show the best combination of:\n"
        response += "• Strong growth potential\n"
        response += "• Market resilience (survived 2020 shock)\n"
        response += "• Predictable performance patterns\n"
        response += "• Real economic contribution to space industry\n\n"
        response += "🔍 **Data Source:** Bureau of Economic Analysis Space Economy Real Value Added (2012-2023)"
        
        return response
    
    def resilience_insights_with_data(self, question):
        """Provide resilience insights using real analysis data"""
        results = self.read_analysis_results()
        
        if isinstance(results, str):
            return f"🛡️ {results}\n\nPlease ask me to run a fresh analysis first."
        
        response = "🛡️ **2020 PANDEMIC SHOCK RESILIENCE ANALYSIS:**\n\n"
        
        if results.get('resilient_sectors'):
            response += "🏆 **MOST RESILIENT SECTORS TO 2020 SHOCK:**\n\n"
            for i, sector in enumerate(results['resilient_sectors'][:8], 1):
                response += f"{i}. **{sector['industry']}** - Resilience Score: {sector['score']}\n"
            
            response += "\n💡 **KEY INSIGHTS:**\n"
            if results['resilient_sectors']:
                response += f"• **Top Performer:** {results['resilient_sectors'][0]['industry']} (Score: {results['resilient_sectors'][0]['score']})\n"
            response += "• These sectors maintained stability during the pandemic crisis\n"
            response += "• Space-related infrastructure proved essential during lockdowns\n"
            response += "• Transportation and logistics adapted quickly to new demands\n\n"
            
            response += "🔍 **Why This Matters for Investment:**\n"
            response += "• Resilient sectors are safer long-term investments\n"
            response += "• They provide stability during economic uncertainty\n"
            response += "• Essential services maintain revenue streams in crises\n"
            response += "• Government-backed sectors show consistent support\n\n"
        
        # Cross-reference with top investments
        if results.get('top_investments'):
            resilient_and_top = []
            resilient_names = [r['industry'] for r in results['resilient_sectors'][:5]]
            for inv in results['top_investments'][:5]:
                if any(resilient in inv['industry'] or inv['industry'] in resilient for resilient in resilient_names):
                    resilient_and_top.append(inv['industry'])
            
            if resilient_and_top:
                response += "🎯 **SECTORS THAT ARE BOTH HIGH-SCORING AND RESILIENT:**\n"
                for sector in resilient_and_top[:3]:
                    response += f"• {sector}\n"
                response += "\n"
        
        response += "📊 **Analysis Method:** Measured actual performance drop during 2020 pandemic shock using BEA space economy data"
        
        return response
    
    def growth_analysis_with_data(self, question):
        """Provide growth analysis using real data"""
        results = self.read_analysis_results()
        
        if isinstance(results, str):
            return f"📈 {results}\n\nPlease ask me to run a fresh analysis first."
        
        response = "📈 **SPACE ECONOMY GROWTH ANALYSIS (2012-2023):**\n\n"
        
        if results.get('top_investments'):
            response += "🚀 **HIGH-GROWTH SPACE SECTORS:**\n\n"
            # Sort by growth score - handle both numeric and string values
            growth_sorted = sorted(results['top_investments'], 
                                 key=lambda x: float(x['growth']) if str(x['growth']).replace('.','').isdigit() else 0, 
                                 reverse=True)
            
            for i, sector in enumerate(growth_sorted[:5], 1):
                response += f"{i}. **{sector['industry']}**\n"
                response += f"   • Growth Score: {sector['growth']}\n"
                response += f"   • Overall Score: {sector['overall_score']}\n"
                response += f"   • Resilience Score: {sector['resilience']}\n\n"
            
            response += "🌟 **KEY GROWTH DRIVERS (From BEA Data):**\n"
            if growth_sorted:
                top_growth = growth_sorted[0]
                response += f"• **Top Performer:** {top_growth['industry']} (Score: {top_growth['growth']})\n"
            response += "• Technology integration accelerating space capabilities\n"
            response += "• Government defense spending driving rapid expansion\n"
            response += "• Commercial space markets creating new opportunities\n"
            response += "• Infrastructure development supporting long-term growth\n\n"
            
            response += "💰 **GROWTH INVESTMENT STRATEGY:**\n"
            response += "• Focus on top 3 growth sectors for maximum potential\n"
            response += "• Balance growth with resilience scores for risk management\n"
            response += "• Consider overall score for comprehensive evaluation\n"
            response += "• Monitor space economy trends for emerging opportunities\n\n"
        
        response += "📊 **Analysis Period:** 12 years of BEA space economy real value added data"
        
        return response
    
    def forecast_insights_with_data(self, question):
        """Provide forecast insights using real analysis data"""
        results = self.read_analysis_results()
        
        if isinstance(results, str):
            return f"🔮 {results}\n\nPlease ask me to run a fresh analysis first."
        
        response = "🔮 **FORECAST BACKTEST ANALYSIS:**\n\n"
        
        # Show most predictable sectors
        if results.get('forecast_results', {}).get('best_predictable'):
            response += "🎯 **MOST PREDICTABLE SECTORS (Low Forecast Error - MAPE):**\n\n"
            for i, pred in enumerate(results['forecast_results']['best_predictable'], 1):
                response += f"{i}. **{pred['industry']}** - Forecast Error: {pred['mape']}\n"
            
            response += "\n💡 **What This Means:**\n"
            response += "• These sectors have consistent, predictable growth patterns\n"
            response += "• Lower forecast error = more reliable investment projections\n"
            response += "• MAPE <10% is considered excellent predictability\n\n"
        
        # Show least predictable sectors  
        if results.get('forecast_results', {}).get('worst_predictable'):
            response += "⚠️ **HIGHEST VOLATILITY SECTORS (High Forecast Error - MAPE):**\n\n"
            for i, pred in enumerate(results['forecast_results']['worst_predictable'], 1):
                response += f"{i}. **{pred['industry']}** - Forecast Error: {pred['mape']}\n"
            
            response += "\n🎲 **What This Means:**\n"
            response += "• These sectors are harder to predict but may offer higher rewards\n"
            response += "• High volatility can mean both higher risk and higher potential returns\n"
            response += "• MAPE >30% indicates significant unpredictability\n\n"
        
        response += "🎯 **FORECAST-BASED INVESTMENT STRATEGY:**\n\n"
        
        if results.get('forecast_results'):
            # Find sectors that are both top investments and predictable
            if results.get('top_investments') and results['forecast_results'].get('best_predictable'):
                predictable_names = [p['industry'] for p in results['forecast_results']['best_predictable']]
                top_and_predictable = []
                for inv in results['top_investments'][:5]:
                    if any(pred in inv['industry'] or inv['industry'] in pred for pred in predictable_names):
                        top_and_predictable.append(inv['industry'])
                
                if top_and_predictable:
                    response += "🏆 **IDEAL INVESTMENTS (High Score + Predictable):**\n"
                    for sector in top_and_predictable:
                        response += f"• {sector}\n"
                    response += "\n"
        
        response += "💰 **Recommendation:**\n"
        response += "• **Conservative Strategy:** Focus on predictable sectors (low MAPE)\n"
        response += "• **Aggressive Strategy:** Include some high-volatility, high-reward sectors\n"
        response += "• **Balanced Strategy:** Combine predictable base with selective volatile picks\n\n"
        
        response += "📈 **MAPE Guide:** <10% excellent · 10-20% good · 20-30% fair · >30% unpredictable"
        
        return response
    
    def industry_insights_with_data(self, question):
        """Provide industry insights using real data"""
        results = self.read_analysis_results()
        
        response = "🏭 **Live Space Industry Analysis:**\n\n"
        
        if isinstance(results, dict) and results.get('top_investments'):
            response += "📊 **Key Findings from Current Analysis:**\n\n"
            
            # Get top performer
            if results['top_investments']:
                top = results['top_investments'][0]
                response += f"🥇 **Top Performer:** {top['industry']}\n"
                response += f"   • Overall Score: {top['investability']}\n"
                response += f"   • Growth Potential: {top['growth']}\n"
                response += f"   • Market Resilience: {top['resilience']}\n\n"
            
            response += "🌟 **Industry Trends:**\n"
            response += "• Space economy shows consistent growth (2012-2023)\n"
            response += "• Technology sectors lead in growth metrics\n"
            response += "• Defense spending drives rapid expansion\n"
            response += "• Manufacturing critical for space infrastructure\n\n"
            
            response += "💡 **Ask me to 'run fresh analysis' for the latest industry data.**"
        
        return response
    
    def general_space_info_with_data(self, question):
        """Provide general info using real analysis data"""
        response = "🌌 **Space Economy Analysis Dashboard:**\n\n"
        response += "Welcome to your live space economy analysis system! I can access and analyze real BEA data using your R analysis tools.\n\n"
        
        response += "🔧 **Available Analysis Tools:**\n"
        response += "• **Fresh Analysis**: 'Run new analysis' - Execute full R script\n"
        response += "• **Investment Advice**: Get top picks based on current data\n"
        response += "• **Resilience Analysis**: 2020 shock resistance data\n"
        response += "• **Growth Trends**: 12-year sector growth analysis\n"
        response += "• **Market Forecasts**: Predictability and volatility insights\n\n"
        
        response += "📊 **Data Source:** Bureau of Economic Analysis (2012-2023)\n"
        response += "🔄 **Analysis Engine:** Your custom R analysis script\n\n"
        
        response += "💡 **Try asking:**\n"
        response += "• 'Run fresh analysis for latest data'\n"
        response += "• 'What are the best investments right now?'\n"
        response += "• 'Which sectors survived COVID best?'\n"
        response += "• 'Show me current growth trends'\n"
        
        return response

def main():
    # Main header with enhanced space theme
    st.markdown('<h1 class="main-header">🚀 Space Economy Investment Advisor</h1>', unsafe_allow_html=True)
    st.markdown("*Your AI guide to space industry investment opportunities*")
    
    # Initialize bot
    if 'bot' not in st.session_state:
        st.session_state.bot = SpaceEconomyBot()
    
    # Initialize chat history
    if 'messages' not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "🛰️ Welcome! I'm your **Live Space Economy Investment Advisor** with integrated R analysis tools!\n\n🔧 **What I can do:**\n• **Run fresh analysis** using your R script and BEA data\n• **Investment recommendations** based on real-time calculations\n• **Market resilience analysis** from actual 2020 shock data\n• **Growth trend insights** from 12-year analysis\n• **Industry forecasts** with predictability metrics\n\n🚀 **Try these commands:**\n• 'Run fresh analysis' - Execute your R script\n• 'What are the best investments?' - Get live recommendations\n• 'Which sectors survived COVID?' - Resilience analysis\n• 'Show me growth trends' - Live growth data\n\n💡 **I use your actual `data_analysis_clean.r` script as a tool to provide real-time insights!**"
            }
        ]
    
    # Create two columns for layout
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Display chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        
        # Chat input
        if prompt := st.chat_input("Ask me about space economy investments..."):
            # Add user message
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            
            # Generate and add assistant response
            with st.chat_message("assistant"):
                with st.spinner("Analyzing space economy data..."):
                    response = st.session_state.bot.generate_response(prompt)
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})
    
    with col2:
        # Enhanced sidebar with space theme
        st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
        st.markdown("### 🚀 Analysis Tools")
        
        # Quick action buttons with proper handling
        if st.button("🔄 Run Fresh Analysis", key="fresh_analysis", use_container_width=True):
            st.session_state.messages.append({"role": "user", "content": "Run fresh space economy analysis"})
            with st.spinner("Running R analysis..."):
                response = st.session_state.bot.run_fresh_analysis("run analysis")
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()
        
        if st.button("💰 Top Investment Picks", key="investments", use_container_width=True):
            st.session_state.messages.append({"role": "user", "content": "Show me top investment picks"})
            response = st.session_state.bot.investment_advice_with_data("investment advice")
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()
        
        if st.button("📈 Growth Leaders", key="growth", use_container_width=True):
            st.session_state.messages.append({"role": "user", "content": "Show me growth leaders"})
            response = st.session_state.bot.growth_analysis_with_data("growth trends")
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()
        
        if st.button("🛡️ Resilient Sectors", key="resilience", use_container_width=True):
            st.session_state.messages.append({"role": "user", "content": "Show me resilient sectors"})
            response = st.session_state.bot.resilience_insights_with_data("resilience analysis")
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()
        
        if st.button("🔮 Market Forecast", key="forecast", use_container_width=True):
            st.session_state.messages.append({"role": "user", "content": "Show me market forecast"})
            response = st.session_state.bot.forecast_insights_with_data("forecast analysis")
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()
        
        st.markdown("---")
        
        # Analysis status with enhanced styling
        if os.path.exists('analysis_results.txt'):
            st.success("✅ Analysis Results Available")
            mod_time = os.path.getmtime('analysis_results.txt')
            st.caption(f"Last updated: {datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d %H:%M')}")
        else:
            st.warning("⚠️ No analysis results found")
            st.caption("Click 'Run Fresh Analysis' to generate")
        
        # Data source info
        st.markdown("**🔧 Analysis Engine:** R Script Integration")
        st.markdown("**📊 Data Source:** Bureau of Economic Analysis (2012-2023)")
        st.markdown("**🎯 Analysis Period:** 12 years of space economy data")
        
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
